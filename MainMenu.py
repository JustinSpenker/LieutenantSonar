import pygame
import random

pygame.init()

win = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Main Menu")

TitleImg = pygame.image.load('Title.png')
# TitleImg = pygame.transform.scale(TitleImg, (800, 50))

bg = pygame.image.load('MMs.jpg')
bg = pygame.transform.scale(bg, (1600, 900))

playImg = pygame.image.load('PlayButton.png')
settingsImg = pygame.image.load('SettingsButton.png')
creditsImg = pygame.image.load('Credits.png')
helpImg = pygame.image.load('qMark.png')
tGray = pygame.image.load('TranslucentGray.png')

class play(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class settings(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class credits(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class help(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

counter = 2
TitleWidth = 800
TitleHeight = 50
TitleImg = pygame.transform.scale(TitleImg, (TitleWidth, TitleHeight))
tGray = pygame.transform.scale(tGray, (1920, 80))
while True:
    win.blit(bg, (0, 0))
    win.blit(tGray, (0, 60))
    win.blit(TitleImg, (350, 70))

    win.blit(playImg, (20, 250))
    win.blit(settingsImg, (20, 400))
    win.blit(creditsImg, (20, 550))
    win.blit(helpImg, (20, 700))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




