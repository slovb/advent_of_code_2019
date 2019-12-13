class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]

    def apply_moon_gravity(self, moon):
        for i in range(3):
            if self.position[i] < moon.position[i]:
                self.velocity[i] += 1
            elif self.position[i] > moon.position[i]:
                self.velocity[i] -= 1

    def update(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def __str__(self):
        return '{}\t{}'.format(self.position, self.velocity)


def solve(data):
    def tokenize(moons):
        values = []
        for m in moons:
            for p in m.position:
                values.append(p)
            for v in m.velocity:
                values.append(v)
        return tuple(values)

    moons = [Moon(pos) for pos in data]
    mem = set()
    current = tokenize(moons)

    i = 0
    while current not in mem:
        mem.add(current)
        for moon in moons:
            for other in moons:
                if moon == other:
                    continue
                moon.apply_moon_gravity(other)
        for moon in moons:
            moon.update()
        current = tokenize(moons)
        i += 1
        if i % 10**3 == 0:
            print(i)
    return i


def read(filename):
    def parse(row):
        parts = row.split(',')
        reduced = []
        for part in parts:
            reduced.append(int(part.split('=')[1].rstrip('>\n')))
        return reduced
    with open(filename, 'r') as f:
        return [parse(row) for row in f.readlines()]


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
