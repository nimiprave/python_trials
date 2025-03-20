# implementing the datastructure using the library-- bigtree.
from bigtree import Node

root = Node("a", age=90)
b = Node("b", age=65, parent=root)
c = Node("d", age=65, parent=root)
d = Node("d", age=65, parent=b)

root.show(attr_list=['age'])
root.hshow()
