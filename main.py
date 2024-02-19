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
start_time = time.time()

start_vertex = 0
goal_vertex = 100
result_path = my_complex_graph.ucs(start_vertex, goal_vertex)

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000  # Convert seconds to milliseconds

if result_path:
    print(f"\nLowest-cost path from {start_vertex} to {goal_vertex}: {result_path}")
    print(f"Elapsed time: {elapsed_time_ms:.4f} milliseconds")
else:
    print(f"\nNo path found from {start_vertex} to {goal_vertex}")
