from queue import PriorityQueue

v = 14
graph = [[] for i in range(v)]  # Create an adjacency list with empty lists

def add_edge(x, y, cost):
    """Adds an undirected edge with a given cost between nodes x and y."""
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def best_first_search(actual_Src, target, n):
    """Performs Best-First Search from actual_Src to target."""
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))  # (priority, node)
    visited[actual_Src] = True

    while not pq.empty():
        cost, u = pq.get()
        print(u, end=" ")  # Print the current node

        if u == target:
            break

        for v, c in graph[u]:  # Iterate through neighbors
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))  # Use cost as priority

# Example Graph
add_edge(0, 1, 4)
add_edge(0, 2, 3)
add_edge(1, 3, 2)
add_edge(2, 3, 1)
add_edge(3, 4, 5)

# Run Best-First Search
print("Best First Search path:")
best_first_search(0, 4, v)  # Start from node 0, looking for node 4
