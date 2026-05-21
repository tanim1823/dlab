graph = {
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',9)],
    'E':[('D',6)],
    'D':[('G',1)],
    'C':[],
    'G':[]
}

h = {'A':11,'B':6,'C':99,'D':1,'E':7,'G':0}

open = ['A']
g = {'A':0}
parent = {'A':None}

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