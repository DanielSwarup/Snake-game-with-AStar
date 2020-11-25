import pygame
pygame.init()

from SnakeMain import *
from SnakeLink import *
from Food import *

def startState(screen):
    startStateRun = True
    fontStart = pygame.font.Font('arial.ttf', 35) 

    while startStateRun:
        screen.fill((100,100,100))
        #Start if "P" is pressed
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_p]:
                startStateRun = False
        #Initialize instructions
        instruc0 = fontStart.render("Welcome to the Simulation",1,(255,255,255,0))
        startDisplay = fontStart.render("Press P To Start",1,(255,255,255,0))

        #Display instructions
        screen.blit(instruc0,(30,260))
        screen.blit(startDisplay,(30,200))

        pygame.display.update()
        # Flip the display
        pygame.display.flip()
        #Has user quit game or not
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

#Simulation State
def simState(screen, gameWidth,gameHeight):

    screen.fill((100,100,100))
    simRunning = True
    snake = Snake(screen, 20,20,gameWidth,gameHeight)
    font = pygame.font.Font('arial.ttf', 25) 
    while simRunning:
        screen.fill((100,100,100))

        snake.snakeMain()

        pygame.display.update()
        # Flip the display
        pygame.display.flip()
        #Has user quit game or not
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

    


#Main Function
def main():
    gameWidth = 900
    gameHeight = 600
    screen = pygame.display.set_mode([gameWidth, gameHeight])
    pygame.display.set_caption("Snake")
    #startState(screen)
    simState(screen, gameWidth, gameHeight)


if __name__ == "__main__":
    main()  