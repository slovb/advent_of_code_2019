from intcode import Program


def solve(memory):
    program = Program(memory, [])
    while not program.halted:
        program.run()
    return program.output


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
