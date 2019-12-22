def increment(deck, v, size):
    newDeck = [0] * size
    i = 0
    while len(deck) > 0:
        newDeck[i] = deck.pop(0)
        i = (i + v) % size
    return newDeck


def solve(instructions, size=10007):
    deck = []
    for i in range(10007):
        deck.append(i)
    for i, v in instructions:
        if i == 'new':
            deck.reverse()
        elif i == 'cut':
            if v > 0:
                for _ in range(v):
                    deck.append(deck.pop(0))
            else:
                for _ in range(-v):
                    deck.insert(0, deck.pop())
        elif i == 'increment':
            deck = increment(deck, v, size)
        else:
            raise Exception('Unknown instruction')
    return deck.index(2019)


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
