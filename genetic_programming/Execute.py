from Helper import helper
import matplotlib.pyplot as plt

depth = 4
lengthPopulation = 1000
generations = 100

population = helper.createPopulation(lengthPopulation, depth)
#helper.printPopulation(population)
errors = helper.evaluatePopulation(population)
helper.createGraphs(population, errors)

for i in range(generations):

    chosenParents = helper.getChosenParents(population, errors, 5)
 

    population = helper.getNewPopulation(errors, population, chosenParents, depth)
    
    errors = helper.evaluatePopulation(population)

    helper.updateGraphs(i+1, population, errors)

helper.printBest(generations + 2)
plt.show()
