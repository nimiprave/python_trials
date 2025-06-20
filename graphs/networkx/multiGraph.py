
import networkx as nx
import matplotlib.pyplot as plt

# Create a multigraph
G = nx.MultiGraph()

# Add edges with different keys
G.add_edge('A', 'B', key='edge1', weight=1)
G.add_edge('A', 'B', key='edge2', weight=2)
G.add_edge('B', 'C', key='edge3', weight=3)
G.add_edge('C', 'A', key='edge4', weight=4)

# Print the edges
print("Edges:")
for u, v, key, data in G.edges(keys=True, data=True):
    print(f"{u} -- {v} (key: {key}, weight: {data['weight']})")

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
print(edge_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
