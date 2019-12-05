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
        return ip + 4

    def op_mul(op):
        #  print('{} <- {} + {}'.format(param(3, 1), param(1, op[1]), param(2, op[2])))
        mem[param(3, 1)] = param(1, op[1]) * param(2, op[2])
        return ip + 4

    def op_input(op):
        #  print('{} <- {}'.format(param(1, 1), data[0]))
        mem[param(1, 1)] = data.pop(0)
        return ip + 2

    def op_output(op):
        print(mem[param(1, 1)])
        return ip + 2

    def op_jump_if_true(op):
        if param(1, op[1]) != 0:
            return param(2, op[2])
        return ip + 3

    def op_jump_if_false(op):
        if param(1, op[1]) == 0:
            return param(2, op[2])
        return ip + 3

    def op_less_than(op):
        if param(1, op[1]) < param(2, op[2]):
            mem[param(3, 1)] = 1
        else:
            mem[param(3, 1)] = 0
        return ip + 4

    def op_equals(op):
        if param(1, op[1]) == param(2, op[2]):
            mem[param(3, 1)] = 1
        else:
            mem[param(3, 1)] = 0
        return ip + 4

    while True:
        op = operation()
        #  print(mem[ip:ip+4])
        if op[0] == 99:
            break
        elif op[0] == 1:  # add
            ip = op_add(op)
        elif op[0] == 2:  # mul
            ip = op_mul(op)
        elif op[0] == 3:  # input
            ip = op_input(op)
        elif op[0] == 4:  # output
            ip = op_output(op)
        elif op[0] == 5:  # jump-if-true
            ip = op_jump_if_true(op)
        elif op[0] == 6:  # jump-if-false
            ip = op_jump_if_false(op)
        elif op[0] == 7:  # less-than
            ip = op_less_than(op)
        elif op[0] == 8:  # equals
            ip = op_equals(op)
        else:
            raise Exception("Unknown opcode")

    return mem[0]


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(',')]


def main(filename, value):
    run(read(filename), [value])


if __name__ == "__main__":
    import sys
    if (len(sys.argv) != 3):
        print('missing input parameter')
        exit()
    main(sys.argv[1], int(sys.argv[2]))
