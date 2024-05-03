import heapq

class Node:
    def __init__(self, state, cost, total_cost):
        self.state = state
        self.cost = cost
        self.total_cost = total_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def ucs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, Node(start, 0, 0))
    explored = set()

    while frontier:
        curr_Node = heapq.heappop(frontier)
        curr_State, curr_Cost, curr_TCost = curr_Node.state, curr_Node.cost, curr_Node.total_cost

        print("Current state:", curr_State)
        print("Current cost:", curr_Cost)
        print("Current total cost:", curr_TCost)

        if curr_State == goal:
            print("Goal reached! Path found:", curr_State, "Total cost:", curr_TCost)
            return curr_State, curr_TCost  # Goal reached

        explored.add(curr_State)

        for neighbor, cost in graph[curr_State].items():
            if neighbor not in explored:
                total_cost = curr_TCost + cost
                heapq.heappush(frontier, Node(neighbor, cost, total_cost))

    print("Goal not reachable.")
    return None, None

graph = {
    'S': {'A': 3, 'B': 2, 'C': 6},
    'A': {'S': 3, 'B': 1, 'D': 1},
    'B': {'S': 2, 'A': 1, 'D': 4, 'E': 2},
    'C': {'S': 6, 'E': 5},
    'D': {'A': 1, 'B': 4, 'E': 1, 'F': 5},
    'E': {'B': 2, 'C': 5, 'D': 1, 'F': 3},
    'F': {'D': 5, 'E': 3}
}

start_node = 'S'
goal_node = 'F'

result_node, total_cost = ucs(graph, start_node, goal_node)
if result_node:
    print("Goal reached! Path found:", result_node, "Total cost:", total_cost)
else:
    print("Goal not reachable.")
