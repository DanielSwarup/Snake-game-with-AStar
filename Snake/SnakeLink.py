import pygame
pygame.init()
from SnakeMain import *
class SnakeLink:
    def __init__(self, screen, linkX,linkY,gameWidth,gameHeight,direction):
        self.screen = screen
        self.linkX = linkX
        self.linkY = linkY
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.directon = direction
    def linkMain(self):
        self.__drawSnakeLink()
    def __drawSnakeLink(self):
        self.color = (0,200,0) 
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.linkX, self.linkY, 10, 10)) 

    def moveLink(self, frontX,frontY):
        self.linkX = frontX
        self.linkY = frontY
    def getLinkX(self):
        return self.linkX
    def getLinkY(self):
        return self.linkY
    def getDirection(self):
        return self.getDirection
    def changeDirection(self, changedDir):
        self.direction = changedDir