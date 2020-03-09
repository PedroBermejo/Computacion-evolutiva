from BinaryTree import Tree
from BinaryTree import Node

print('Test generate a Tree')
tree = Tree()
data = [1,2,3,4,5,6,7,8,9]
tree.createFromList(data)
tree.printTree()

print('Test the nodes')
tree.printNodes()

print('Test find a node')
node = tree.getNodes()[7]
print('Node: ', node)
nodeFound = tree.find(node)
print('Parent node found: ', nodeFound)
nodeFound = tree.find(Node(8))
print('Parent node found: ', nodeFound)