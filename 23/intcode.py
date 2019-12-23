class Program:
    def __init__(self, memory, input):
        self.memory = memory
        self.input = input
        self.output = []
        self.pc = 0
        self.halted = False
        self.awaiting_input = False
        self.relative_base = 0

    def append(self, instruction):
        self.input.append(instruction)

    def pop(self):
        return self.output.pop(0)

    def dump(self):
        tmp = self.output
        self.output = []
        return tmp

    def get(self, address):
        if address < 0:
            raise Exception('Reading from negative memory address')
        if address not in self.memory:
            return 0
        return self.memory[address]

    def set(self, address, value):
        if address < 0:
            raise Exception('Writing to negative memory address')
        self.memory[address] = value
        return self

    def op(self):
        return self.get(self.pc) % 10**2

    def op_mode(self, p):
        return (self.get(self.pc) // 10**(p + 1)) % 10

    def param(self, offset, mode):
        value = self.get(self.pc + offset)
        if mode == 0:  # position
            return self.get(value)
        elif mode == 1:  # immediate
            return value
        elif mode == 2:  # relative
            return self.get(self.relative_base + value)
        raise Exception('Unrecognized mode')

    def p_modal(self, p):
        return self.param(p, self.op_mode(p))

    def p_position(self, p):
        return self.param(p, 0)

    def p_immediate(self, p):
        return self.param(p, 1)

    def p_relative(self, p):
        return self.param(p, 2)

    def p_write(self, p):
        if self.op_mode(p) == 2:
            return self.relative_base + self.p_immediate(p)
        return self.p_immediate(p)

    def add(self):
        self.set(self.p_write(3), self.p_modal(1) + self.p_modal(2))
        self.pc += 4

    def mul(self):
        self.set(self.p_write(3), self.p_modal(1) * self.p_modal(2))
        self.pc += 4

    def read(self):
        if len(self.input) == 0:
            self.awaiting_input = True
            return
        self.set(self.p_write(1), self.input.pop(0))
        self.pc += 2

    def write(self):
        self.output.append(self.p_modal(1))
        self.pc += 2

    def jump_if_true(self):
        if self.p_modal(1) != 0:
            self.pc = self.p_modal(2)
        else:
            self.pc += 3

    def jump_if_false(self):
        if self.p_modal(1) == 0:
            self.pc = self.p_modal(2)
        else:
            self.pc += 3

    def less_than(self):
        if self.p_modal(1) < self.p_modal(2):
            self.set(self.p_write(3), 1)
        else:
            self.set(self.p_write(3), 0)
        self.pc += 4

    def equals(self):
        if self.p_modal(1) == self.p_modal(2):
            self.set(self.p_write(3), 1)
        else:
            self.set(self.p_write(3), 0)
        self.pc += 4

    def relative_base_offset(self):
        self.relative_base += self.p_modal(1)
        self.pc += 2

    def step(self):
        op = self.op()
        if op == 99:
            self.halted = True
        elif op == 1:  # add
            self.add()
        elif op == 2:  # mul
            self.mul()
        elif op == 3:  # input
            self.read()
            if self.awaiting_input:
                return
        elif op == 4:  # output
            self.write()
        elif op == 5:  # jump-if-true
            self.jump_if_true()
        elif op == 6:  # jump-if-false
            self.jump_if_false()
        elif op == 7:  # less-than
            self.less_than()
        elif op == 8:  # equals
            self.equals()
        elif op == 9:  # relative_base_offset
            self.relative_base_offset()
        else:
            raise RuntimeError("Unknown opcode")

    def run(self):
        if self.awaiting_input:
            if len(self.input) > 0:
                self.awaiting_input = False
            else:
                raise RuntimeError('Awaiting input')
        while True:
            self.step()
            if self.halted:
                return

    def __str__(self):
        return str({
            'memory': self.memory,
            'input': self.input,
            'output': self.output,
            'pc': self.pc,
            'halted': self.halted,
            'awaiting_input': self.awaiting_input,
            'relative_base': self.relative_base
        })


def solve(memory, input):
    p = Program(memory, input)
    p.run()
    if p.awaiting_input:
        raise Exception('Missing input')
    return p.output


def read(filename):
    memory = {}
    with open(filename, 'r') as f:
        for k, n in enumerate(f.readline().split(',')):
            memory[k] = int(n)
    return memory


def main(filename, input):
    print(solve(read(filename), input))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    main(sys.argv[1], [int(n) for n in sys.argv[2:]])
