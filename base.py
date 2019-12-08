def solve(data):
    return data


def read(filename):
    with open(filename, 'r') as f:
        #  return [row.rstrip().split(')') for row in f.readlines()]
        return [int(n) for n in f.readline().split(',')]


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
