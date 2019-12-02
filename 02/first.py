def solve(data):
    print("Input: {}".format(','.join(str(i) for i in data)))
    pos = 0
    while True:
        code = data[pos]
        if code == 99:
            break
        elif code == 1:
            data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos + 2]]
        elif code == 2:
            data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]
        else:
            raise Exception("Unknown opcode")
        pos += 4
    return data


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(',')]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("Result: {}\n".format(",".join(str(i) for i in main(f))))
