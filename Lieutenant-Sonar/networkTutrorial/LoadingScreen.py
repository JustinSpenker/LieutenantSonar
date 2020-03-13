import pygame
import time

def loadingScreenPlay(screen):
    while True:
        clock = pygame.time.get_ticks()

        bg = pygame.image.load("loadingScreen1.png")
        bg = pygame.transform.scale(bg, (1920, 1080))
        bg1 = pygame.image.load("loadingScreen1.png")
        bg1 = pygame.transform.scale(bg1, (1920, 1080))
        bg2 = pygame.image.load("loadingScreen2.png")
        bg2 = pygame.transform.scale(bg2, (1920, 1080))
        bg3 = pygame.image.load("loadingScreen3.png")
        bg3 = pygame.transform.scale(bg3, (1920, 1080))


        print(clock)

        if clock <= 1000:
            screen.blit(bg, (0, 0))
            pygame.display.update()
        elif clock <= 2000:
            screen.blit(bg1,(0,0))
            pygame.display.update()
        elif clock <= 3000:
            screen.blit(bg2, (0, 0))
            pygame.display.update()
        elif clock <= 4000:
            screen.blit(bg3, (0, 0))
            pygame.display.update()
        elif clock <= 5000:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()