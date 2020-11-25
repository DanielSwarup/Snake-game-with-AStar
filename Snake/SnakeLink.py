#Importing and initalizing PyGame for graphics
import pygame
pygame.init()

#Class for each link/unit of length of the Snake
#@params draw screen, x coordinate of link, Y coordinate of link, drawing screen width, drawing screen height, link direction of travel 
class SnakeLink:
    def __init__(self, screen, linkX,linkY,gameWidth,gameHeight):
        self.screen = screen
        self.linkX = linkX
        self.linkY = linkY
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.color = (0,200,0) 

    #Main memember function to handle food events
    def linkMain(self):
        self.__drawSnakeLink()

    #Drawing Link
    def __drawSnakeLink(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.linkX, self.linkY, 10, 10)) 

    #Setter method to update Link X and Y coordinate
    def moveLink(self, frontX,frontY):
        self.linkX = frontX
        self.linkY = frontY

    #Getting method for Link's X coordinate
    def getLinkX(self):
        return self.linkX

    #Getting method for Link's Y coordinate
    def getLinkY(self):
        return self.linkY