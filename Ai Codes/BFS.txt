
from collections import defaultdict, deque

# Function to perform Breadth First Search
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['G', 'H'],
        'C': ['E','F'],
        'G': ['I'],
        'E': ['K'],
        'D':[],
        'H':[],'F':[],'I':[],'K':[]
    }

    start_node = 'S'  # Starting node for BFS
    traversal_order = bfs(graph, start_node)
    print("BFS Traversal Order:", traversal_order)