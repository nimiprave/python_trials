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

# assessing the nodes and their features
for node in graph.nodes(data=True):
    print(node)
    # print(f"Node is {node} and its attributes are {graph.nodes[node]}")

# printing edges
for edge in graph.edges(data=True):
    print(edge)
    # print(f"The Edge is {edge} and their weights are {graph.edges[edge]}")

# print the number of nodes
print(f"#Nodes : {graph.number_of_nodes()}")
print(f"#Edges : {graph.number_of_edges()}")

# calculating the degrees of the node
for node in graph.nodes:
    print(f"Degree({node}) =  {graph.degree(node)}")

# Calculators the neighbors of the node.
for node in graph.nodes:
    neighbor_list = [n for n in graph.neighbors(node)]
    print(f"Neighbors({node}) =  {neighbor_list}")


# displaying the graph
nx.draw(graph, pos=pos, with_labels=True, node_color="red", node_size=3000,
        font_color="black", font_size=8, font_family="Times New Roman", width=3)
plt.show()
