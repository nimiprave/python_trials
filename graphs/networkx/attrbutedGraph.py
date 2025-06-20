import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

seed = 0
random.seed(seed)
np.random.seed(seed)


# creating a list of nodes:
node_list = [("A_PurchaseOrderType", {"NavigationProperty": ["to_PurchaseOrderItem", " to_PurchaseOrderNote"]}),
             ("A_PurchaseOrderItemType", {"NavigationProperty": ["A_PurOrdAccountAssignmentType", "A_PurchaseOrderItemNoteType",
                                                                 "A_PurOrdPricingElementType", "A_PurchaseOrderScheduleLineType"]}),
             ("A_PurchaseOrderNoteType"),
             ("A_PurchaseOrderScheduleLineType"),
             ("A_PurOrdAccountAssignmentType"),
             ("A_PurchaseOrderItemNoteType"),
             ("A_PurOrdPricingElementType"),
             ("A_PurchaseOrderScheduleLineType", {
              "NavigationProperty": ["A_POSubcontractingComponentType"]}),
             ("A_POSubcontractingComponentType")]

# undirected graph
unDirectedGraph = nx.DiGraph()

# attributes to graph
unDirectedGraph.graph["Name"] = "PurchaseOrder"
unDirectedGraph.graph["Description"] = "Purchase Order Graph"
unDirectedGraph.graph["Version"] = "1.0"
unDirectedGraph.graph["Author"] = "Nirmal Praveen Pothuraj"

# adding nodes from list
unDirectedGraph.add_nodes_from(node_list)

# simple way of creating edges
list_of_edges = [("A_PurchaseOrderType", "A_PurchaseOrderItemType"),
                 ("A_PurchaseOrderType", "A_PurchaseOrderNoteType"),
                 ("A_PurchaseOrderItemType", "A_PurOrdAccountAssignmentType"),
                 ("A_PurchaseOrderItemType", "A_PurchaseOrderItemNoteType"),
                 ("A_PurchaseOrderItemType", "A_PurOrdPricingElementType"),
                 ("A_PurchaseOrderItemType", "A_PurchaseOrderScheduleLineType"),
                 ("A_PurchaseOrderScheduleLineType", "A_POSubcontractingComponentType")]

# position of nodes in the graph
pos = nx.spring_layout(unDirectedGraph, seed=seed)
# adding position to nodes


# adding edges from list
unDirectedGraph.add_edges_from(list_of_edges)

nx.draw(unDirectedGraph, with_labels=True, node_color="red", node_size=7000,
        font_color="black", font_size=8, font_family="Times New Roman", width=2)

# show the graph. use the matplotlib library
plt.margins(0.2)
plt.show()
