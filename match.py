import pygame
pygame.init()

WIDTH = 550
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("white")

candycrush = pygame.image.load("lesson 5 - match the following/images/candycrush.jpg")
ludo = pygame.image.load("lesson 5 - match the following/images/ludo.png")
subwaysurfers = pygame.image.load("lesson 5 - match the following/images/subwaysurfer.png")
templerun = pygame.image.load("lesson 5 - match the following/images/templerun.png")

candycrushrect = pygame.Rect(90,90,90,90)
ludorect = pygame.Rect(90,200,90,90)
subwaysurfersrect = pygame.Rect(90,300,90,90)
templerunrect = pygame.Rect(90,400,90,90)

screen.blit(candycrush,candycrushrect)
#pygame.draw.rect(screen,"blue",candycrushrect,2)
screen.blit(ludo,ludorect)
#pygame.draw.rect(screen,"red",ludorect,2)
screen.blit(subwaysurfers,subwaysurfersrect)
#pygame.draw.rect(screen,"green",subwaysurfersrect,2)
screen.blit(templerun,templerunrect)
#pygame.draw.rect(screen,"yellow",templerunrect,2)

font = pygame.font.SysFont("bradleyhand",30)
subwaytext = font.render("Subway Surfers",True,"black")
subwaytextrect = pygame.Rect(240,120,220,40)
screen.blit(subwaytext,subwaytextrect)
#pygame.draw.rect(screen,"blue",subwaytextrect,2)

templeruntext = font.render("Temple Run",True,"black")
templeruntextrect = pygame.Rect(240,230,170,40)
screen.blit(templeruntext,templeruntextrect)
#pygame.draw.rect(screen,"red",templeruntextrect,2)

ludotext = font.render("Ludo",True,"black")
ludotextrect = pygame.Rect(240,320,70,40)
screen.blit(ludotext,ludotextrect)
#pygame.draw.rect(screen,"green",ludotextrect,2)

candycrushtext = font.render("Candy Crush",True,"black")
candycrushtextrect = pygame.Rect(240,430,190,40)
screen.blit(candycrushtext,candycrushtextrect)
#pygame.draw.rect(screen,"yellow",candycrushtextrect,2)

matches = [(candycrushrect,candycrushtextrect),(ludorect,ludotextrect),(subwaysurfersrect,subwaytextrect),(templerunrect,templeruntextrect)]

startpos = None
endpos = None
startrect = None
endrect = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            startpos = pygame.mouse.get_pos()
            clicked_on_valid_area = False
            for img_rect,text_rect in matches:
                if img_rect.collidepoint(startpos):
                    clicked_on_valid_area = True
                    startrect = img_rect
                    break
            if clicked_on_valid_area == True:
                pygame.draw.circle(screen,"black",startpos,4)

        if event.type == pygame.MOUSEBUTTONUP:
            endpos = pygame.mouse.get_pos()
            released_on_valid_area = False
            for img_rect,text_rect in matches:
                if text_rect.collidepoint(endpos):
                    released_on_valid_area = True
                    endrect = text_rect
                    break
            if released_on_valid_area == True and clicked_on_valid_area == True:
                pygame.draw.circle(screen,"black",endpos,4)

    pygame.display.update()