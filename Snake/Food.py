#Importing and initalizing PyGame for graphics
import pygame
pygame.init()

#Class for the Food
#@params Draw Screen, Food X co-ordinate, Food Y co-ordinate, Window Width, Window Height 
class Food:
    def __init__(self, screen, foodX, foodY, gameWidth,gameHeight):
        self.screen = screen
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.foodX = foodX
        self.foodY = foodY
        self.color = (255,0,0) 
    #Main memember function to handle food events
    def foodMain(self):
        self.__makeFood()
    #Food Drawing     
    def __makeFood(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.foodX, self.foodY, 10, 10)) 
    #Getter Method for Food X coordinate
    def getFoodX(self):
        return foodX
    #Getter Method for Food Y coordinate
    def getFoodY(self):
        return foodY


