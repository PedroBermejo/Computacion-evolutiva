import pygame
import operator
from Helper import Helper

def job():
    print("I'm working...")

pygame.init()
pygame.display.set_caption("BOARD")

helper = Helper()

timer = pygame.time.Clock()
finished_game = False
finished_genetic = False
while finished_game is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_game = True
    pygame.display.flip()
    timer.tick(5)
    if(finished_genetic is False):
        startP, endP = helper.getRandomStartEndPositions()
        print("Start position:", startP)
        print("End position:", endP)
        population = helper.createPopulation(10, startP, endP)
        helper.resetBoard(min(population, key=operator.itemgetter(1))[0])
        finished_genetic = True

pygame.quit()