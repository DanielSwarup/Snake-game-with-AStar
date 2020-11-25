
import pygame
pygame.init()
from SnakeMain import *

class Food:
    def __init__(self, screen, foodX, foodY, gameWidth,gameHeight):
        self.screen = screen
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.foodX = foodX
        self.foodY = foodY
        self.color = (255,0,0) 
    def foodMain(self):
        self.__makeFood()
    def __makeFood(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.foodX, self.foodY, 10, 10)) 
    def getFoodX(self):
        return foodX
    def getFoodY(self):
        return foodY


