import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 139, 139)

pygame.init()

dimensiones = [700, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("TABLERO")

juego_terminado = False

reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / 20)
alto = int(dimensiones[1] / 20)

pantalla.fill(BLANCO)
color = 0
for i in range(0, dimensiones[0], ancho):
    for j in range(0, dimensiones[1], alto):
        if color % 2 == 0:
            pygame.draw.rect(pantalla, NEGRO, [i, j, ancho, alto], 0)
        else:
            pygame.draw.rect(pantalla, BLANCO, [i, j, ancho, alto], 0)
        color += 1
    color += 1
    
pygame.draw.rect(pantalla, AZUL, [3 * ancho, 5 * alto, ancho, alto], 0)
pygame.draw.rect(pantalla, VERDE, [7 * ancho, 10 * alto, ancho, alto], 0)

while juego_terminado is False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True
    pygame.display.flip()
    reloj.tick(5)

pygame.quit()