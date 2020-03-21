import random
import math
import operator
from BinaryTree import Tree
import matplotlib.pyplot as plt

class helper:
    operators = ['+', '-', '*', '/']
    popularity = [64.5, 61.0, 62.8, 61.1, 61.8, 63.2, 62.8, 58.6, 58.7, 57.3, 55.1]

    # Calculates number of all nodes in a tree given depth
    def calculateNumberOfNodes(depth):
        numbNodes = 0
        for i in range(depth):
            numbNodes = numbNodes + math.pow(2, i)
        return numbNodes

    def createPopulation(lengthPopu, dephTree):
        population = []
        numbOperators = int(helper.calculateNumberOfNodes(dephTree -1))
        numbLeaves = int(helper.calculateNumberOfNodes(dephTree)) - numbOperators
        for i in range(lengthPopu):
            chromOperators = helper.createRandomOperationList(numbOperators)
            chromNumbers = helper.createRandomNumbersList(numbLeaves)
            tree = Tree()
            tree.createFromList(chromOperators + chromNumbers)
            population.append(tree)
        return population

    def printPopulation(population):
        for i in range(len(population)):
            print('Tree number:', i)
            population[i].printTree()
            
    def createRandomOperationList(length):
        chrom = []
        for i in range(length):
            randNum = random.randrange(len(helper.operators))
            chrom.append(helper.operators[randNum])
        
        randIndex = random.randrange(length)
        chrom[randIndex] = chrom[randIndex] + 'math.sin'
        '''
        secondRandIndex = random.randrange(length)
        while(randIndex == secondRandIndex):
            secondRandIndex = random.randrange(length)
        chrom[secondRandIndex] = chrom[secondRandIndex] + 'math.log10'
        '''
        return chrom

    def createRandomNumbersList(length):
        chrom = []
        for i in range(length):
            randNum = random.randrange(10)
            if (randNum is 0):
                randNum = 0.000001
            chrom.append(str(randNum))

        numVariables = int(random.randrange(1, length))
        for i in range(numVariables):
            randNum = int(random.randrange(len(chrom)))
            chrom[randNum] = chrom[randNum] + '*x'

        return chrom

    def evaluatePopulation(population):
        errors = []
        for i in range(len(population)):
            acumError = 0
            ecuation = population[i].createEcuation()
            for j in range(len(helper.popularity)):
                if(j==0):
                    x = 0.000001
                else: 
                    x = j
                try:
                    y = eval(ecuation)
                except ZeroDivisionError:
                    y = 1000
                diff = helper.popularity[j] - y
                acumError = acumError + abs(diff)
            errors.append(acumError)
        return errors

    def getYvaluesFromTree(tree):
        yValues = []
        ecuation = tree.createEcuation()
        for j in range(len(helper.popularity)):
            if(j==0):
                x = 0.000001
            else: 
                x = j
            yValues.append(eval(ecuation))

        return yValues

    def getBestInTournament(errors, percent):
        selection =  []
        while len(selection) < percent:
            value = random.randint(0, len(errors) -1)
            if value not in selection:
                selection.append((value, errors[value]))
        return min(selection, key=operator.itemgetter(1))

    def getChosenParents(population, errors, percent):
        chosenParents = []
        while len(chosenParents) < len(population):
            winer = helper.getBestInTournament(errors, percent)
            #print(winer)
            chosenParents.append(winer[0])
        #print(chosenParents)
        return chosenParents

    def crossover(tree_1, tree_2, depth):
        numbNodes = helper.calculateNumberOfNodes(depth)
        crossPoint = random.randint(2, numbNodes - 1)
        #print("CrossPoint:", crossPoint, "Number nodes:", numbNodes)
        #print("Tree_1:", tree_1.creationList)
        #print("Tree_2:", tree_2.creationList)
        list_1 = tree_1.creationList[0:crossPoint] + tree_2.creationList[crossPoint:int(numbNodes)]
        list_2 = tree_2.creationList[0:crossPoint] + tree_1.creationList[crossPoint:int(numbNodes)]
        #print()
        #print("List_1:", list_1)
        #print("List_2:", list_2)
        newTree_1 = Tree()
        newTree_2 = Tree()
        newTree_1.createFromList(list_1)
        newTree_2.createFromList(list_2)
        return newTree_1, newTree_2

    def replication(tree_1, tree_2):
        newTree_1 = tree_1.cloneTree()
        newTree_2 = tree_2.cloneTree()
        return newTree_1, newTree_2

    def mutate(tree_1, tree_2, depth):
        newTrees = helper.createPopulation(2, depth)
        newTree_1, waste = helper.crossover(tree_1, newTrees[0], depth)
        newTree_2, waste = helper.crossover(tree_2, newTrees[1], depth)
        return newTree_1, newTree_2

    def getNewPopulation(errors, population, chosenParents, depth):
        newPopulation = []
        i = 0
        #print("Population:", len(population), "Chosen:", len(chosenParents))
        while(i < len(chosenParents)):
            randNumb = random.randint(0, 1000)/1000
            child_1, child_2 = None, None
            if(randNumb <= 0.1):
                winer_1 = helper.getBestInTournament(errors, 10)
                winer_2 = helper.getBestInTournament(errors, 10)
                child_1, child_2 = helper.replication(population[winer_1[0]], population[winer_2[0]])
            elif(randNumb <= 0.8):
                child_1, child_2 = helper.crossover(population[i], population[i+1], depth)
            else:
                child_1, child_2 = helper.mutate(population[i], population[i+1], depth)
            i = i+2
            newPopulation.append(child_1)
            newPopulation.append(child_2)
        return newPopulation

    def createGraphs(population, errors):
        minIndx = errors.index(min(errors))
        # Saves the best in all 100 generations
        global best 
        best = (1, population[minIndx], errors[minIndx])
        # History Figure will acumulate, Popularity is replaced
        global fig, ax 
        fig, ax = plt.subplots(1, 2, figsize=(12,5))
        ax[0].set_xlabel('X generations')
        ax[0].set_ylabel('Y error')
        ax[0].title.set_text("Current error: " + str(errors[minIndx]))
        ax[0].axis([0, 110, 0, 100])
        ax[0].scatter(1, errors[minIndx])
        # Cities Figure
        ax[1].set_xlabel('X time')
        ax[1].set_ylabel('Y popularity')
        ax[1].title.set_text("Ecuation: " + population[minIndx].createEcuation())
        ax[1].axis([0, 11, 0, 100])
        x = []
        for i in range(len(helper.popularity)):
            x.append(i)
        y = helper.getYvaluesFromTree(population[minIndx])
        ax[1].plot(x,y)
        ax[1].plot(x,helper.popularity)

    def updateGraphs(i, population, errors):
        # Update history graph
        minIndx = errors.index(min(errors))
        global best
        if(errors[minIndx] < best[2]):
            best = (i, population[minIndx], errors[minIndx])
        print(i, errors[minIndx])
        ax[0].scatter(i, errors[minIndx])
        ax[0].title.set_text("Current error: " + str(errors[minIndx]))
        # Replace coordenates graph
        x = []
        ax[1].cla()
        ax[1].set_xlabel('X time')
        ax[1].set_ylabel('Y popularity')
        ax[1].title.set_text("Ecuation: " + population[minIndx].createEcuation())
        for j in range(len(helper.popularity)):
            x.append(j)
        y = helper.getYvaluesFromTree(population[minIndx])
        ax[1].plot(x, y)
        ax[1].plot(x, helper.popularity)
        plt.pause(0.01)

    def printBest(i):
        print("Best: ", best[0], best[2])
        ax[0].scatter(i, best[2])
        ax[0].title.set_text("Lowest error: " + str(best[2]))
        x = []
        ax[1].cla()
        ax[1].set_xlabel('X time')
        ax[1].set_ylabel('Y popularity')
        ax[1].title.set_text("Ecuation: " + best[1].createEcuation())
        for j in range(len(helper.popularity)):
            x.append(j)
        y = helper.getYvaluesFromTree(best[1])
        ax[1].plot(x, y)
        ax[1].plot(x, helper.popularity)
        plt.pause(0.01)