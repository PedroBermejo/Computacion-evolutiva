import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 139, 139)

pygame.init()

boardSize = [700, 600]
screen = pygame.display.set_mode(boardSize)
pygame.display.set_caption("BOARD")

timer = pygame.time.Clock()
width = int(boardSize[0] / 20)
height = int(boardSize[1] / 20)

screen.fill(WHITE)
color = 0
for i in range(0, boardSize[0], width):
    for j in range(0, boardSize[1], height):
        if color % 2 == 0:
            pygame.draw.rect(screen, BLACK, [i, j, width, height], 0)
        else:
            pygame.draw.rect(screen, WHITE, [i, j, width, height], 0)
        color += 1
    color += 1
    
pygame.draw.rect(screen, BLUE, [3 * width, 5 * height, width, height], 0)
pygame.draw.rect(screen, GREEN, [7 * width, 10 * height, width, height], 0)

finished_game = False

while finished_game is False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            finished_game = True
    pygame.display.flip()
    timer.tick(5)

pygame.quit()