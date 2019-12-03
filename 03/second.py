def traverse(instructions):
    x, y, c = 0, 0, 0
    path = {}
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
            c += 1
            path[(x, y)] = c
    return path


def solve(data):
    path0 = traverse(data[0])
    path1 = traverse(data[1])
    values = []
    for x0, y0 in path0:
        p0 = (x0, y0)
        if p0 in path1:
            values.append(path0[p0] + path1[p0])
    return min(values)


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
