import pygame
from math import sqrt
pygame.init()

display_width = 1000
display_height = 750

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

mousePos = pygame.mouse.get_pos()

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Functions woo')

clock = pygame.time.Clock()


def mouseY(mousex):
    if mousex > 500:
        mousePosy = round(.65 * mousex + 100)
    else: mousePosy = round(.65 * mousex)
    return mousePosy
def yPos(mousex):
    pos = round(.65 * mousex)
def mouseX(mousex):
    if mousex == 450:
        mousex += 2
    return mousex

def radius():
    xCenter = 450
    yCenter = 293
    y = round(.65 * mousex)
    if mousex > 500:
        rad = round(sqrt((mousex - xCenter) ** 2 + (y - yCenter + 100) ** 2))
    elif mousex < xCenter - 50:
        rad = round(sqrt((mousex - xCenter) ** 2 + (y - yCenter - 100) ** 2))
    else: rad = round(sqrt((mousex - xCenter) ** 2 + (y - yCenter) ** 2))
    return rad

stop = False
clock.tick(60)
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            gameDisplay.fill(black)
            pygame.draw.line(gameDisplay, white, (0, 0), (500, 325))
            pygame.draw.line(gameDisplay, white, (501, 426), (846, 650))

            pygame.draw.circle(gameDisplay, red, (450,293), radius(), 1)
            pygame.draw.circle(gameDisplay, green, (450, 293), 4, 0)
            pygame.display.flip()
        if event.type == pygame.QUIT:
            stop = True
        print(event)

    pygame.draw.line(gameDisplay,white,(0,0),(500,325))
    pygame.draw.line(gameDisplay,white,(550, 358), (846,650))



