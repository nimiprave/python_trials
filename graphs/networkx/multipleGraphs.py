import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

seed = 0
random.seed(seed)
np.random.seed(seed)

# creating a list of nodes:

node_list = ["A_PurchaseOrderType", "A_PurchaseOrderItemType", "A_PurchaseOrderNoteType",
             "A_PurchaseOrderScheduleLineType", "A_PurOrdAccountAssignmentType",
             "A_PurchaseOrderItemNoteType", "A_PurOrdPricingElementType",
             "A_PurchaseOrderScheduleLineType", "A_POSubcontractingComponentType"]

# undirected graph
unDirectedGraph = nx.DiGraph()
# unDirectedGraph1 = nx.DiGraph()

# adding node to the second graph
# unDirectedGraph1.add_nodes_from(['a', 'b', 'c'])
# unDirectedGraph1.add_edges_from([('a', 'b'), ('a', 'c')])

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

# adding edges from list
unDirectedGraph.add_edges_from(list_of_edges)

nx.draw(unDirectedGraph, with_labels=True, node_color="green", node_size=7000,
        font_color="black", font_size=8, font_family="Times New Roman", width=2)

# nx.draw(unDirectedGraph1, with_labels=True, node_color="green", node_size=7000,
#         font_color="black", font_size=8, font_family="Times New Roman", width=2)

# show the graph. use the matplotlib library
plt.margins(0.2)
plt.show()
