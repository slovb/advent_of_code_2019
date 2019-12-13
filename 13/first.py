from intcode import Program


def solve(memory):
    program = Program(memory, [])
    state = {}
    count = 0
    while not program.halted:
        program.run()
        while len(program.output) > 0:
            x, y, id = program.pop(), program.pop(), program.pop()
            state[(x, y)] = id
            if id == 2:
                count += 1
    return count


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
