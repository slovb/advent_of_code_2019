from intcode import Program


def display(data):
    return ''.join([str(chr(d)) for d in data])


def encode(instructions):
    output = []
    for instruction in instructions:
        for r in instruction:
            output.append(ord(r))
        output.append("\n")
    return output


def solve(memory):
    memory[0] = 2
    instruction = encode([
        'A,B,C,A,C,A,C',
        'L,6,R,12,L,4,L,6,R,6',
        'L,6,R,12,R,6',
        'L,6,R,12,L,6,L,10,L,10,R,6',
        'n'
    ])
    program = Program(memory, instruction)
    program.run()
    data = program.dump()
    print(display(data[:-2]))
    return data[-1]


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
