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

    def resetBoard(self, matrix):
        self.screen.fill(self.WHITE)
        color = 0
        for i in range(0, self.boardNumber):
            for j in range(0, self.boardNumber):
                if matrix[i][j] > 0:
                    pygame.draw.rect(self.screen, self.BLUE, [i*self.width, j*self.height, self.width, self.height], 0)
                elif color % 2 == 0:
                    pygame.draw.rect(self.screen, self.BLACK, [i*self.width, j*self.height, self.width, self.height], 0)
                else:
                    pygame.draw.rect(self.screen, self.WHITE, [i*self.width, j*self.height, self.width, self.height], 0)
                color += 1
            color += 1


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
        for i in self.Y_1:
            for j in self.X_2:
                Y = eval(i)
                X = eval(j)
                if(Y >= 0 and Y < self.boardNumber and X >= 0 and X < self.boardNumber):
                    posibles.append([Y, X]) 
        for i in self.Y_2:
            for j in self.X_1:
                Y = eval(i)
                X = eval(j)
                if(Y >= 0 and Y < self.boardNumber and X >= 0 and X < self.boardNumber):
                    posibles.append([Y, X])
        return posibles
                
    def createEmptyMatrix(self):
        return [[0 for x in range(self.boardNumber)] for y in range(self.boardNumber)]

    # x is the with, y is the height, in the matrix is matrix[y][x]
    def createChrom(self, startP, endP):
        matrix = self.createEmptyMatrix()
        matrix[startP[0]][startP[1]] = 2
        matrix[endP[0]][endP[1]] = 2 
        goingP = [startP[0], startP[1]]
        iterations = 0
        while (endP[0] != goingP[0] or endP[1] != goingP[1]) and iterations < 1:
            print("Iteration:", iterations)
            posibleMoves = self.getPosibleMoves(matrix, goingP)
            for move in posibleMoves:
                matrix[move[0]][move[1]] = 1
            iterations = iterations + 1
        return matrix
        

    def createPopulation(self, lengthPopulation, startP, endP):
        population = []
        for i in range(lengthPopulation):
            population.append(self.createChrom(startP, endP))
        return population


    def printPopulation(self, population):
        for c in range(len(population)):
            print("Chrom number", c)
            for y in range(len(population[c])):
                for x in range(len(population[c][y])):
                    print(population[c][y][x], end=" ")
                print()

'''

'''