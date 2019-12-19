from intcode import Program


def display(tractor, xlim, ylim):
    output = []
    for y in range(ylim):
        row = []
        for x in range(xlim):
            if (x, y) in tractor:
                row.append('#')
            else:
                row.append('.')
        output.append(''.join(row))
    return '\n'.join(output)


def isTractor(memory, x, y):
    program = Program(memory.copy(), [x, y])
    program.run()
    return program.pop()


def solve(memory):
    left = 0
    y = 200
    while True:
        while not isTractor(memory, left, y):
            left += 1
        if isTractor(memory, left + 100, y - 100):
            return left * 10000 + y - 100
        y += 1


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
