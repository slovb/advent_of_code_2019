def run(memory, data):
    ip = 0

    def param(offset, mode):
        if mode == 0:
            return memory[memory[ip + offset]]
        return memory[ip + offset]

    def operation():
        op = memory[ip] % 10**2
        c = (memory[ip] // 10**2) % 10
        b = (memory[ip] // 10**3) % 10
        a = (memory[ip] // 10**4) % 10
        return (op, a, b, c)

    def op_add(op):
        memory[param(3, 1)] = param(1, op[1]) + param(2, op[2])

    def op_mul(op):
        memory[param(3, 1)] = param(1, op[1]) * param(2, op[2])

    def op_input(op):
        memory[param(1, 1)] = data.pop(0)

    def op_output(op):
        print(memory[param(1, 1)])

    while True:
        op = operation()
        if op[0] == 99:
            break
        elif op[0] == 1:  # add
            op_add(op)
            ip += 4
        elif op[0] == 2:  # mul
            op_mul(op)
            ip += 4
        elif op[0] == 3:  # input
            op_input(op)
            ip += 2
        elif op[0] == 4:  # output
            op_output(op)
            ip += 2
        else:
            raise Exception("Unknown opcode")

    return memory[0]


def solve(memory, data):
    run(memory, data)
    return memory


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(',')]


def main(filename):
    return solve(read(filename), [1])


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))
