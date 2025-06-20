import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

seed = 0
random.seed(seed)
np.random.seed(seed)


# undirected graph
unDirectedGraph = nx.DiGraph()

# adding nodes
unDirectedGraph.add_node("A_PurchaseOrderType")
unDirectedGraph.add_node("A_PurchaseOrderItemType")
unDirectedGraph.add_node("A_PurchaseOrderNoteType")
unDirectedGraph.add_node("A_PurchaseOrderScheduleLineType")
unDirectedGraph.add_node("A_PurOrdAccountAssignmentType")
unDirectedGraph.add_node("A_PurchaseOrderItemNoteType")
unDirectedGraph.add_node("A_PurOrdPricingElementType")
unDirectedGraph.add_node("A_PurchaseOrderScheduleLineType")
unDirectedGraph.add_node("A_POSubcontractingComponentType")


# creating edges
unDirectedGraph.add_edge("A_PurchaseOrderType", "A_PurchaseOrderItemType")
unDirectedGraph.add_edge("A_PurchaseOrderType", "A_PurchaseOrderNoteType")
unDirectedGraph.add_edge("A_PurchaseOrderItemType",
                         "A_PurOrdAccountAssignmentType")
unDirectedGraph.add_edge("A_PurchaseOrderItemType",
                         "A_PurchaseOrderItemNoteType")
unDirectedGraph.add_edge("A_PurchaseOrderItemType",
                         "A_PurOrdPricingElementType")
unDirectedGraph.add_edge("A_PurchaseOrderItemType",
                         "A_PurchaseOrderScheduleLineType")
unDirectedGraph.add_edge("A_PurchaseOrderScheduleLineType",
                         "A_POSubcontractingComponentType")


nx.draw(unDirectedGraph, with_labels=True, node_color="red", node_size=7000,
        font_color="black", font_size=8, font_family="Times New Roman", width=2)

# show the graph. use the matplotlib library
plt.margins(0.2)
plt.show()
