import networkx as nx
import matplotlib.pyplot as plt
import random

import networkx as nx
import matplotlib.pyplot as plt
import random


def show_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

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
my_graph3 = generate_random_graph(300);


show_graph(my_graph1)
show_graph(my_graph2)
show_graph(my_graph3)


