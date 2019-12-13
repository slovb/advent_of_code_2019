from intcode import Program


def limits(state):
    xMin, xMax, yMin, yMax = 0, 0, 0, 0
    for x, y in state:
        xMin = min(xMin, x)
        xMax = max(xMax, x)
        yMin = min(yMin, y)
        yMax = max(yMax, y)
    return xMin, xMax, yMin, yMax


def display(state, score):
    xMin, xMax, yMin, yMax = limits(state)
    output = []
    paddle = (0, 0)
    ball = (0, 0)
    for j in range(yMin, yMax + 1):
        y = yMin + j
        row = []
        for i in range(xMin, xMax + 1):
            x = xMin + i
            p = (x, y)
            if p not in state:
                row.append(' ')
            elif state[p] == 0:
                row.append(' ')
            elif state[p] == 1:
                row.append('#')
            elif state[p] == 2:
                row.append('x')
            elif state[p] == 3:
                row.append('-')
                paddle = p
            elif state[p] == 4:
                row.append('o')
                ball = p
            else:
                raise Exception("This shouldn't happend right")
        output.append(''.join(row))
    output.append(str(score))
    output.append('\n')
    return '\n'.join(output), paddle, ball


def solve(memory):
    memory[0] = 2
    program = Program(memory, [])
    state = {}
    score = 0
    while not program.halted:
        program.run()
        while len(program.output) > 0:
            x, y, id = program.pop(), program.pop(), program.pop()
            if x == -1 and y == 0:
                score = id
            else:
                state[(x, y)] = id
        if program.awaiting_input:
            current, paddle, ball = display(state, score)
            print(current)
            if paddle[0] > ball[0]:
                program.input.append(-1)
            elif paddle[0] == ball[0]:
                program.input.append(0)
            elif paddle[0] < ball[0]:
                program.input.append(1)
    return score


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
