#Importing and initalizing PyGame for graphics
import pygame
pygame.init()
#Import SnakeLink and Food classes
from SnakeLink import *
from Food import *

#Importing Seed and randint from Random library
from random import seed
from random import randint
seed(2)
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
        self.food = []
        self.foodX = randint(0,self.gameWidth/10)*10
        self.foodY = randint(0,self.gameHeight/10)*10
        self.direction = "UP"
        self.__createFirstLink()
        for x in range(3):
            self.createNewLinks()
        self.__createFood()

    def snakeMain(self):
        self.__headMove()
        for x in self.snakeLinks:
            x.linkMain()
        for i in self.food:
            i.foodMain()

    def __eatFood(self):
        if (self.snakeLinks[0].getLinkX() == self.foodX and self.snakeLinks[0].getLinkY() == self.foodY):
            self.food *= 0
            self.createNewLinks()
            self.foodX = randint(0,self.gameWidth/10)*10
            self.foodY = randint(0,self.gameHeight/10)*10
            self.__createFood()


            
    def __createFirstLink(self):
        self.snakeLinks.append(SnakeLink(self.screen,self.snakeX,self.snakeY,self.gameWidth,self.gameHeight,self.direction))

    def __createFood(self):
        for x in self.snakeLinks:
            if (x.getLinkX == self.foodX) and (x.getLinkY == self.foodY ):
                self.foodX = randint(0,self.gameWidth/10)*10
                self.foodY = randint(0,self.gameHeight/10)*10
            else: 
                self.food.append(Food(self.screen, self.foodX, self.foodY,self.gameWidth,self.gameHeight))

    def createNewLinks(self):
        if self.direction == "RT":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX()-10,self.snakeLinks[len(self.snakeLinks)-1].getLinkY(),self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
        elif self.direction == "LT":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX()+10,self.snakeLinks[len(self.snakeLinks)-1].getLinkY(),self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
        elif self.direction == "UP":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX(),self.snakeLinks[len(self.snakeLinks)-1].getLinkY()+10,self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
        else:
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX(),self.snakeLinks[len(self.snakeLinks)-1].getLinkY()-10,self.gameWidth,self.gameHeight,self.snakeLinks[len(self.snakeLinks)-1].getDirection()))
            
    def getLinks(self):
        return self.snakeLinks()
    def moveAllLink(self):
        for x in range(len(self.snakeLinks)-1,-1,-1):
            self.snakeLinks[x].moveLink(self.snakeLinks[x-1].getLinkX(),self.snakeLinks[x-1].getLinkY())

    #Function handles movement of Head
    def __headMove(self):
        self.snakeLinks[0].moveLink(self.snakeX,self.snakeY)
        self.ticksPast = pygame.time.get_ticks()

        #Directional Maniplulation
        self.keyPressed = pygame.key.get_pressed()
        if(self.ticksPast % 100 == 0):
            if(self.snakeX>0) and (self.snakeX<self.gameWidth-10):
                self.snakeX += self.snakeDX
                self.__eatFood()
            if(self.snakeY>0) and (self.snakeY<self.gameHeight -10):
                self.snakeY += self.snakeDY
                self.__eatFood()
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
