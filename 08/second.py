def solve(data):
    width = 25
    height = 6
    size = width * height
    image = [2]*size
    for k, d in enumerate(data):
        i = k % size
        if d != 2:
            if image[i] == 2:
                image[i] = d
    cmap = [' ', '*']
    for j in range(height):
        print(''.join([cmap[i] for i in image[j*width:(j+1)*width]]))


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
