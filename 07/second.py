class Program:
    def __init__(self, memory, input):
        self.memory = memory
        self.input = input
        self.output = []
        self.pc = 0
        self.halted = False
        self.awaitingInput = False

    def param(self, offset, mode):
        if mode == 0:
            return self.memory[self.memory[self.pc + offset]]
        return self.memory[self.pc + offset]

    def param1(self, op): return self.param(1, op[1])
    def param1Immediate(self): return self.param(1, 1)
    def param1Position(self): return self.param(1, 0)

    def param2(self, op): return self.param(2, op[2])
    def param2Immediate(self): return self.param(2, 1)
    def param2Position(self): return self.param(2, 0)

    def param3(self, op): return self.param(3, op[3])
    def param3Immediate(self): return self.param(3, 1)
    def param3Position(self): return self.param(3, 0)

    def operation(self):
        op = self.memory[self.pc] % 10**2
        c = (self.memory[self.pc] // 10**2) % 10
        b = (self.memory[self.pc] // 10**3) % 10
        a = (self.memory[self.pc] // 10**4) % 10
        return (op, c, b, a)

    def op_add(self, op):
        self.memory[self.param3Immediate()] = \
            self.param1(op) + self.param2(op)
        self.pc += 4

    def op_mul(self, op):
        self.memory[self.param3Immediate()] = \
            self.param1(op) * self.param2(op)
        self.pc += 4

    def op_input(self, op):
        if len(self.input) == 0:
            self.awaitingInput = True
            return
        self.memory[self.param1Immediate()] = self.input.pop(0)
        self.pc += 2

    def op_output(self, op):
        self.output.append(self.param1Position())
        self.pc += 2

    def op_jump_if_true(self, op):
        if self.param1(op) != 0:
            self.pc = self.param2(op)
        else:
            self.pc += 3

    def op_jump_if_false(self, op):
        if self.param1(op) == 0:
            self.pc = self.param2(op)
        else:
            self.pc += 3

    def op_less_than(self, op):
        if self.param1(op) < self.param2(op):
            self.memory[self.param3Immediate()] = 1
        else:
            self.memory[self.param3Immediate()] = 0
        self.pc += 4

    def op_equals(self, op):
        if self.param1(op) == self.param2(op):
            self.memory[self.param3Immediate()] = 1
        else:
            self.memory[self.param3Immediate()] = 0
        self.pc += 4

    def run(self):
        if self.awaitingInput:
            if len(self.input) > 0:
                self.awaitingInput = False
            else:
                raise RuntimeError('Awaiting input')
        while True:
            op = self.operation()
            if op[0] == 99:
                self.halted = True
                break
            elif op[0] == 1:  # add
                self.op_add(op)
            elif op[0] == 2:  # mul
                self.op_mul(op)
            elif op[0] == 3:  # input
                self.op_input(op)
                if self.awaitingInput:
                    return
            elif op[0] == 4:  # output
                self.op_output(op)
            elif op[0] == 5:  # jump-if-true
                self.op_jump_if_true(op)
            elif op[0] == 6:  # jump-if-false
                self.op_jump_if_false(op)
            elif op[0] == 7:  # less-than
                self.op_less_than(op)
            elif op[0] == 8:  # equals
                self.op_equals(op)
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
    #  print(runGivenPhases(read(filename), [9, 8, 7, 6, 5]))
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
