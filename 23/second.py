from intcode import Program


def notHalted(programs):
    for p in programs:
        if not p.halted:
            return True
    return False


def isIdle(programs):
    for p in programs:
        if len(p.input) > 0 and p.input[0] != -1:
            return False
    return True


def solve(memory):
    programs = []
    inputBuffer = {}
    nat = None
    mem = set()
    for i in range(50):
        programs.append(Program(memory.copy(), [i]))
        inputBuffer[i] = []
    while notHalted(programs):
        # send out input
        for i, program in enumerate(programs):
            if len(program.input) == 1 and program.input[0] == -1:
                program.input.pop()
            while len(inputBuffer[i]) > 0:
                x, y = inputBuffer[i].pop(0)
                program.append(x)
                program.append(y)
        # check idleness
        if nat is not None and isIdle(programs):
            programs[0].append(nat[0])
            programs[0].append(nat[1])
            print(nat[1])
            if nat[1] in mem:
                return nat[1]
            mem.add(nat[1])
            nat = None
        # do a step
        for program in programs:
            if program.halted:
                continue
            # default input
            if len(program.input) == 0:
                program.append(-1)
            program.step()
            while len(program.output) > 2:
                dst = program.pop()
                x = program.pop()
                y = program.pop()
                if dst == 255:
                    nat = (x, y)
                else:
                    inputBuffer[dst].append((x, y))
    raise Exception('Should end early')


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
