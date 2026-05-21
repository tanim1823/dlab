graph = {
    'S':[('A',4),('B',3)],
    'A':[('C',2),('E',6)],
    'B':[('D',4),('E',5)],
    'C':[('F',3)],
    'D':[('F',2)],
    'E':[('F',7)],
    'F':[('G',1)],
    'G':[]
}

h = {'S':12,'A':8,'B':6,'C':5,'D':3,'E':9,'F':2,'G':0}

open = ['S']
g = {'S':0}
parent = {'S':None}

while open:

    n = min(open, key=lambda x: g[x] + h[x])

    if n == 'G':
        break

    open.remove(n)

    for m,c in graph[n]:

        new_cost = g[n] + c

        if m not in g or new_cost < g[m]:
            g[m] = new_cost
            parent[m] = n

            if m not in open:
                open.append(m)

path = []
node = 'G'

while node:
    path.append(node)
    node = parent[node]

path.reverse()

print("Path:", " -> ".join(path))
print("Cost:", g['G'])