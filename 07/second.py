class Program:
    def __init__(self, memory, input):
        self.memory = memory
        self.input = input
        self.output = []
        self.pc = 0
        self.halted = False
        self.awaitingInput = False

    def op(self): return self.memory[self.pc] % 10**2

    def op_mode(self, p): return (self.memory[self.pc] // 10**(p + 1)) % 10

    def param(self, offset, mode):
        if mode == 0:
            return self.memory[self.memory[self.pc + offset]]
        return self.memory[self.pc + offset]

    def p_modal(self, p): return self.param(p, self.op_mode(p))
    def p_position(self, p): return self.param(p, 0)
    def p_immediate(self, p): return self.param(p, 1)

    def add(self):
        self.memory[self.p_immediate(3)] = \
            self.p_modal(1) + self.p_modal(2)
        self.pc += 4

    def mul(self):
        self.memory[self.p_immediate(3)] = \
            self.p_modal(1) * self.p_modal(2)
        self.pc += 4

    def read(self):
        if len(self.input) == 0:
            self.awaitingInput = True
            return
        self.memory[self.p_immediate(1)] = self.input.pop(0)
        self.pc += 2

    def write(self):
        self.output.append(self.p_position(1))
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
            self.memory[self.p_immediate(3)] = 1
        else:
            self.memory[self.p_immediate(3)] = 0
        self.pc += 4

    def equals(self):
        if self.p_modal(1) == self.p_modal(2):
            self.memory[self.p_immediate(3)] = 1
        else:
            self.memory[self.p_immediate(3)] = 0
        self.pc += 4

    def run(self):
        if self.awaitingInput:
            if len(self.input) > 0:
                self.awaitingInput = False
            else:
                raise RuntimeError('Awaiting input')
        while True:
            op = self.op()
            if op == 99:
                self.halted = True
                break
            elif op == 1:  # add
                self.add()
            elif op == 2:  # mul
                self.mul()
            elif op == 3:  # input
                self.read()
                if self.awaitingInput:
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
            else:
                raise RuntimeError("Unknown opcode")

    def __str__(self):
        return str({
            'memory': self.memory,
            'input': self.input,
            'output': self.output,
            'pc': self.pc,
            'halted': self.halted,
            'awaitingInput': self.awaitingInput
        })


def runAllConcurrent(programs):
    previousProgram = programs[-1]
    while True:
        for program in programs:
            while len(previousProgram.output) > 0:
                program.input.append(previousProgram.output.pop(0))
            if program.halted:              # assume all are halted when we
                return program.input.pop()  # get to an already halted
            program.run()
            previousProgram = program


def runGivenPhases(memory, phases):
    programs = []
    for p in phases:
        programs.append(Program(memory.copy(), [p]))
    programs[0].input.append(0)
    return runAllConcurrent(programs)


def solve(memory):
    import itertools
    maxOutput = 0
    for phases in itertools.permutations([5, 6, 7, 8, 9]):
        maxOutput = max(maxOutput, runGivenPhases(memory, phases))
    return maxOutput


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(',')]


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
