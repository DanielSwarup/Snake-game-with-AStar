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

#Next: Implement A* algo
#Possible: Implement a more efficient food position system

#Class for the main Snake
#@params draw screen, snake X coordinate, snake Y coordinate, draw screen width, draw screen height
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
        self.dead = False
        self.foodX = randint(0,self.gameWidth/10)*10
        self.foodY = randint(0,self.gameHeight/10)*10
        self.direction = "UP"
        #create a snake with 4 links
        self.__createFirstLink()
        for x in range(3):
            self.createNewLinks()
        self.__createFood()

    #Main member function for handeling the snake
    def snakeMain(self):
        self.__headMove()
        for x in self.snakeLinks:
            x.linkMain()

        for i in self.food:
            i.foodMain()
        self.__selfCollision()
    #Function to check self collision       
    def __selfCollision(self):
        for i in range(len(self.snakeLinks)-1,1,-1):
            if (self.snakeX == self.snakeLinks[i].getLinkX() and self.snakeY == self.snakeLinks[i].getLinkY()):
                self.dead = True
    #Function to eat the food, create new food, and grow the snake
    def __eatFood(self):
        if (self.snakeLinks[0].getLinkX() == self.foodX and self.snakeLinks[0].getLinkY() == self.foodY):
            self.food *= 0
            self.createNewLinks()
            self.foodX = randint(0,(self.gameWidth-20)/10)*10
            self.foodY = randint(0,(self.gameHeight-20)/10)*10
            self.__createFood()
    
    #Creating the first(Head) link of the snake
    def __createFirstLink(self):
        self.snakeLinks.append(SnakeLink(self.screen,self.snakeX,self.snakeY,self.gameWidth,self.gameHeight))

    #Function to create food and not collide with the snake. Can(MUST) be optimized
    def __createFood(self):
        for x in self.snakeLinks:
            if (x.getLinkX == self.foodX) and (x.getLinkY == self.foodY ):
                self.foodX = randint(10,(self.gameWidth-10)/10)*10
                self.foodY = randint(10,(self.gameHeight-10)/10)*10
            else: 
                self.food.append(Food(self.screen, self.foodX, self.foodY,self.gameWidth,self.gameHeight))

    #Function to create new links(grow) the snake
    def createNewLinks(self):
        if self.direction == "RT":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX()-10,self.snakeLinks[len(self.snakeLinks)-1].getLinkY(),self.gameWidth,self.gameHeight))
        elif self.direction == "LT":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX()+10,self.snakeLinks[len(self.snakeLinks)-1].getLinkY(),self.gameWidth,self.gameHeight))
        elif self.direction == "UP":
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX(),self.snakeLinks[len(self.snakeLinks)-1].getLinkY()+10,self.gameWidth,self.gameHeight))
        else:
            self.snakeLinks.append(SnakeLink(self.screen,self.snakeLinks[len(self.snakeLinks)-1].getLinkX(),self.snakeLinks[len(self.snakeLinks)-1].getLinkY()-10,self.gameWidth,self.gameHeight))
   
    #Getter method for snakeLinks which contains all the links        
    def getLinks(self):
        return self.snakeLinks()
    
    #Function in charge of moving the links
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
        else:
            self.dead = True
        if(self.snakeX<self.gameWidth-10):
            if self.keyPressed[pygame.K_RIGHT] and self.snakeDX != -10:
                self.snakeDX = 10
                self.snakeDY = 0
                self.direction = "RT"
        else:
            self.dead = True
        if(self.snakeY>0):
            if self.keyPressed[pygame.K_UP] and self.snakeDY != 10:
                self.snakeDX = 0
                self.snakeDY = -10
                self.direction = "UP"
        else:
            self.dead = True                
        if(self.snakeY<self.gameHeight-10):
            if self.keyPressed[pygame.K_DOWN]  and self.snakeDY != -10:
                self.snakeDX = 0
                self.snakeDY = 10
                self.direction = "DWN"
        else:
            self.dead = True
    
    #Return if Snake is dead or not
    def isDead(self):
        return self.dead