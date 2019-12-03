def traverse(instructions):
    x, y = 0, 0
    path = set()
    for i in instructions:
        xDiff = 0
        yDiff = 0
        if i[0] == 'L':
            xDiff = -1
        elif i[0] == 'R':
            xDiff = 1
        elif i[0] == 'D':
            yDiff = -1
        else:
            yDiff = 1
        for j in range(i[1]):
            x += xDiff
            y += yDiff
            path.add((x, y))
    return path


def manhattan(p):
    return abs(p[0]) + abs(p[1])


def solve(data):
    path0 = traverse(data[0])
    path1 = traverse(data[1])
    return min([manhattan(p) for p in path0.intersection(path1)])


def read(filename):
    def process(row):
        return [(w[0], int(w[1:])) for w in row.split(',')]
    with open(filename, 'r') as f:
        return (process(f.readline()), process(f.readline()))


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))
