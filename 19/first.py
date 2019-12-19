from intcode import Program


def solve(memory):
    val = 0
    for y in range(50):
        for x in range(50):
            program = Program(memory.copy(), [x, y])
            program.run()
            val += program.pop()
    return val


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
