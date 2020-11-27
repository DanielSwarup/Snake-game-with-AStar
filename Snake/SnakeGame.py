#Importing and initalizing PyGame for graphics
import pygame
pygame.init()

#Import Snake Main 
from SnakeMain import *

class SnakeGame:
    def __init__(self):
        #Come back to this and change to gamewidth
        self.gameWidth = 900
        self.gameHeight = 600
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode([self.gameWidth, self.gameHeight])
        self.state = 0
        self.fontStart = pygame.font.Font('arial.ttf', 35) 
        self.__stateSetter()
        
    def __drawBoarder(self):
        self.color = (0,0,0)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(0, 0, self.gameWidth, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(0, 0, 10, self.gameHeight))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(0, self.gameHeight-10, self.gameWidth, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.gameWidth-10, 0, 10, self.gameHeight)) 
    def __stateSetter(self):
        if self.state == 0:
            self.__startState()
        else:
            self.__gameState()
    def __startState(self):
        while self.state == 0:
            self.screen.fill((100,100,100))
            #Start if "P" is pressed
            self.keyPressed = pygame.key.get_pressed()
            if self.keyPressed[pygame.K_p]:
                self.state = 1
                self.__stateSetter()
            #Initialize instructions
            self.instruc0 = self.fontStart.render("Welcome to the Simulation",1,(255,255,255,0))
            self.startDisplay = self.fontStart.render("Press P To Start",1,(255,255,255,0))

            #Display instructions
            self.screen.blit(self.instruc0,(30,260))
            self.screen.blit(self.startDisplay,(30,200))

            pygame.display.update()
            # Flip the display
            pygame.display.flip()
            #Has user quit game or not
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def __gameState(self):
        self.snake = Snake(self.screen, 20,20,self.gameWidth,self.gameHeight)
        while self.state == 1:
            self.screen.fill((100,100,100))
            self.__drawBoarder()
            self.snake.snakeMain()
            if self.snake.isDead():
                self.__gameState()
            pygame.display.update()
            # Flip the display
            pygame.display.flip()
            #Has user quit game or not
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()