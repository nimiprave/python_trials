import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


def create_graph():
    # # Set the seed for reproducibility
    # seed = 0
    # random.seed(seed)
    # np.random.seed(seed)

    # # Create a directed graph
    # graph = nx.DiGraph()

    # # Add nodes and edges to the graph
    # node_list = ["A", "B", "C", "D"]
    # graph.add_nodes_from(node_list)

    # # add edges to the list with its attributes
    # edge_list = [('A', 'B', {"weight": 3}), ('A', 'C', {"weight": 3}), ('A', 'D', {"weight": 3}),
    #              ('B', 'C', {"weight": 2}), ('B', 'D', {"weight": 2}), ('C', 'D', {"weight": 1})]
    # graph.add_edges_from(edge_list)

    # graph.graph["Name"] = "Nirmal graph"
    # graph.graph["seed"] = seed
    # return graph

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
    unDirectedGraph.graph["Name"] = "PurchaseOrder"
    unDirectedGraph.graph["Description"] = "Purchase Order Graph"
    unDirectedGraph.graph["Version"] = "1.0"
    unDirectedGraph.graph["Author"] = "Nirmal Praveen Pothuraj"
    unDirectedGraph.graph["seed"] = seed
    return unDirectedGraph


def onclick_callback():
    st.write("Button clicked!")
    graph = create_graph()
    # pos = {
    #     "A": (1, 5),
    #     "B": (4.5, 6.6),
    #     "C": (3.6, 1.4),
    #     "D": (5.8, 3.5),
    # }
    plt.figure(figsize=(10, 6))
    nx.draw(graph, with_labels=True, node_color="red", node_size=3000,
            font_color="black", font_size=8, font_family="Times New Roman", edge_color="black", width=2)
    plt.margins(0.2)
    plt.title("Graph Visualization")
    st.pyplot(plt, use_container_width=False)


if __name__ == "__main__":
    st.multiselect("Select the nodes", ["A", "B", "C", "D"])
    # st.button("Submit", on_click=onclick_callback,
    #           args=None, kwargs=None, disabled=False,)
    if st.button("Submit"):
        with st.expander("Graph Visualization", expanded=True):  # Simulates a popup
            onclick_callback()
