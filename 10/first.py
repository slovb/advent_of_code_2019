def crossProduct(u, v):
    return u[0]*v[1] - u[1]*v[0]


def dotProduct(u, v):
    return u[0]*v[0] + u[1]*v[1]


def diff(u, v):
    return (u[0] - v[0], u[1] - v[1])


# is c on the line a-b?
def isBetween(a, b, c):
    ba = diff(b, a)
    ca = diff(c, a)
    if crossProduct(ba, ca) != 0:
        return False
    dot = dotProduct(ba, ca)
    if dot < 0 or dot > dotProduct(ba, ba):
        return False
    return True


def canSee(p, t, data):
    for b in data:
        if b == p or b == t:
            continue
        if isBetween(p, t, b):
            return False
    return True


def countViewable(p, data):
    c = 0
    for t in data:
        if t == p:
            continue
        if canSee(p, t, data):
            c += 1
    return c


def solve(data):
    bestP = data[0]
    bestC = -1
    for p in data:
        c = countViewable(p, data)
        if c > bestC:
            bestC = c
            bestP = p
    return bestC, bestP


def read(filename):
    data = []
    with open(filename, 'r') as f:
        for y, l in enumerate(f.readlines()):
            for x, c in enumerate(l):
                if c == '#':
                    data.append((x, y))
    return data


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        main(f)
