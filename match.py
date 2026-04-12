import pygame
pygame.init()

WIDTH = 550
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("white")

candycrush = pygame.image.load("lesson 5 - match the following/images/candycrush.jpg")
#pygame.image.load("")
candycrushrect = pygame.Rect(90,90,110,110)

screen.blit(candycrush,candycrushrect)
pygame.draw.rect(screen,"blue",candycrushrect,2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()