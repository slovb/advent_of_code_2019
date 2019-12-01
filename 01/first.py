def calc(mass):
    return (mass // 3) - 2


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
