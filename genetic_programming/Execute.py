from Helper import helper
import matplotlib.pyplot as plt

depth = 4
lengthPopulation = 10
generations = 10

population = helper.createPopulation(lengthPopulation, depth)
#helper.printPopulation(population)
errors = helper.evaluatePopulation(population)
helper.createGraphs(population, errors)

for i in range(generations):

    chosenParents = helper.getChosenParents(population, errors)
 

    population = helper.getNewPopulation(population, chosenParents, depth)
    
    errors = helper.evaluatePopulation(population)

    helper.updateGraphs(i+1, population, errors)

'''
# 4.- Print and graph the best of all times
helper.printBest()
'''

plt.show()
