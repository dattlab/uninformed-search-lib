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
