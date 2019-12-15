from intcode import Program
import random


def limits(state):
    xMin, xMax, yMin, yMax = 0, 0, 0, 0
    for x, y in state:
        xMin = min(xMin, x)
        xMax = max(xMax, x)
        yMin = min(yMin, y)
        yMax = max(yMax, y)
    return xMin, xMax, yMin, yMax


def display(state, dead, pos):
    xMin, xMax, yMin, yMax = limits(state)
    output = []
    for j in range(yMax + 1 - yMin):
        y = yMin + j
        row = []
        for i in range(xMax + 1 - xMin):
            x = xMin + i
            p = (x, y)
            if x == pos[0] and y == pos[1]:
                row.append('@')
            elif x == 0 and y == 0:
                row.append('x')
            elif p not in state:
                row.append(' ')
            elif state[p] == 0:
                row.append('#')
            elif state[p] == 1:
                if p in dead:
                    row.append('-')
                else:
                    row.append('.')
            elif state[p] == 2:
                row.append('o')
            else:
                raise Exception("This shouldn't happend right")
        output.append(''.join(row))
    output.append('\n')
    return '\n'.join(output)


def update_position(pos, direction):
    x, y = pos
    if direction == 1:
        return (x, y - 1)
    elif direction == 2:
        return (x, y + 1)
    elif direction == 3:
        return (x - 1, y)
    elif direction == 4:
        return (x + 1, y)
    else:
        raise Exception('Unknown direction')


def dead_options(pos, dead):
    count = 0
    for d in range(1, 5):
        opt_pos = update_position(pos, d)
        if opt_pos not in dead:
            count += 1
    return count < 2


def pick_direction(pos, prev, state, dead):
    options = []
    for d in range(1, 5):
        opt_pos = update_position(pos, d)
        if opt_pos not in state:
            return d
        if opt_pos not in dead:
            options.append(d)
    back_direction = -1
    if prev == 1:
        back_direction = 2
    elif prev == 2:
        back_direction = 1
    elif prev == 3:
        back_direction = 4
    elif prev == 4:
        back_direction = 3
    if len(options) == 0:
        return None
    elif len(options) > 1 and back_direction in options:
        options.remove(back_direction)
    return random.choice(options)


def solve(memory):
    program = Program(memory, [])
    state = {}
    pos = (0, 0)
    direction = 2
    oxygen_pos = None
    steps = 0
    distances = {pos: steps}
    dead = set()
    while not program.halted:
        new_pos = update_position(pos, direction)
        program.append(direction)
        program.run()
        if program.awaiting_input:
            status = program.pop()
            if status == 0:
                state[new_pos] = 0
                # don't update pos
                dead.add(new_pos)
            elif status == 1 or status == 2:
                state[new_pos] = 1
                pos = new_pos
                if dead_options(pos, dead):
                    dead.add(pos)
                steps += 1
                if pos in distances:
                    if distances[pos] < steps:
                        steps = distances[pos]
                    else:
                        distances[pos] = steps
                else:
                    distances[pos] = steps
                if status == 2:
                    oxygen_pos = pos
            else:
                raise Exception('Bad status')
            direction = pick_direction(pos, direction, state, dead)
            if direction is None:
                break
            if oxygen_pos is not None:
                print(distances[oxygen_pos])
        print(display(state, dead, pos))
    return distances[oxygen_pos]


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
