import pygame
import random

def dotGame():
    pygame.init()
    bg = pygame.image.load('Images/DGbg.jpeg')
    bg = pygame.transform.scale(bg, (1280, 720))
    win = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("Dot Game")

    counterfont = pygame.font.SysFont('comicsans', 128, True, True)
    timeAllowance = 8.25

    class dotParent(object):

        def __init__(self, x, y, radius):
            self.x = x
            self.y = y
            self.radius = radius

    dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
    counter = 10
    miliseconds = 8.25*1000
    startOver = "Start Over!"
    StartOverText = counterfont.render(startOver, 1, (255, 255, 255))
    trueTimePast = pygame.time.get_ticks()
    cooldownCounter1 = 0
    while True:
        win.blit(bg, (0, 0))
        counterText = counterfont.render('' + str(counter), 1, (255, 255, 255))
        win.blit(counterText, (1100, 10))

        cooldownCounter = pygame.time.get_ticks() - cooldownCounter1

        if cooldownCounter == 3000:
            cooldown = True
            cooldownCounter = 0
            cooldownCounter1 = pygame.time.get_ticks()
        else:
            cooldown = False

        (mouseX, mouseY) = pygame.mouse.get_pos()
        (button1, button2, button3) = pygame.mouse.get_pressed()

        pygame.draw.circle(win, (255, 0, 0), (dot.x, dot.y), dot.radius)

        if (((mouseX <= dot.x + dot.radius) and (mouseX >= dot.x - dot.radius)) and ((mouseY <= dot.y + dot.radius) and (mouseY >= dot.y - dot.radius))):
            if button1 == True:
                dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
                counter -= 1
                pygame.display.update()
                if counter == 0:
                    pygame.quit()
                    quit()
        else:
            if button1 == True  and cooldown == True:
                dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
                counter += 1
                pygame.display.update()
                cooldown = 5
                if counter == 0:
                    pygame.quit()
                    quit()


        # if (((mouseX >= dot.x + dot.radius) and (mouseX <= dot.x - dot.radius)) and ((mouseY >= dot.y + dot.radius) and (mouseY <= dot.y - dot.radius))) and button1 == True:
        #     dot = dotParent(random.randint(1, 1280), random.randint(0, 720), 20)
        #     miliseconds -= 1*1000
        #     win.fill((0, 0, 0))


        aMiliseconds = miliseconds - (pygame.time.get_ticks() - trueTimePast)
        seconds = round((aMiliseconds / 1000), 2)
        secondsText = counterfont.render('' + str(seconds), 1, (255, 255, 255))
        win.blit(secondsText, (100, 10))

        pygame.display.update()

        if seconds <= 0:
            timeAllowance += 1
            win.fill((0, 0, 0))
            win.blit(StartOverText, (100, 480))
            pygame.display.update()
            pygame.time.wait(1000)
            miliseconds = timeAllowance * 1000
            trueTimePast = pygame.time.get_ticks()
            counter = 10
            pygame.draw.circle(win, (255, 0, 0), (dot.x, dot.y), dot.radius)

        pygame.display.update()
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#Problems = Text display on start over