import math


def calculate_priority(craft):
    used_for = {'FUEL': set()}
    prio = []
    for product in craft:
        composites = [material for _, material in craft[product][1]]
        while len(composites) > 0:
            material = composites.pop()
            if material in used_for:
                used_for[material].add(product)
            else:
                used_for[material] = set([product])
            if material != 'ORE':
                for _, m in craft[material][1]:
                    composites.append(m)
    while len(used_for) > 0:
        for m in used_for:
            if len(used_for[m]) == 0:
                prio.append(m)
                used_for.pop(m)
                for mm in used_for:
                    if m in used_for[mm]:
                        used_for[mm].remove(m)
                break  # unsure about removing while iterating
    return prio


def pick_requirement(requirements, priority):
    i = 0
    p = priority.index(requirements[i][1])
    for j, r in enumerate(requirements):
        m_p = priority.index(r[1])
        if m_p < p:
            i = j
            p = m_p
    return requirements.pop(i)


def build_craft_table(data):
    craft = {}
    for materials, result in data:
        craft[result[1]] = (result[0], materials)
    return craft


def solve(data):
    craft = build_craft_table(data)
    priority = calculate_priority(craft)
    oreReq = 0
    requirements = [[1, 'FUEL']]
    while len(requirements) > 0:
        print(requirements)
        r_a, r_m = pick_requirement(requirements, priority)
        p_a = craft[r_m][0]
        multiplier = math.ceil(r_a / p_a)
        for a, m in craft[r_m][1]:
            amount = a * multiplier
            if m == 'ORE':
                print('+ ' + str(amount))
                oreReq += amount
            else:
                isNew = True
                for r in requirements:
                    if r[1] == m:
                        r[0] += amount
                        isNew = False
                        break
                if isNew:
                    requirements.append([amount, m])
    return oreReq


def read(filename):
    def token(m):
        t = m.split(' ')
        return int(t[0]), t[1]

    def process(line):
        n = line.rstrip().split(' => ')
        return ([token(m) for m in n[0].split(', ')], token(n[1]))
    with open(filename, 'r') as f:
        return [process(l) for l in f.readlines()]


def main(filename):
    print(solve(read(filename)))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
