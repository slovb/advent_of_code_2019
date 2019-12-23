from intcode import Program


def notHalted(programs):
    for p in programs:
        if not p.halted:
            return True
    return False


def solve(memory):
    programs = []
    inputBuffer = {}
    for i in range(50):
        programs.append(Program(memory.copy(), [i]))
        inputBuffer[i] = []
    while notHalted(programs):
        # send out input
        for i, program in enumerate(programs):
            while len(inputBuffer[i]) > 0:
                x, y = inputBuffer[i].pop(0)
                program.append(x)
                program.append(y)
            if len(program.input) == 0:
                program.append(-1)
        # do a step
        for program in programs:
            if program.halted:
                continue
            program.step()
            while len(program.output) > 2:
                dst = program.pop()
                x = program.pop()
                y = program.pop()
                if dst == 255:
                    return y
                inputBuffer[dst].append((x, y))


def read(filename):
    memory = {}
    with open(filename, 'r') as f:
        for k, n in enumerate(f.readline().split(',')):
            memory[k] = int(n)
    return memory


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
