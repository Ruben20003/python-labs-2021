import pygame


pygame.init()

սեվ = (  0,   0,   0)
սպիտակ = (255, 255, 255)
կապույտ =  (  0,   0, 255)
կանաչ = (  0, 255,   0)
կարմիր =   (255,   0,   0)
մոխրագույն =  (128, 128, 128)
դեղին =(255, 255,   0)

FPS = 30
screen = pygame.display.set_mode((800, 800))


screen.fill(մոխրագույն)

pygame.draw.circle(screen, դեղին, (400, 400), 200)
pygame.draw.circle(screen, սեվ, (400, 400), 200, 3)

pygame.draw.circle(screen, կարմիր, (325, 350), 45)
pygame.draw.circle(screen, կարմիր, (475, 350), 30)

pygame.draw.circle(screen, սեվ, (325, 350), 45, 1)
pygame.draw.circle(screen, սեվ, (475, 350), 30, 1)

pygame.draw.circle(screen, սեվ, (325, 350), 15)
pygame.draw.circle(screen, սեվ, (475, 350), 15)

pygame.draw.rect(screen, սեվ, (325, 475, 150, 25))

pygame.draw.polygon(screen, սեվ, [(325, 275), (310, 295), (370, 325), (385, 305)])

pygame.draw.polygon(screen, սեվ, [(475, 275), (490, 295), (430, 325), (415, 305)])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

