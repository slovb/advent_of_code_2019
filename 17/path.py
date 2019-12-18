from intcode import Program


def display(data):
    return ''.join([str(chr(d)) for d in data])


def parse(data):
    scaffold = {}
    x = 0
    y = 0
    state = ()
    for d in data:
        if d == ord('.'):
            x += 1
        elif d == ord("\n"):
            x = 0
            y += 1
        else:
            if d == ord('^'):
                state = (x, y, 0)
            elif d == ord('>'):
                state = (x, y, 1)
            elif d == ord('v'):
                state = (x, y, 2)
            elif d == ord('<'):
                state = (x, y, 3)
            scaffold[(x, y)] = d
            x += 1
    return scaffold, state


def forward(state):
    x, y, d = state
    if d == 0:
        return (x, y - 1, d)
    elif d == 1:
        return (x + 1, y, d)
    elif d == 2:
        return (x, y + 1, d)
    elif d == 3:
        return (x - 1, y, d)
    raise Exception('Unknown direction')


def forward_position(state):
    f = forward(state)
    return (f[0], f[1])


def where_turn(scaffold, state):
    x, y, d = state
    left = (x, y, (d - 1) % 4)
    right = (x, y, (d + 1) % 4)
    if forward_position(left) in scaffold:
        return 'L', left
    if forward_position(right) in scaffold:
        return 'R', right
    return 'x', state


def solve(memory):
    program = Program(memory, [])
    program.run()
    data = program.dump()
    print(display(data))
    scaffold, state = parse(data)
    path = []
    count = 0
    turn, state = where_turn(scaffold, state)
    while turn != 'x':
        path.append(turn)
        count = 0
        while forward_position(state) in scaffold:
            state = forward(state)
            count += 1
        path.append(str(count))
        turn, state = where_turn(scaffold, state)
    return ','.join(path)


def read(filename):
    memory = {}
    with open(filename, 'r') as f:
        for k, n in enumerate(f.readline().split(',')):
            memory[k] = int(n)
    return memory


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
