import random
import math
import operator
import pygame

class Helper:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 139, 139)
        self.GRAY = (150, 150, 150)
        self.RED = (255, 0, 0)
        self.boardSize = [688, 592]
        self.screen = pygame.display.set_mode(self.boardSize)
        self.boardNumber = 16
        self.width = int(self.boardSize[0] / 16)
        self.height = int(self.boardSize[1] / 16)
        self.sequenceOp = [2, 1]
        self.Y_1 = ['y + 1', 'y - 1']
        self.Y_2 = ['y + 2', 'y - 2']
        self.X_1 = ['x + 1', 'x - 1']
        self.X_2 = ['x + 2', 'x - 2']

    def resetBoard(self, matrix, generation):
        pygame.display.set_caption("Generation: " + str(generation))
        self.screen.fill(self.WHITE)
        colorInd = 0
        font = pygame.font.Font('freesansbold.ttf', 32)
        for i in range(0, self.boardNumber):
            color = None
            for j in range(0, self.boardNumber):
                if matrix[j][i] == -1:
                    color = self.BLUE
                elif matrix[j][i] == -2:
                    color = self.GREEN
                elif matrix[j][i] == 0:
                    if colorInd % 2 == 0:
                        color = self.BLACK
                    else:
                        color = self.WHITE
                else:
                    color = self.GRAY
                pygame.draw.rect(self.screen, color, [i*self.width, j*self.height, self.width, self.height], 0)
                if matrix[j][i] > 0:
                    text = font.render(str(matrix[j][i]), False, self.RED)
                    textRect = text.get_rect()
                    textRect.center = (i*self.width + self.width / 2, j*self.height + self.height / 2) 
                    self.screen.blit(text, textRect) 
                colorInd += 1
            colorInd += 1
        

    def getRandomStartEndPositions(self):
        startP = (random.randint(0, self.boardNumber / 4 -1), random.randint(0, self.boardNumber -1))
        endP = (random.randint(self.boardNumber * 3 / 4 -1, self.boardNumber -1), random.randint(0, self.boardNumber -1))
        return startP, endP

    # Formula goes Y +2, X +1 and all combination of simbols and changing position of the numbers
    # Y +2, X +1 | Y -2, X +1 | Y +2, X -1 | Y -2, X -1
    # Y +1, X +2 | Y -1, X +2 | Y +1, X -2 | Y -1, X -2
    def getPosibleMoves(self, matrix, goingP):
        posibles = []
        y = goingP[0]
        x = goingP[1]
        for i in self.X_1:
            for j in self.Y_2:
                Y = eval(j)
                X = eval(i)
                if(Y >= 0 and Y < self.boardNumber and X >= 0 and X < self.boardNumber
                and (matrix[Y][X] is 0 or matrix[Y][X] is -2)):
                    posibles.append([Y, X])
        for i in self.X_2:
            for j in self.Y_1:
                Y = eval(j)
                X = eval(i)
                if(Y >= 0 and Y < self.boardNumber and X >= 0 and X < self.boardNumber
                and (matrix[Y][X] is 0 or matrix[Y][X] is -2)):
                    posibles.append([Y, X])
        return posibles

    def createEmptyMatrix(self, startP, endP):
        matrix = [[0 for x in range(self.boardNumber)] for y in range(self.boardNumber)]
        matrix[startP[0]][startP[1]] = -1
        matrix[endP[0]][endP[1]] = -2
        return matrix

    # x is the with, y is the height, in the matrix is matrix[y][x]
    def createChrom(self, startP, endP):
        matrix = self.createEmptyMatrix(startP, endP)
        goingP = [startP[0], startP[1]]
        iterations = 1
        while True:
            #print("Iteration:", iterations)
            posibleMoves = self.getPosibleMoves(matrix, goingP)
            for move in posibleMoves:
                if move[0] is endP[0] and move[1] is endP[1]:
                    return (matrix, iterations + 1)
            if len(posibleMoves) is 0:
                matrix = self.createEmptyMatrix(startP, endP)
                goingP = [startP[0], startP[1]]
                iterations = 1
            else:
                chosen = random.randint(0, len(posibleMoves) -1)
                matrix[posibleMoves[chosen][0]][posibleMoves[chosen][1]] = iterations
                goingP[0] = posibleMoves[chosen][0]
                goingP[1] = posibleMoves[chosen][1]
                iterations = iterations + 1        

    def createPopulation(self, lengthPopulation, startP, endP):
        population = []
        for i in range(lengthPopulation):
            population.append(self.createChrom(startP, endP))
        return population

    def printPopulation(self, population):
        for c in range(len(population)):
            print("Generation:", c, "Moves:", population[c][1])
            for i in range(len(population[c][0])):
                for j in range(len(population[c][0][i])):
                    print(population[c][0][i][j], end=" ")
                print()

    def exchage(self, parent_1, parent_2, chosenPoint, startP, endP):
        crossPointChild_1 = parent_1[0][chosenPoint[0]][chosenPoint[1]]
        crossPointChild_2 = parent_2[0][chosenPoint[0]][chosenPoint[1]]
        print(chosenPoint, crossPointChild_1, crossPointChild_2)

        matrix_1 = self.createEmptyMatrix(startP, endP)
        matrix_2 = self.createEmptyMatrix(startP, endP)
        iterations_1 = 1
        iterations_2 = 1
        # Generate matrix 1 with firt part of parent_1 and second part of parent_2
        for i in range(0, self.boardNumber):
            for j in range(0, self.boardNumber):
                if parent_1[0][j][i] > 0 and parent_1[0][j][i] <= crossPointChild_1:
                    matrix_1[j][i] = iterations_1
                    iterations_1 = iterations_1 + 1
                if parent_2[0][j][i] > 0 and parent_2[0][j][i] <= crossPointChild_2:
                    matrix_2[j][i] = iterations_2
                    iterations_2 = iterations_2 + 1
                
        for i in range(0, self.boardNumber):
            for j in range(0, self.boardNumber):
                if parent_1[0][j][i] > crossPointChild_1:
                    matrix_2[j][i] = iterations_2
                    iterations_2 = iterations_2 + 1
                if parent_2[0][j][i] > crossPointChild_2:
                    matrix_1[j][i] = iterations_1
                    iterations_1 = iterations_1 + 1
                

        print("Iterations 1:", iterations_1)
        print("Iterations 2:", iterations_2)

        return (matrix_1, iterations_1), (matrix_2, iterations_2)


    def reproduce(self, parent_1, parent_2, startP, endP):
        crossPoints = []
        for i in range(0, self.boardNumber):
            for j in range(0, self.boardNumber):
                if parent_1[0][j][i] > 0 and parent_2[0][j][i] > 0:
                    crossPoints.append((j, i))

        if len(crossPoints) is 0:
            return parent_1, parent_2
        else:
            chosenPoint = random.randint(0, len(crossPoints) -1)
            return self.exchage(parent_1, parent_2, crossPoints[chosenPoint], startP, endP)


    def generateNewPopulation(self, population, startP, endP):
        newPopulation = []
        i = 0
        while len(newPopulation) < len(population):
            rand_ind_1 = random.randint(0, len(population) -1)
            rand_ind_2 = rand_ind_1
            while rand_ind_2 is rand_ind_1:
                rand_ind_2 = random.randint(0, len(population) -1)
                
            child_1, child_2 = self.reproduce(population[rand_ind_1], population[rand_ind_2], startP, endP)
            i = i + 2
            newPopulation.append(child_1)
            newPopulation.append(child_2)
    
        # This will get the best in old popoulation and replace worst in new population    
        maxValueInd = newPopulation.index(max(newPopulation, key=operator.itemgetter(1)))
        newPopulation[maxValueInd] = min(population, key=operator.itemgetter(1))
        
        return newPopulation

    def generateNewPopulation_2(self, population, startP, endP):
        newPopulation = self.createPopulation(len(population), startP, endP)
        newPopulation.append(min(population, key=operator.itemgetter(1)))

        return newPopulation
            
