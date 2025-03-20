import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()   # undirected graph
dG = nx.DiGraph()  # Directed graph

G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9)

nx.draw_spring(G, with_labels=True)
plt.show()
