def calc(mass):
    step = lambda m: (m // 3) - 2
    fuel = step(mass)
    total = 0
    while fuel > 0:
        total += fuel
        fuel = step(fuel)
    return total


def solve(data):
    total = 0
    for mass in data:
        fuel = calc(mass)
        print("Mass: {}\t, Fuel: {}".format(mass, fuel))
        total += fuel
    return total


def read(filename):
    with open(filename, 'r') as f:
        return [int(l) for l in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\nTotal fuel requirement {}".format(main(f)))
