import pygame
import random

pygame.init()

win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Dot Game")

counterfont = pygame.font.SysFont('comicsans', 128, True, True)

class dotParent(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
counter = 10
miliseconds = 3.25*1000

while True:

    counterText = counterfont.render('' + str(counter), 1, (255, 255, 255))


    win.blit(counterText, (1100, 10))


    (mouseX, mouseY) = pygame.mouse.get_pos()
    (button1, button2, button3) = pygame.mouse.get_pressed()
    pygame.draw.circle(win, (255, 0, 0), (dot.x, dot.y), dot.radius)

    if (((mouseX <= dot.x + dot.radius) and (mouseX >= dot.x - dot.radius)) and ((mouseY <= dot.y + dot.radius) and (mouseY >= dot.y - dot.radius))) and button1 == True:
        dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
        counter -= 1
        win.fill((0, 0, 0))
        if counter == 0:
            pygame.quit()
            quit()

    # if (((mouseX >= dot.x + dot.radius) and (mouseX <= dot.x - dot.radius)) and ((mouseY >= dot.y + dot.radius) and (mouseY <= dot.y - dot.radius))) and button1 == True:
    #     dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
    #     miliseconds -= 1*1000
    #     win.fill((0, 0, 0))


    aMiliseconds = miliseconds - pygame.time.get_ticks()
    seconds = round((aMiliseconds / 1000), 2)
    secondsText = counterfont.render('' + str(seconds), 1, (255, 255, 255))
    win.blit(secondsText, (100, 10))

    pygame.display.update()
    win.fill((0, 0, 0))
    if seconds == 0:
        StartOverText = counterfont.render(("Time ran out Start over"), 1, (255, 255, 255))
        win.blit(StartOverText, (200, 480))
        pygame.time.wait(1000)
        miliseconds = 11*1000
        counter = 10
        pygame.draw.circle(win, (255, 0, 0), (dot.x, dot.y), dot.radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

#Problems = Text display on start over