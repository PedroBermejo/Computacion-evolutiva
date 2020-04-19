import pygame
from Helper import Helper

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
        population = helper.createPopulation(1, startP, endP)
        helper.printPopulation(population)
        for matrix in population:
            helper.resetBoard(matrix)
            pygame.display.flip()
            timer.tick(5)
            
        finished_genetic = True

pygame.quit()