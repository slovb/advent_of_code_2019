def display(grid):
    output = []
    for z in range(-5, 6):
        output.append('Depth {}:'.format(z))
        for y in range(5):
            line = []
            for x in range(5):
                if x == 2 and y == 2:
                    line.append('?')
                elif (x, y, z) in grid:
                    line.append('#')
                else:
                    line.append('.')
            output.append(''.join(line))
        output.append('')
    return '\n'.join(output)


def adjacent(p):
    x, y, z = p
    a = []
    if x == 0 or x == 3:
        a.append((x + 1, y, z))
        if x == 0:
            a.append((1, 2, z - 1))
        elif y == 2:  # x == 3
            for rY in range(5):
                a.append((4, rY, z + 1))
        else:  # x == 3
            a.append(((x - 1) % 5, y, z))
    else:  # x == 1 or x == 4
        a.append((x - 1, y, z))
        if x == 4:
            a.append((3, 2, z - 1))
        elif y == 2:  # x == 1
            for rY in range(5):
                a.append((0, rY, z + 1))
        else:  # x == 1
            a.append(((x + 1) % 5, y, z))

    if y == 0 or y == 3:
        a.append((x, y + 1, z))
        if y == 0:
            a.append((2, 1, z - 1))
        elif x == 2:  # y == 3
            for rX in range(5):
                a.append((rX, 4, z + 1))
        else:  # y == 3
            a.append((x, (y - 1) % 5, z))
    else:  # y == 1 or y == 4
        a.append((x, y - 1, z))
        if y == 4:
            a.append((2, 3, z - 1))
        elif x == 2:  # y == 1
            for rX in range(5):
                a.append((rX, 0, z + 1))
        else:  # y == 1
            a.append((x, (y + 1) % 5, z))
    return a


def test(grid, p):
    if p in grid:
        return 1
    return 0


def subprocess(grid, p, a, update):
    c = sum([test(grid, p) for p in a])
    if p in grid:
        if c == 1:
            update.add(p)
    else:
        if c == 1 or c == 2:
            update.add(p)


def step(grid):
    update = set()
    queue = []
    for p in grid:
        a = adjacent(p)
        subprocess(grid, p, a, update)
        for q in a:
            if q not in grid and q not in queue:
                queue.append(q)
    for p in queue:
        a = adjacent(p)
        subprocess(grid, p, a, update)
    return update


def solve(grid):
    for _ in range(200):
        grid = step(grid)
    #  print(display(grid))
    return len(grid)


def read(filename):
    grid = set()
    y = 0
    with open(filename, 'r') as f:
        for row in f.readlines():
            x = 0
            for c in row.rstrip():
                if x == 2 and y == 2:
                    pass  # recursive hole
                elif c == '#':
                    grid.add((x, y, 0))
                elif c == '.':
                    pass
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
