import matplotlib.pyplot as plt
import random
import operator
import numpy as np

class helper:
    # Print population for testing
    def printPopulation(population):
        for i in range(len(population)):
            print(i, population[i])

    # Print population for testing
    def printPopulation_result(population, result):
        for i in range(len(population)):
            print(i, population[i], result[i])

    # creates population base on list (chormosoma) 
    # and given length
    def createPopulation(minR, maxR, chromLength, popuLength):
        population = []
        for i in range(popuLength):
            chrom = []
            for j in range(chromLength):
                chrom.append(random.randint(minR, maxR))
            population.append(chrom)
        return population

    def evaluateEcuation(chrom, divisor, x):
        exp = len(chrom) - 1
        y = 0
        for i in chrom:
            y += (i/divisor)*(x**exp)
            exp -= 1
        return y

    # formula Ax^2 + Bx + C = y, x and y are constants
    # A, B and C are in chrom, they will be divided as well
    # if chrom is higher in legth secuence is followed
    def calculateResults(population, divisor, x, y):
        results = []
        for chrom in population:
            y_1 = helper.evaluateEcuation(chrom, divisor, x)
            results.append(abs(y - y_1))
        return results

    # Gets 5 random numbers (0 - 99) and chooses the
    # best (lower) result
    def getBestInTournament(distances, length, percent):
        selection =  []
        while len(selection) < percent:
            value = random.randint(0, length)
            if value not in selection:
                selection.append((value, distances[value]))
        return min(selection, key=operator.itemgetter(1))

    def getChosenParents(population, results, percent, parentNum):
        chosenParents = []
        while len(chosenParents) < len(population)*parentNum:
            winer = helper.getBestInTournament(results, 
                len(population) -1, percent)
            if ((len(chosenParents) == 0) or (chosenParents[-1] != winer[0])):
                chosenParents.append(winer[0])
        return chosenParents

    def intToBitArray(number, bits):
        mask = []
        for i in range(bits):
            mask.append(0)
        arrayBits = [int(i) for i in list('{0:0b}'.format(number))]
        position = bits - len(arrayBits)
        return mask[0:position] + arrayBits
    
    def bitArrayToInt(bitArray):
        return int("".join(str(x) for x in bitArray), 2)

    def flipBits(parent_1, parent_2, position, bits):
        child = []
        mod = position % bits
        if ( mod == 0):
            pos = int(position / bits)
            child = parent_1[0:pos] + parent_2[pos:]
        else:
            pos = int(position / bits)
            bit_1 = helper.intToBitArray(parent_1[pos], bits)
            bit_2 = helper.intToBitArray(parent_2[pos], bits)
            newBitArray = bit_1[0:mod] + bit_2[mod:]
            newNumber = helper.bitArrayToInt(newBitArray)
            child = parent_1[0:pos] + [newNumber] + parent_2[pos+1:]
            #print("parent_1", parent_1)
            #print("parent_2", parent_2)
            #print("bit_1", position, bit_1, mod)
            #print("bit_2", position, bit_2, mod)
            #print("newBitArray", newBitArray, newNumber)
        return child
 
    def bitExchangeReproduction(population, chosenParents, parentNum, bits):
        newPopulation = []
        for i in range(len(population)):
            ind = i * parentNum
            if (parentNum == 2):
                position = random.randint(0, len(population[i])*bits)
                #print("position", position)
                child = helper.flipBits(population[chosenParents[ind]].copy(), 
                    population[chosenParents[ind+1]].copy(), position, bits)
            newPopulation.append(child)
        return newPopulation

    def printEcuation(ax, chrom, axisRange, divisor):
        x = []
        y = []
        #ax[1].cla()
        ax[1].set_xlabel('X axis')
        ax[1].set_ylabel('Y axis')
        ax[1].title.set_text("Ecuations")
        for i in np.arange(0.0, float(axisRange), 0.1):
            x.append(i)
            y.append(helper.evaluateEcuation(chrom, divisor, i))
        ax[1].plot(x,y)
        plt.pause(0.1)

    def upGraphs(i, population, results, ecuaParms):
        # Update history graph
        minIndx = results.index(min(results))
        #global best
        #if(results[minIndx] < best[2]):
        #    best = (i, population[minIndx], results[minIndx])
        print(i, results[minIndx])
        ax[0].scatter(i, results[minIndx])
        # Replace coordenates graph
        x = []
        y = []
        axisRange = ecuaParms.maxR/ecuaParms.divisor
        helper.printEcuation(ax, population[minIndx], axisRange, 
            ecuaParms.divisor)
        
    def createGraph(x, results):
        fig, ax = plt.subplots(1, 1, figsize=(12,5))
        ax.set_xlabel('X generations')
        ax.set_ylabel('Y grades')
        ax.axis([0, 100, 0, 100])
        ax.scatter(x, results)
        plt.show()

'''   
    def printBest():
        print(best)
        ax[0].scatter(travelParms.population + 5, best[2])
        x = []
        y = []
        for i in best[1]:
            x.append(cities.data[i].x)
            y.append(cities.data[i].y)
        ax[1].cla()
        ax[1].set_xlabel('X axis')
        ax[1].set_ylabel('Y axis')
        ax[1].title.set_text("Cities")
        ax[1].plot(x, y, '-r')
        plt.pause(0.1)

'''    

    



        
