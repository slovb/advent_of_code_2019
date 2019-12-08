def count(n, size, character, data):
    c = 0
    for i in data[n*size:(n+1)*size]:
        if i == character:
            c += 1
    return c


def solve(data):
    width = 25
    height = 6
    size = width * height
    nLayers = len(data) // size
    leastC = 150
    leastN = -1
    for n in range(nLayers):
        c = count(n, size, 0, data)
        if c < leastC:
            leastC = c
            leastN = n
    return count(leastN, size, 1, data) * count(leastN, size, 2, data)


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline()]


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
