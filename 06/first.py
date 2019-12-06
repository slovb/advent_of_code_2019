def trace(n, tree):
    if n == 'COM':
        return 0
    return 1 + trace(tree[n], tree)


def solve(data):
    tree = {}
    for d in data:
        tree[d[1]] = d[0]
    total = 0
    for n in tree:
        total += trace(n, tree)
    return total


def read(filename):
    with open(filename, 'r') as f:
        return [row.rstrip().split(')') for row in f.readlines()]


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
