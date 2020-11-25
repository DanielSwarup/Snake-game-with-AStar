import pygame
pygame.init()

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
    test = SnakeLink(screen,0,20,gameWidth,gameHeight )
    font = pygame.font.Font('arial.ttf', 25) 
    while simRunning:

        screen.fill((100,100,100))

        snake.snakeMain()
        test.linkMain()


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

    def snakeMain(self):
        self.__snakeHead()
        self.__headMove()
    def __snakeHead(self):
        self.color = (0,200,0) 
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.snakeX, self.snakeY, 10, 10)) 
    def __snakeLink(self):
        self.color = (0,200,0) 


    #Function handles movement of Head
    def __headMove(self):
        self.ticksPast = pygame.time.get_ticks()
        #Directional Maniplulation
        self.keyPressed = pygame.key.get_pressed()
        if(self.ticksPast % 300 == 0):
            if(self.snakeX>0) and (self.snakeX<self.gameWidth-10):
                self.snakeX += self.snakeDX
            if(self.snakeY>0) and (self.snakeY<self.gameHeight -10):
                self.snakeY += self.snakeDY

        # User interactions for Snake head movement
        if(self.snakeX>0):
            if self.keyPressed[pygame.K_LEFT] and self.snakeDX != 10:
                self.snakeDX = -10
                self.snakeDY = 0
        if(self.snakeX<self.gameWidth-10):
            if self.keyPressed[pygame.K_RIGHT] and self.snakeDX != -10:
                self.snakeDX = 10
                self.snakeDY = 0
        if(self.snakeY>0):
            if self.keyPressed[pygame.K_UP] and self.snakeDY != 10:
                self.snakeDX = 0
                self.snakeDY = -10
        
        if(self.snakeY<self.gameHeight-10):
            if self.keyPressed[pygame.K_DOWN]  and self.snakeDY != -10:
                self.snakeDX = 0
                self.snakeDY = 10
#-------------------------------------------------------------------------------------------
class SnakeLink:
    def __init__(self, screen, linkX,linkY,gameWidth,gameHeight):
        self.screen = screen
        self.linkX = linkX
        self.linkY = linkY
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
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




#-------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()  