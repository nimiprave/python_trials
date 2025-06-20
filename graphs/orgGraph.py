
from graphviz import Digraph

# Load the data into a dictionary
data = {
    "CommunicationArea": ["ZNI_ROOT", "ZNI_C1", "ZNI_C1_C1", "ZNI_C1_C2", "ZNI_C2", "ZNI_C2_C1", "ZNI_C1", "ZNI_C1_C1", "ZNI_C1_C2", "ZNI_C1_C1", "ZNI_C1_C2", "ZNI_C2", "ZNI_C2_C1", "ZNI_C2_C1"],
    "AuthorizedCommunicationArea": ["ZNI_ROOT", "ZNI_ROOT", "ZNI_ROOT", "ZNI_ROOT", "ZNI_ROOT", "ZNI_ROOT", "ZNI_C1", "ZNI_C1", "ZNI_C1", "ZNI_C1_C1", "ZNI_C1_C2", "ZNI_C2", "ZNI_C2", "ZNI_C2_C1"]
}

# Create a dictionary to represent the graph
graph_data = {}
for i in range(len(data["CommunicationArea"])):
    child = data["CommunicationArea"][i]
    parent = data["AuthorizedCommunicationArea"][i]
    if parent in graph_data:
        graph_data[parent].append(child)
    else:
        graph_data[parent] = [child]

print(graph_data)


# Create a directed graph
dot = Digraph(comment='Organization Chart')

# Add nodes
for node in graph_data:
    dot.node(node)
    for child in graph_data[node]:
        dot.node(child)
        dot.edge(node, child)

# Save the graph to a file
dot.render('organization_chart', format='png', cleanup=True)
