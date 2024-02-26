import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
import time



def show_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            queue.extend(neighbor for neighbor in graph.neighbors(current_node) if neighbor not in visited)

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    print(start_node)
    visited.add(start_node)

    for neighbor in graph.neighbors(start_node):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def generate_random_graph(num_nodes):

    G = nx.Graph()

    # Add nodes using a loop
    for i in range(num_nodes):
        G.add_node(i)

    # Create edges to add randomness while ensuring each node has at least one connection
    for i in range(num_nodes):
        # Choose a random node to connect to (excluding itself)
        target_node = random.choice([node for node in G.nodes() if node != i])
        G.add_edge(i, target_node)

    return G

my_graph1 = generate_random_graph(100);
my_graph2 = generate_random_graph(200);
my_graph3 = generate_random_graph(1000);

#show_graph(my_graph1)
#show_graph(my_graph2)
#show_graph(my_graph3)


#-----------BFS---------#

start_time = time.time()
bfs(my_graph3, 1) # Pasirinkti grafą
end_time = time.time()


# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"BFS execution time: {elapsed_time} seconds")

#-----------DFS-----------#

start_time = time.time()
dfs(my_graph3, 1) # Pasirinkti grafą
end_time = time.time()


elapsed_time = end_time - start_time
print(f"DFS execution time: {elapsed_time} seconds")





