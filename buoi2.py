from collections import deque

def BFS(N, A, n0, DICH):
    fringe = deque([n0])
    closed = set()
    while fringe:
        n = fringe.popleft()
        closed.add(n)
        if n in DICH:
            return f"SOLUTION({n})"
        neighbors = A.get(n, [])
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in closed and neighbor not in fringe:
                    fringe.append(neighbor)
    return "No solution"

import heapq

def UCS(N, A, n0, DICH):
    fringe = []
    heapq.heappush(fringe, (0, n0))    
    closed = set()
    while fringe:
        cost, n = heapq.heappop(fringe)

        if n in closed:
            continue
        closed.add(n)

        if n in DICH:
            return f"SOLUTION({n}), COST({cost})"
        neighbors = A.get(n, [])
        for neighbor, neighbor_cost in neighbors:
            if neighbor not in closed:
                heapq.heappush(fringe, (cost + neighbor_cost, neighbor))
    return "No solution"

def DFS(N, A, n0, DICH):
    fringe = [(n0, 0)] 
    closed = set()
    while fringe:
        n, cost = fringe.pop()

        if n in closed:
            continue
        closed.add(n)

        if n in DICH:
            return f"SOLUTION({n}), COST({cost})"
        neighbors = A.get(n, [])
        for neighbor, neighbor_cost in neighbors:
            if neighbor not in closed:
                fringe.append((neighbor, cost + neighbor_cost))
    return "No solution"

N = 6
A = {
    1: [(2, 1), (3, 4)],
    2: [(4, 2), (5, 5)],
    3: [(6, 1)],
    4: [],
    5: [],
    6: []
}
n0 = 1
DICH = {6}

result = DFS(N, A, n0, DICH)
print(result)