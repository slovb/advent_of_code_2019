def trace(n, tree, mem, c=0):
    if n in mem:
        return c + mem[n]
    mem[n] = c
    if n != 'COM':
        return trace(tree[n], tree, mem, c + 1)
    return -1


def solve(data):
    tree = {}
    mem = {}
    for d in data:
        tree[d[1]] = d[0]
    trace(tree['SAN'], tree, mem)
    return trace(tree['YOU'], tree, mem)


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
