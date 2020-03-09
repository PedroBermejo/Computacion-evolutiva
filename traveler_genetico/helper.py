from constants import cities, travelParms
import matplotlib.pyplot as plt
import random
import operator

class helper:
    # Print population for testing
    def printPopulation(population, distances):
        for i in range(len(population)):
            print(i, population[i], distances[i])

    # creates population base on list (chormosoma) 
    # and given length
    def createPopulation(base_chrom, length):
        base = base_chrom.copy()
        population = []
        for i in range(length):
            random.shuffle(base)
            population.append(base)
        return population

    # formula sqr((y1-y2)^2 + (x1-x2)^2)
    def calculateDistance(city_1, city_2):
        coord_1 = cities.data[city_1]
        coord_2 = cities.data[city_2]
        distance = ((coord_1.y - coord_2.y)**2 + 
        (coord_1.x - coord_2.x)**2)**0.5
        return distance

    def getTotalDistance(chromosome):
        distance = 0
        for i in range(len(chromosome) -1):
            distance += \
            helper.calculateDistance(chromosome[i], chromosome[i+1])
        return distance

    def calculateDistancesInPopulation(population):
        distances = []
        for i in range(len(population)):
            distances.append(helper.getTotalDistance(population[i]))
        return distances

    # Gets 5 random numbers (0 - 99) and chooses the 
    # shortest distance
    def getBestInTournament(distances, length):
        selection =  []
        while len(selection) < 5:
            value = random.randint(0, length)
            if value not in selection:
                selection.append((value, distances[value]))
        return min(selection, key=operator.itemgetter(1))

    def getChosenParents(population, distances):
        chosenParents = []
        while len(chosenParents) < travelParms.population:
            winer = helper.getBestInTournament(distances, len(population) -1)
            #print(winer)
            chosenParents.append(winer[0])
        #print(chosenParents)
        return chosenParents
    
    def inversionReproduction(child):
        originalLength = len(child)
        length = random.randint(2, originalLength -1)
        start = random.randint(0, originalLength -1)
        end = start + length
        child.extend(child)
        #print(length, start, end)
        #print(child)
        child[start:end] = child[start:end][::-1]
        #print(child)
        if(end > originalLength -1):
            start = end - originalLength
            return child[originalLength:end] + child[start:originalLength]
        else:
            return child[0:originalLength]

    def flipReproduction(child):
        middleLength = len(child) //2
        length = random.randint(1, middleLength)
        position = random.randint(0, middleLength - length)
        position_2 = random.randint(position + length, len(child) - length)
        tempChunk = child[position:position + length]
        child[position:position + length] = child[position_2:position_2 + length]
        child[position_2:position_2 + length] = tempChunk
        return child

    def getNewPopulation(population, chosenParents):
        newPopulation = []
        for parent in chosenParents:
            child = []
            if(random.randint(0, 1) == 0):
                child = helper.inversionReproduction(population[parent].copy())
            else:
                child = helper.flipReproduction(population[parent].copy())
            newPopulation.append(child)
        return newPopulation

    def updateGraphs(i, population, distances):
        # Update history graph
        minIndx = distances.index(min(distances))
        global best
        if(distances[minIndx] < best[2]):
            best = (i, population[minIndx], distances[minIndx])
        print(i, distances[minIndx])
        ax[0].scatter(i, distances[minIndx])
        # Replace coordenates graph
        x = []
        y = []
        for i in population[minIndx]:
            x.append(cities.data[i].x)
            y.append(cities.data[i].y)
        ax[1].cla()
        ax[1].set_xlabel('X axis')
        ax[1].set_ylabel('Y axis')
        ax[1].title.set_text("Cities")
        ax[1].plot(x, y)
        plt.pause(0.1)
    

    def createGraphs(population, distances):
        minIndx = distances.index(min(distances))
        # Saves the best in a global variable
        global best 
        best = (1, population[minIndx], distances[minIndx])
        # History Figure
        global fig, ax 
        fig, ax = plt.subplots(1, 2, figsize=(12,5))
        ax[0].set_xlabel('X generations')
        ax[0].set_ylabel('Y distance')
        ax[0].title.set_text("History")
        ax[0].axis([0, 110, 0, 160])
        ax[0].scatter(1, distances[minIndx])
        # Cities Figure
        ax[1].set_xlabel('X axis')
        ax[1].set_ylabel('Y axis')
        ax[1].title.set_text("Cities")
        ax[1].axis([0, 10, 0, 10])
        x = []
        y = []
        for i in population[minIndx]:
            x.append(cities.data[i].x)
            y.append(cities.data[i].y)
        ax[1].plot(x,y)
    
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

    def grahpSingleChrom(chrom, distance):
        fig, ax = plt.subplots(1, 1, figsize=(12,5))
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.title.set_text("Total distance: " + str(distance))
        ax.axis([0, 10, 0, 11])
        x = []
        y = []
        for i in chrom:
            x.append(cities.data[i].x)
            y.append(cities.data[i].y)
        ax.plot(x,y)     
        plt.show()   

    



        
