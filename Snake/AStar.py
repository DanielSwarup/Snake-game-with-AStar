class Node:
    def __init__(self, position:(), parent:()):
        self.parent = parent
        self.position = position

        self.g = 0
        self.f = 0
        self.h = 0
    
    def __eq__(self,other):
        return self.position == other.position
    def __lt__(self, other):
        return self.f < other.f


class AStar:
    def __init__(self, startPos, goalPos):
        #Create start and goal nodes
        self.startNode = Node(startPos, None)
        self.startNode.g = self.startNode.h = self.startNode.f = 0
        self.goalNode = Node(goalPos,None)
        self.goalNode.g = self.goalNode.h = self.goalNode.f = 0

        #Create List for open and closed nodes 
        self.openList = []
        self.closedList = []
        #Append start Node
        self.openList.append(self.startNode)

    #Check if neighbor should be added to the open List    
    def __addToOpen(self, open, neighbor):
        for node in open:
            if(neighbor == node and neighbor.f >=node.f):
                return False
        return True

    def algo(self):
        #Run while openList is not empty
        while len(self.openList)>0:
            #Sort the open list to start with the lowest cost
            self.openList.sort()
            #Set current node with the lowest cost Node
            self.currentNode = self.openList.pop(0)

            #Add the currentNode to the closedList
            self.closedList.append(self.currentNode)

            #Check if we've reached the goalNode if yes return reversed path
            if self.currentNode == self.goalNode:
                self.path = []
                while self.currentNode != self.startNode:
                    self.path.append(self.currentNode.position)
                    self.currentNode = self.currentNode.parent
                return self.path [::-1]

            (self.x, self.y) = self.currentNode.position

            self.neighbors = [(self.x-10,self.y),(self.x+10,self.y),(self.x, self.y - 10),(self.x,self.y + 10)]

            for next in self.neighbors:
                #HLDER for MAP


                self.neighbor = Node(next, self.currentNode)
                if self.neighbor in self.closedList:
                    continue
                self.neighbor.g = abs(self.neighbor.position[0] - self.startNode.position[0]) + abs(self.neighbor.position[1] - self.startNode.position[1])  
                self.neighbor.h = abs(self.neighbor.position[0] - self.goalNode.position[0]) + abs(self.neighbor.position[1] - self.goalNode.position[1])  
                self.neighbor.f = self.neighbor.g + self.neighbor.h

                if(self.__addToOpen(self.openList,self.neighbor)== True):
                    self.openList.append(self.neighbor)

        return None


            
