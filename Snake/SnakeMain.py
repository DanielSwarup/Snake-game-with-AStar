import pygame
pygame.init()
from SnakeLink import *
class Snake:
    def __init__(self, screen, snakeX,snakeY,gameWidth,gameHeight):
        self.screen = screen
        self.snakeX = snakeX
        self.snakeY = snakeY
        self.snakeDX = 10
        self.snakeDY = 0
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.ticksPast = pygame.time.get_ticks()
        self.snakeLinks = []
        self.direction = "UP"
        self.oldPos = []
        self.__createFirstLink()
        self.createNewLinks()
        self.createNewLinks()
        self.createNewLinks()





    def snakeMain(self):
        self.__headMove()
        for x in self.snakeLinks:
            x.linkMain()

    def __createFirstLink(self):
        self.snakeLinks.append(SnakeLink(self.screen,self.snakeX,self.snakeY,self.gameWidth,self.gameHeight,self.direction))

    def createNewLinks(self):
        if self.direction == "RT":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX()-10,self.snakeLinks[len(self.snakeLinks)-1].getLinkY(),self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
        elif self.direction == "LT":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX()+10,self.snakeLinks[len(self.snakeLinks)-1].getLinkY(),self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
        elif self.direction == "UP":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX(),self.snakeLinks[len(self.snakeLinks)-1].getLinkY()+10,self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
        else:
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX(),self.snakeLinks[len(self.snakeLinks)-1].getLinkY()-10,self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
            

    def moveAllLink(self):
        print(len(self.snakeLinks)-1)

        for x in range(len(self.snakeLinks)-1,-1,-1):
            self.snakeLinks[x].moveLink(self.snakeLinks[x-1].getLinkX(),self.snakeLinks[x-1].getLinkY())

    #Function handles movement of Head
    def __headMove(self):
        self.snakeLinks[0].moveLink(self.snakeX,self.snakeY)
        self.ticksPast = pygame.time.get_ticks()



        #Directional Maniplulation
        self.keyPressed = pygame.key.get_pressed()
        if(self.ticksPast % 300 == 0):
            if(self.snakeX>0) and (self.snakeX<self.gameWidth-10):
                self.snakeX += self.snakeDX
            if(self.snakeY>0) and (self.snakeY<self.gameHeight -10):
                self.snakeY += self.snakeDY
            self.moveAllLink()

        # User interactions for Snake head movement
        if(self.snakeX>0):
            if self.keyPressed[pygame.K_LEFT] and self.snakeDX != 10:
                self.snakeDX = -10
                self.snakeDY = 0
                self.direction = "LT"
        if(self.snakeX<self.gameWidth-10):
            if self.keyPressed[pygame.K_RIGHT] and self.snakeDX != -10:
                self.snakeDX = 10
                self.snakeDY = 0
                self.direction = "RT"
        if(self.snakeY>0):
            if self.keyPressed[pygame.K_UP] and self.snakeDY != 10:
                self.snakeDX = 0
                self.snakeDY = -10
                self.direction = "UP"
        if(self.snakeY<self.gameHeight-10):
            if self.keyPressed[pygame.K_DOWN]  and self.snakeDY != -10:
                self.snakeDX = 0
                self.snakeDY = 10
                self.direction = "DWN"
