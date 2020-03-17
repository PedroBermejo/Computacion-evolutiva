from BinaryTree import Tree
from BinaryTree import Node
import math
from Helper import helper

print('-----Test generate a Tree-----')
tree = Tree()
data = [1,2,3,4,5,6,7,8,9]
tree.createFromList(data)
tree.printTree()

print('-----Test find a node-----')
node = tree.getListNodes()[7]
print('Node: ', node)
nodeFound = tree.find(node)
print('Parent node found: ', nodeFound)
nodeFound = tree.find(Node(6))
print('Parent node found: ', nodeFound)

print('----c-Test eval()-----')
x = 8
print(eval('((8)*(x))'))
print(eval('((9)*(math.sin((7)*(x))))'))
print(eval('(((8)*(x))+((0)*(x)*(1)*(x)))'))

print('-----Test number of Nodes-----')
print('Deph 1:', helper.calculateNumberOfNodes(1))
print('Deph 2:', helper.calculateNumberOfNodes(2))
print('Deph 3:', helper.calculateNumberOfNodes(3))
print('Deph 4:', helper.calculateNumberOfNodes(4))

print('-----Test real Tree depth 4-----')
population = helper.createPopulation(1, 3)
helper.printPopulation(population)
ecuation = population[0].createEcuation()
print(ecuation)
x=1
print(eval(ecuation))
x=2
print(eval(ecuation))

print('-----Test clone tree-----')
population = helper.createPopulation(1, 4)
helper.printPopulation(population)
clonePopulation = []
clonePopulation.append(population[0].cloneTree())
helper.printPopulation(clonePopulation)

print('-----Test create new population-----')
population = helper.createPopulation(2, 4)
helper.printPopulation(population)
chosen = [0, 1]
newPopulation = helper.getNewPopulation(population, chosen, 4)
helper.printPopulation(newPopulation)