from intcode import Program


def display(data):
    return ''.join([str(chr(d)) for d in data])


def encode(instructions):
    output = []
    for instruction in instructions:
        for r in instruction:
            output.append(ord(r))
        output.append(ord("\n"))
    return output


def solve(memory):
    solution = None
    instructions = [
        "NOT A J",
        "NOT B T",
        "OR T J",
        "NOT C T",
        "OR T J",
        "AND D J",
        "NOT E T",
        "NOT T T",
        "OR H T",
        "AND T J",
        "RUN",
    ]
    program = Program(memory, [])
    program.run()
    print(display(program.output))
    for i in encode(instructions):
        program.append(i)
    program.run()
    if program.output[-1] > 255:
        solution = program.output.pop()
    print(display(program.output))
    print('Runtime: {}'.format(program.runtime))
    return solution


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
