from Helper import Helper

helper = Helper()

startP = (0, 0)
endP = (14, 14)

matrix_1 = helper.createEmptyMatrix(startP, endP)
matrix_1[1][2] = 1
matrix_1[3][4] = 2
matrix_1[5][5] = 3
matrix_1[5][9] = 4
#Equal point
matrix_1[13][14] = 5
matrix_1[8][9] = 6
matrix_1[9][10] = 7
matrix_1[9][15] = 8

matrix_2 = helper.createEmptyMatrix(startP, endP)
matrix_2[10][12] = 1
matrix_2[12][13] = 2
matrix_2[13][12] = 3
#Equal point
matrix_2[13][14] = 4
matrix_2[15][14] = 5
matrix_2[15][15] = 6

population = []
population.append((matrix_1, 8))
population.append((matrix_2, 6))

newPopulation = helper.generateNewPopulation(population, startP, endP)

helper.printPopulation(population)
helper.printPopulation(newPopulation)
