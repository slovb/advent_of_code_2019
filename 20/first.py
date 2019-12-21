class Node:
    def __init__(self, p):
        self.adjacent = []
        self.p = p

    def join(self, node):
        self.adjacent.append(node)
        node.adjacent.append(self)

    def __str__(self):
        return str(self.p)


def solve(start, end):
    queue = [(0, start)]
    memory = {start: 0}
    best = None
    while len(queue) > 0:
        s, n = queue.pop()
        if best is not None and s >= best:
            continue
        for a in n.adjacent:
            if a == end:
                if best is None or best > s + 1:
                    best = s + 1
            elif a not in memory or memory[a] > s + 1:
                queue.append((s + 1, a))
                memory[a] = s + 1
    return best


def read(filename):
    portalMarkings = {}
    nodes = {}
    with open(filename, 'r') as f:
        data = [row.rstrip() for row in f.readlines()]
        for y, row in enumerate(data):
            for x, c in enumerate(row):
                p = (x, y)
                if c == '.':
                    nodes[p] = Node(p)
                    if (x - 1, y) in nodes:
                        nodes[p].join(nodes[(x - 1, y)])
                    if (x, y - 1) in nodes:
                        nodes[p].join(nodes[(x, y - 1)])
                elif c.isupper():
                    portalMarkings[p] = c
    state = {
        'nodes': nodes,
        #  'portals': {},
        'processedPortals': {},
    }

    # figure out the portals
    def process(state, pm, p1, p2, flip):
        global start, end, portals, processedPortals
        if p1 in portalMarkings and p2 in nodes:
            name = pm + portalMarkings[p1]
            if flip:
                name = portalMarkings[p1] + pm
            if name == 'AA':
                state['start'] = p2
            elif name == 'ZZ':
                state['end'] = p2
            else:
                if name in state['processedPortals']:
                    p3 = state['processedPortals'][name]
                    #  state['portals'][p2] = p3
                    #  state['portals'][p3] = p2
                    state['nodes'][p2].join(state['nodes'][p3])
                else:
                    state['processedPortals'][name] = p2
    for x, y in portalMarkings:
        pm = portalMarkings[(x, y)]
        process(state, pm, (x - 1, y), (x - 2, y), True)
        process(state, pm, (x + 1, y), (x + 2, y), False)
        process(state, pm, (x, y - 1), (x, y - 2), True)
        process(state, pm, (x, y + 1), (x, y + 2), False)
    return nodes[state['start']], nodes[state['end']]


def main(filename):
    start, end = read(filename)
    print(solve(start, end))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
