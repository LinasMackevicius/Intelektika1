import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
import time

def show_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()


def bfs(graph, start_node, target_node):
    visited = set()
    queue = deque([(start_node, [start_node])])  # Tuple (node, path)

    while queue:
        current_node, path = queue.popleft()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            if current_node == target_node:
                return path  # Return the path taken

            # Extend the path with the current node
            path = path + [neighbor for neighbor in graph.neighbors(current_node) if neighbor not in visited]

            queue.extend((neighbor, path) for neighbor in graph.neighbors(current_node) if neighbor not in visited)

    return []  # If target_node is not found, return an empty list


def dfs(graph, start_node, target_node, visited=None, steps=0):
    if visited is None:
        visited = set()

    print(start_node)
    visited.add(start_node)
    if start_node == target_node:
        return steps  # Return the steps taken

    for neighbor in graph.neighbors(start_node):
        if neighbor not in visited:
            result = dfs(graph, neighbor, target_node, visited, steps + 1)
            if result != -1:
                return result
    return -1  # If target_node is not found


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

def main():

    my_graph1 = generate_random_graph(100);
    my_graph2 = generate_random_graph(200);
    my_graph3 = generate_random_graph(1000);

    show_graph(my_graph1)
    #show_graph(my_graph2)
    #show_graph(my_graph3)


    #-----------BFS---------#

    visited_nodes = bfs(my_graph1, 0, 13);
    print(f"Number of nodes traversed: {len(visited_nodes)}")

    #-----------DFS-----------#

    #start_time = time.time()
    #dfs(my_graph3, 1) # Pasirinkti grafą
    #end_time = time.time()
    #
    #
    #elapsed_time = end_time - start_time
    #print(f"DFS execution time: {elapsed_time} seconds")





