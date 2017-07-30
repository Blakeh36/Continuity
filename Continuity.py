import pygame
from math import sqrt


#setting up window
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

pygame.display.set_caption('Continuity')

clock = pygame.time.Clock()


def mouseX(mousex):
    if mousex == 450:
        mousex += 2
    return mousex
""" The graph is basically a view of the quadrant IV and the graph:
 y = -.65x for 0 <= x < 500
 and
 y = -.65x for 500 < x < 856

 Later, it should be able to be any function with y as a function of x
"""
def radius(): #changes the radius based on where the jump is
    xCenter = 450
    yCenter = 293
    y = round(.65 * mousex)
    if mousex > 500:
        rad = round(sqrt((mousex - xCenter) ** 2 + (y - yCenter + 100) ** 2)) #uses pythagorean theorem to calculate the radius
    elif mousex < xCenter - 50:
        rad = round(sqrt((mousex - xCenter) ** 2 + (y - yCenter - 100) ** 2))
    else: rad = round(sqrt((mousex - xCenter) ** 2 + (y - yCenter) ** 2))
    return rad

stop = False
clock.tick(60)
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos #get the x and y values from the mouse's position
            gameDisplay.fill(black) #resets the screen to redraw the circle
            pygame.draw.line(gameDisplay, white, (0, 0), (500, 325))
            pygame.draw.line(gameDisplay, white, (501, 426), (846, 650))

            pygame.draw.circle(gameDisplay, red, (450,293), radius(), 1)
            pygame.draw.circle(gameDisplay, green, (450, 293), 4, 0)
            pygame.display.flip() #updates screen
        if event.type == pygame.QUIT:
            stop = True
        print(event)

    pygame.draw.line(gameDisplay,white,(0,0),(500,325))
    pygame.draw.line(gameDisplay,white,(550, 358), (846,650))



