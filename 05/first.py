def run(mem, data):
    ip = 0

    def param(offset, mode):
        if mode == 0:
            return mem[mem[ip + offset]]
        return mem[ip + offset]

    def operation():
        op = mem[ip] % 10**2
        c = (mem[ip] // 10**2) % 10
        b = (mem[ip] // 10**3) % 10
        a = (mem[ip] // 10**4) % 10
        return (op, c, b, a)

    def op_add(op):
        #  print('{} <- {} + {}'.format(param(3, 1), param(1, op[1]), param(2, op[2])))
        mem[param(3, 1)] = param(1, op[1]) + param(2, op[2])

    def op_mul(op):
        #  print('{} <- {} + {}'.format(param(3, 1), param(1, op[1]), param(2, op[2])))
        mem[param(3, 1)] = param(1, op[1]) * param(2, op[2])

    def op_input(op):
        #  print('{} <- {}'.format(param(1, 1), data[0]))
        mem[param(1, 1)] = data.pop(0)

    def op_output(op):
        print(mem[param(1, 1)])

    while True:
        op = operation()
        #  print(mem[ip:ip+4])
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

    return mem[0]


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(',')]


def main(filename):
    run(read(filename), [1])


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
