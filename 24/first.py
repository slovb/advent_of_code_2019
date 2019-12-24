def display(grid):
    output = []
    for y in range(5):
        line = []
        for x in range(5):
            if grid[(x, y)]:
                line.append('#')
            else:
                line.append('.')
        output.append(''.join(line))
    return '\n'.join(output) + '\n'


def adjacent(grid, x, y):
    def test(grid, x, y):
        return (x, y) in grid and grid[(x, y)]
    c = 0
    if test(grid, x - 1, y):
        c += 1
    if test(grid, x + 1, y):
        c += 1
    if test(grid, x, y - 1):
        c += 1
    if test(grid, x, y + 1):
        c += 1
    return c


def key(grid):
    v = 0
    for y in range(5):
        for x in range(5):
            if grid[(x, y)]:
                v += 2**(x + 5*y)
    return v


def step(grid):
    update = {}
    for y in range(5):
        for x in range(5):
            a = adjacent(grid, x, y)
            if grid[(x, y)]:
                update[(x, y)] = (a == 1)
            else:
                update[(x, y)] = (a == 1 or a == 2)
    return update


def solve(grid):
    mem = set()
    while True:
        # print(display(grid))
        k = key(grid)
        if k in mem:
            return k
        mem.add(k)
        grid = step(grid)


def read(filename):
    grid = {}
    y = 0
    with open(filename, 'r') as f:
        for row in f.readlines():
            x = 0
            for c in row.rstrip():
                if c == '#':
                    grid[(x, y)] = True
                elif c == '.':
                    grid[(x, y)] = False
                else:
                    raise Exception('Unknown input')
                x += 1
            y += 1
    return grid


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
