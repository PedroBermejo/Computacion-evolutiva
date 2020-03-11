import random
import math
from BinaryTree import Tree

class helper:
    operators = ['+', '-', '*', '/']
    popularity = [64.5, 61.0, 62.8, 61.1, 61.8, 63.2, 62.8, 58.6, 58.7, 57.3, 55.1]

    def calculateNumberOfNodes(deph):
        numbNodes = 0
        for i in range(deph):
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
                y = eval(ecuation)
                diff = helper.popularity[j] - y
                acumError = acumError + abs(diff)
            errors.append(acumError)
        return errors
