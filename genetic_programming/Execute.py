from Helper import helper

population = helper.createPopulation(2, 4)
helper.printPopulation(population)
errors = helper.evaluatePopulation(population)

print(errors)
