def simulate(data, pattern, phase):
    def process(n):
        return abs(n) % 10
    output = []
    for m in range(len(data)):
        psum = []
        for k, v in enumerate(data):
            j = (1 + k) // (m + 1)
            psum.append(v * pattern[j % len(pattern)])
        output.append(process(sum(psum)))
    return output


def solve(data, iterations):
    def process(parts):
        n = 0
        for v in parts:
            n = 10 * n + v
        return n
    pattern = [0, 1, 0, -1]
    for i in range(iterations):
        data = simulate(data, pattern, i + 1)
    return process(data[:8])


def read(filename):
    parts = []
    with open(filename, 'r') as f:
        n = int(f.readline())
        while n > 0:
            parts.insert(0, n % 10)
            n //= 10
    return parts


def main(filename, iterations):
    print(solve(read(filename), iterations))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 3):
        print('missing input parameter')
        exit()
    main(sys.argv[1], int(sys.argv[2]))
