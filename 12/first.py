class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]

    def energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def kinetic_energy(self):
        return sum(abs(v) for v in self.velocity)

    def potential_energy(self):
        return sum(abs(p) for p in self.position)

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
    moons = [Moon(pos) for pos in data]
    for i in range(1000):
        for moon in moons:
            for other in moons:
                if moon == other:
                    continue
                moon.apply_moon_gravity(other)
        for moon in moons:
            moon.update()
    return sum([moon.energy() for moon in moons])


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
