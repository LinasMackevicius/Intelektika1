import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque


def show_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()


def bfs(graph, start_node, target_node):
    queue = deque([start_node])
    visited = set()

    if start_node == target_node:
        return [start_node]

    # Initialize 'parent' attribute for each node
    for node in graph.nodes():
        graph.nodes[node]['parent'] = None

    while queue:
        current_node = queue.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == target_node:
            path = [current_node]
            while current_node != start_node:
                current_node = graph.nodes[current_node]['parent']
                path.insert(0, current_node)
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                graph.nodes[neighbor]['parent'] = current_node  # Set the parent node

    return None


def dfs(graph, start_node, target_node):
    stack = [start_node]
    visited = set()

    if start_node == target_node:
        return [start_node]

    # Initialize 'parent' attribute for each node
    for node in graph.nodes():
        graph.nodes[node]['parent'] = None

    while stack:
        current_node = stack.pop()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == target_node:
            path = [current_node]
            while current_node != start_node:
                current_node = graph.nodes[current_node]['parent']
                path.insert(0, current_node)
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                stack.append(neighbor)
                graph.nodes[neighbor]['parent'] = current_node  # Set the parent node

    return None

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
    my_graph1 = generate_random_graph(150)
    show_graph(my_graph1)

    start_node = 0
    target_node = 13
    visited_nodes_bfs = bfs(my_graph1, start_node, target_node)

    if visited_nodes_bfs:
        print(f"Path from {start_node} to {target_node}: {visited_nodes_bfs} ({len(visited_nodes_bfs)})")
    else:
        print(f"{target_node} is not reachable from {start_node}")

    print("------\n")

    visited_nodes_dfs = dfs(my_graph1, start_node, target_node)

    if visited_nodes_dfs:
        print(f"Path from {start_node} to {target_node}: {visited_nodes_dfs} ({len(visited_nodes_dfs)})")
    else:
        print(f"{target_node} is not reachable from {start_node}")

if __name__ == "__main__":
    main()
