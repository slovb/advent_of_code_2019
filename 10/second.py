def crossProduct(u, v):
    return u[0]*v[1] - u[1]*v[0]


def dotProduct(u, v):
    return u[0]*v[0] + u[1]*v[1]


def diff(u, v):
    return (u[0] - v[0], u[1] - v[1])


# is c on the line a-b
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


def clockAngle(pt):
    import math
    # this is NOT the typical atan2 use, the flipped
    # order is a simple reflection about y=x line
    # then the - is due to the change in coordinate system
    # This makes the positive angles correct
    angle = math.atan2(pt[0], -pt[1])
    if angle < 0:
        angle += 2 * math.pi
    return angle


def process(p, t):
    pt = diff(t, p)
    return (clockAngle(pt), t)


def solve(data, p):
    # I already know there are more than 200 visible asteroids
    # so I don't have to do a full rotation and handle deleted asteroids
    visible = []
    for t in data:
        if canSee(p, t, data):
            visible.append(process(p, t))
    visible.sort()
    mr200 = visible[199]
    return mr200[1][0] * 100 + mr200[1][1]


def read(filename):
    data = []
    with open(filename, 'r') as f:
        for y, l in enumerate(f.readlines()):
            for x, c in enumerate(l):
                if c == '#':
                    data.append((x, y))
    return data


def main(filename):
    print(solve(read(filename), (11, 13)))


if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        main(f)
