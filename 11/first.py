from intcode import Program


def solve(memory):
    program = Program(memory, [])
    memory = {}

    def get(position):
        if position not in memory:
            return 0
        return memory[position]

    def updated_position(position, direction):
        if direction == 0:
            return (position[0], position[1] - 1)
        elif direction == 1:
            return (position[0] + 1, position[1])
        elif direction == 2:
            return (position[0], position[1] + 1)
        elif direction == 3:
            return (position[0] - 1, position[1])
        else:
            raise Exception('Hej kom och hjälp mig')
    position = (0, 0)
    direction = 0  # 0 up, 1 right, 2 down, 3 left
    while not program.halted:
        program.input.append(get(position))
        program.run()
        if program.awaiting_input:
            #  paint
            memory[position] = program.output.pop(0)
            #  update direction
            if program.output.pop(0) == 0:
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            #  update position
            position = updated_position(position, direction)
    return len(memory), program.output


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
