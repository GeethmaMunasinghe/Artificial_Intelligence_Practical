from queue import PriorityQueue

v = 14
graph = [[] for _ in range(v)]  # Create an adjacency list with empty lists

def addedge(x, y, cost):
    """Adds an undirected edge with a given cost between nodes x and y."""
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def best_first_search(actual_Src, target, n):
    """Performs Best-First Search from actual_Src to target."""
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))  # (priority, node)
    visited[actual_Src] = True

    print("Best First Search path:")
    while not pq.empty():
        cost, u = pq.get()
        print(u, end=" ")  # Print the current node

        if u == target:
            break

        for v, c in graph[u]:  # Iterate through neighbors
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))  # Use cost as priority

# Define Graph
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

# Run Best-First Search
source = 0  # Fixed typo (sorce → source)
target = 9
best_first_search(source, target, v)
