def adjacent(position):
    x, y = position
    return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)


def explore(position, walls, keys, doors, gainedKeys, openedDoors):
    options = []
    explored = {}
    queue = [(position, 0)]
    while len(queue) > 0:
        p, step = queue.pop()
        step += 1
        for a in adjacent(p):
            if a in explored and explored[a] <= step:
                continue
            elif a in walls:
                continue
            explored[a] = step
            if a in keys and keys[a] not in gainedKeys:
                options.append((a, step, keys[a]))
            elif a in doors and doors[a] not in openedDoors:
                if doors[a].lower() in gainedKeys:
                    options.append((a, step, doors[a]))
            else:
                queue.append((a, step))
    return options


globalCurrentBest = None


def subsolve(position, walls, keys, doors, gainedKeys, openedDoors, step):
    global globalCurrentBest
    if globalCurrentBest is not None and step > globalCurrentBest:
        return []
    if len(keys) == len(gainedKeys):
        if globalCurrentBest is None or step < globalCurrentBest:
            globalCurrentBest = step
        return [step]
    options = explore(position, walls, keys, doors, gainedKeys, openedDoors)
    solutions = []
    for option in options:
        p, stepMod, type = option
        if type.isupper():
            parts = subsolve(p, walls, keys, doors,
                             gainedKeys,
                             openedDoors + [type],
                             step + stepMod)
            for part in parts:
                solutions.append(part)
        else:
            parts = subsolve(p, walls, keys, doors,
                             gainedKeys + [type],
                             openedDoors,
                             step + stepMod)
            for part in parts:
                solutions.append(part)
    return solutions


def solve(position, walls, keys, doors):
    gainedKeys = []
    openendDoors = []
    solutions = subsolve(position, walls, keys, doors,
                         gainedKeys, openendDoors, 0)
    return min(solutions)


def read(filename):
    keys = {}
    doors = {}
    walls = set()
    position = ()
    with open(filename, 'r') as f:
        rows = [row.rstrip() for row in f.readlines()]
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                p = (x, y)
                if c == '.':
                    continue
                elif c == '#':
                    walls.add(p)
                elif c == '@':
                    position = p
                elif c.isupper():
                    doors[p] = c
                else:
                    keys[p] = c
    return position, walls, keys, doors


def main(filename):
    position, walls, keys, doors = read(filename)
    print(solve(position, walls, keys, doors))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
