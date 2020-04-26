import pygame
import operator
from Helper import Helper

def job():
    print("I'm working...")

pygame.init()
pygame.display.set_caption("BOARD")

helper = Helper()

finished_game = False
finished_genetic = False

clock = pygame.time.Clock()
results = []

startP, endP = helper.getRandomStartEndPositions()
print("Start position:", startP)
print("End position:", endP)
population = helper.createPopulation(4, startP, endP)
results.append(min(population, key=operator.itemgetter(1)))

for i in range(20):
    population = helper.generateNewPopulation_2(population, startP, endP)
    results.append(min(population, key=operator.itemgetter(1)))

helper.printPopulation(results)

for i in range(len(results)):
    finished_game = False
    while finished_game is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_game = True
        helper.resetBoard(results[i][0], i)
        pygame.display.flip()
        clock.tick(35)
        pygame.time.delay(500)
        if i < len(results) - 1:
            finished_game = True

pygame.quit()