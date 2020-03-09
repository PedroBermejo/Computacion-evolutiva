from helper import helper
from constants import travelParms
import matplotlib.pyplot as plt

# ----- START OF EXECUTUION

# 1.- Create random population 100 chromosomes with 30 genes each
population = helper.createPopulation(list(range( 1, 31)), travelParms.population)
distances = helper.calculateDistancesInPopulation(population)

#print("-------INITIAL STATE------")
#helper.printPopulation(population, distances)

# 1.a- Call graphs and graph the best 
# First generation
helper.createGraphs(population, distances)

for i in range(travelParms.iterations):
    
    # 2.- Compete, get chosen parents
    chosenParents = helper.getChosenParents(population, distances)

    # 3.- Reproduction, replace population with children
    population = helper.getNewPopulation(population, chosenParents)
    distances = helper.calculateDistancesInPopulation(population)

    # 3.a- Get the best and graph
    helper.updateGraphs(i+1, population, distances)

# 4.- Print and graph the best of all times
helper.printBest()

plt.show()

#print("-------FINAL STATE------")
#helper.printPopulation(population, distances)




