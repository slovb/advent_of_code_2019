from intcode import Program


def display(data):
    return ''.join([str(chr(d)) for d in data])


def parse(data):
    scaffold = {}
    x = 0
    y = 0
    for d in data:
        if d == ord('.'):
            x += 1
        elif d == ord("\n"):
            x = 0
            y += 1
        else:
            scaffold[(x, y)] = d
            x += 1
    return scaffold


def intersection(point, scaffold):
    x, y = point
    if (x - 1, y) not in scaffold or \
       (x + 1, y) not in scaffold or \
       (x, y - 1) not in scaffold or \
       (x, y + 1) not in scaffold:
        return False
    return True


def solve(memory):
    program = Program(memory, [])
    value = 0
    while not program.halted:
        program.run()
        data = program.dump()
        print(display(data))
        scaffold = parse(data)
        for point in scaffold:
            if intersection(point, scaffold):
                value += point[0] * point[1]
    return value


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
