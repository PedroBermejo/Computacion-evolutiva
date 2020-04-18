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

    def resetBoard(self):
        self.screen.fill(self.WHITE)
        color = 0
        for i in range(0, self.boardSize[0], self.width):
            for j in range(0, self.boardSize[1], self.height):
                if color % 2 == 0:
                    pygame.draw.rect(self.screen, self.BLACK, [i, j, self.width, self.height], 0)
                else:
                    pygame.draw.rect(self.screen, self.WHITE, [i, j, self.width, self.height], 0)
                color += 1  
            color += 1

    def getRandomStartEndPositions(self):
        startP = (random.randint(0, self.boardNumber / 4 -1), random.randint(0, self.boardNumber -1))
        endP = (random.randint(self.boardNumber * 3 / 4 -1, self.boardNumber -1), random.randint(0, self.boardNumber -1))
        return startP, endP

    # x is the with, y is the height, in the matrix is matrix[y][x]
    def createChrom(self, startP, endP):
        matrix = [[0 for x in range(self.boardNumber)] for y in range(self.boardNumber)]
        matrix[startP[0]][startP[1]] = 2
        matrix[endP[0]][endP[1]] = 2 
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