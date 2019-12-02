def run(memory):
    ip = 0

    def lhs():
        return memory[memory[ip + 1]]

    def rhs():
        return memory[memory[ip + 2]]
    while True:
        op = memory[ip]
        if op == 99:
            break
        elif op == 1:
            memory[memory[ip + 3]] = lhs() + rhs()
        elif op == 2:
            memory[memory[ip + 3]] = lhs() * rhs()
        else:
            raise Exception("Unknown opcode")
        ip += 4
    return memory[0]


def solve(data, target):
    noun = 0
    verb = 0
    while verb < 100:
        memory = data.copy()
        memory[1] = noun
        memory[2] = verb
        try:
            val = run(memory)
            if val == target:
                return [noun, verb, 100*noun + verb]
            print(val, noun, verb)
        except Exception:
            pass
        verb += noun // 99
        noun = (noun + 1) % 100
    exit("Ran too far")


def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(',')]


def main(filename, target):
    return solve(read(filename), target)


if __name__ == "__main__":
    import sys
    target = 19690720
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f, target))
