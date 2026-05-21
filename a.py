import heapq

graph = {
    'S': [('A', 4), ('B', 3)],
    'A': [('C', 2), ('D', 6)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 2)],
    'E': [('F', 7)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'S': 12, 'A': 8, 'B': 6,
    'C': 5,  'D': 3, 'E': 9,
    'F': 2,  'G': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)

        print(f"Node: {current}  g={g}  h={heuristic[current]}  f={f}")

        if current == goal:
            print("\nPath:", ' -> '.join(path))
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

astar('S', 'G')