def increment(deck, v, size):
    newDeck = [0] * size
    i = 0
    while len(deck) > 0:
        newDeck[i] = deck.pop(0)
        i = (i + v) % size
    return newDeck


def loopsize(instructions, size, index):
    pos = index
    c = 0
    while c == 0 or pos != index:
        for i, v in instructions:
            if i == 'new':
                pos = size - 1 - pos
            elif i == 'cut':
                if v > 0:
                    pos = (pos - v) % size
                else:
                    pos = (pos + v) % size
            elif i == 'increment':
                pos = v * pos % size
            else:
                raise Exception('Unknown instruction')
        c += 1
    return pos


def solve(instructions, size=119315717514047, repeat=101741582076661,
          index=2020):
    return loopsize(instructions, size, index)


def read(filename):
    output = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            r = row.rstrip().split(' ')
            type = r[-2]
            val = None
            if type != 'new':
                val = int(r[-1])
            output.append((type, val))
    return output


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
