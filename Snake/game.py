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
    # test = SnakeLink(screen,0,20,gameWidth,gameHeight )
    font = pygame.font.Font('arial.ttf', 25) 
    while simRunning:

        screen.fill((100,100,100))

        snake.snakeMain()
        # test.linkMain()


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

#-------------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------

class Food:
    def __init__(self, screen, gameWidth,gameHeight):
        self.screen = screen
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight




#-------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()  