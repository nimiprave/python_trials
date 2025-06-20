import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as py
# creating the graph
graph = nx.DiGraph()

# adding feature for the graph
graph.graph["Name"] = "Nirmal graph"


# set the seed therefore the grapp show the same.
seed = 0
random.seed(seed)
py.random.seed(seed)

# add the nodes to the graph:
nodes_list = [('A', {"age": 19, "sex": 'M'}), ('B', {"age": 16, "sex": 'M'}), ('C', {
    "age": 21, "sex": 'F'}), ('D', {"age": 14, "sex": 'F'})]
graph.add_nodes_from(nodes_list)

# add edges to the list with its attributes
edge_list = [('A', 'B', {"weight": 3}), ('A', 'C', {"weight": 3}), ('A', 'D', {"weight": 3}),
             ('B', 'C', {"weight": 2}), ('B', 'D', {"weight": 2}), ('C', 'D', {"weight": 1})]
graph.add_edges_from(edge_list)

# position of the nodes:
pos = {
    "A": (1, 5),
    "B": (4.5, 6.6),
    "C": (3.6, 1.4),
    "D": (5.8, 3.5),

}

# position of the node attributes:
pos_node_attributes = {}
for node, (x, y) in pos.items():
    pos_node_attributes[node] = (x, y-0.9)


# assessing the nodes and their features
node_labels = {n: (d['age'], d['sex'])
               for n, d in graph.nodes(data=True)}


# edge labels
edge_labels = {(u, v): d["weight"] for u, v, d in graph.edges(data=True)}


# # displaying the graph
nx.draw(graph, pos=pos, with_labels=True, node_color="red", node_size=3000,
        font_color="black", font_size=8, font_family="Times New Roman", edge_color="lightgray", width=3)
nx.draw_networkx_labels(graph, pos=pos_node_attributes,
                        labels=node_labels, font_color="black")

nx.draw_networkx_edge_labels(
    graph, pos=pos, edge_labels=edge_labels, label_pos=0.5)

plt.margins(0.2)
plt.show()
