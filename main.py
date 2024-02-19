import heapq
from collections import defaultdict
import time

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Uncomment this line if the graph is directed

    def ucs(self, start, goal):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)

            if current_node not in visited:
                visited.add(current_node)
                path = path + [current_node]

                if current_node == goal:
                    return path

                for neighbor, edge_cost in self.graph[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))

        return None  # No path found

    def dls(self, start, goal, depth, current_depth=0, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path = path + [start]

        if start == goal:
            return path

        if current_depth < depth:
            for neighbor, _ in self.graph[start]:
                if neighbor not in visited:
                    result = self.dls(neighbor, goal, depth, current_depth + 1, visited.copy(), path.copy())
                    if result:
                        return result

        return None  # No path found within the specified depth

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"Vertex {vertex}: {neighbors}")

# Part 1: Create a more complex graph with 20 vertices and add edges with weights
my_complex_graph = Graph()

# Create edges with random weights for demonstration purposes
for i in range(100):
    my_complex_graph.add_edge(i, i+1, i+2)

# Print the graph
print("Graph Structure:")
my_complex_graph.print_graph()

# Part 2: Apply UCS algorithm from vertex 0 to 100
start_vertex = 0
goal_vertex = 100

start_time_ucs = time.time()
result_path_ucs = my_complex_graph.ucs(start_vertex, goal_vertex)
end_time_ucs = time.time()

elapsed_time_ms_ucs = (end_time_ucs - start_time_ucs) * 1000  # Convert seconds to milliseconds

if result_path_ucs:
    print(f"\nLowest-cost path from {start_vertex} to {goal_vertex} using UCS: {result_path_ucs}")
    print(f"Elapsed time (UCS): {elapsed_time_ms_ucs:.4f} milliseconds")
else:
    print(f"\nNo path found from {start_vertex} to {goal_vertex} using UCS")

# Part 3: Apply DLS algorithm from vertex 0 to 100 with a depth limit
depth_limit = 100

start_time_dls = time.time()
result_path_dls = my_complex_graph.dls(start_vertex, goal_vertex, depth_limit)
end_time_dls = time.time()

elapsed_time_ms_dls = (end_time_dls - start_time_dls) * 1000  # Convert seconds to milliseconds

if result_path_dls:
    print(f"\nPath from {start_vertex} to {goal_vertex} using DLS with depth limit {depth_limit}: {result_path_dls}")
    print(f"Elapsed time (DLS): {elapsed_time_ms_dls:.4f} milliseconds")
else:
    print(f"\nNo path found from {start_vertex} to {goal_vertex} using DLS with depth limit {depth_limit}")
