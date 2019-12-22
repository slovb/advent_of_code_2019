import heapq


class Node:
    def __init__(self, p):
        self.adjacent = []
        self.p = p

    def join(self, node, levelMod=0):
        self.adjacent.append((node, levelMod))
        node.adjacent.append((self, -levelMod))

    def distance(self, other):
        return abs(self.p[0] - other.p[0]) + abs(self.p[1] - other.p[1])

    def __lt__(self, other):
        return self.p < other.p

    def __str__(self):
        return str(self.p)


def solve(start, end):
    def heuristic(n, lvl, step):
        return lvl * 1000 + n.distance(end) + step
    queue = []
    heapq.heappush(queue, (heuristic(start, 0, 0), 0, 0, start))
    memory = {(start, 0): 0}
    best = None
    while len(queue) > 0:
        _, level, s, n = heapq.heappop(queue)
        if best is not None and s >= best:
            continue
        newStep = s + 1
        for a, lmod in n.adjacent:
            newLevel = level + lmod
            if newLevel < 0:
                continue
            if a == end and newLevel == 0:
                if best is None or best > newStep:
                    best = newStep
                    print(best)
            elif (a, newLevel) not in memory or \
                    memory[(a, newLevel)] > newStep:
                h = heuristic(a, newLevel, newStep)
                heapq.heappush(queue, (h, newLevel, newStep, a))
                memory[(a, newLevel)] = newStep
    return best


def read(filename):
    portalMarkings = {}
    nodes = {}
    height = 0
    width = 0
    with open(filename, 'r') as f:
        data = [row.rstrip() for row in f.readlines()]
        height = len(data)
        for y, row in enumerate(data):
            width = max(width, len(row))
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

    # figure out the portals
    processedPortals = {}

    def process(pm, p1, p2, flip):
        if p1 in portalMarkings and p2 in nodes:
            name = pm + portalMarkings[p1]
            if flip:
                name = portalMarkings[p1] + pm
            if name == 'AA':
                processedPortals['start'] = p2
            elif name == 'ZZ':
                processedPortals['end'] = p2
            else:
                if name in processedPortals:
                    p3 = processedPortals[name]
                    mod = 1
                    if p2[0] <= 2 or p2[0] >= width - 2 or \
                       p2[1] <= 2 or p2[1] >= height - 2:
                        mod = -1
                    nodes[p2].join(nodes[p3], mod)
                else:
                    processedPortals[name] = p2
    for x, y in portalMarkings:
        pm = portalMarkings[(x, y)]
        process(pm, (x - 1, y), (x - 2, y), True)
        process(pm, (x + 1, y), (x + 2, y), False)
        process(pm, (x, y - 1), (x, y - 2), True)
        process(pm, (x, y + 1), (x, y + 2), False)
    return nodes[processedPortals['start']], nodes[processedPortals['end']]


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
