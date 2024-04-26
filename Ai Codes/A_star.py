import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, start)
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.x == goal.x and current.y == goal.y:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        closed_set.add((current.x, current.y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = current.x + dx, current.y + dy

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != -1 and (new_x, new_y) not in closed_set:
                new_cost = current.cost + grid[new_x][new_y]
                new_node = Node(new_x, new_y, new_cost, current)
                heapq.heappush(open_set, new_node)

    return None

# Example usage:
grid = [
    [1, 2, 3],
    [4, -1, 6],
    [7, 8, 9]
]

start = Node(0, 0, grid[0][0])
goal = Node(2, 2, 0)

path = astar(start, goal, grid)
if path:
    print("Optimal path found:", path)
else:
    print("No path found.")
