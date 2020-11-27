from queue import PriorityQueue
import pygame
import math
class Node:
    def __init__(self, parent = None, position = None)
        self.parent = parent
        self.position = position

        self.g = 0
        self.f = 0
        self.h = 0
    
    def __eq__(self,other)
        return self.position == other.position
    def __lt__(self, other)
        return self.f< other.f


class AStar:
    def __init__(self, startPos, goalPos):
        #Create start and goal nodes
        self.startNode = Node(None, startPos)
        self.startNode.g = self.startNode.h = self.startNode.f = 0
        self.goalNode = Node(None, goalPos)
        self.goalNode.g = self.goalNode.h = self.goalNode.f = 0

        #Create List for open and closed nodes 
        self.openList = []
        self.closedList = []
        #Append start Node
        self.openList.append(self.startPos)


    def __algo(self):
        #Run while openList is not empty
        while len(openList)>0
 
            self.openList.sort()
            self.currentNode = self.openList.pop(0)

            self.closedList.append(self.currentNode)
            if self.currentNode == self.goalNode:
                self.path = []
                while self.currentNode != self.startNode:
                    self.path.append(self.currentNode.position)
                    self.currentNode = self.currentNode.parent
                return path [::-1]

            (self.x, self.y) = self.currentNode.position
            self.neighbors = [(self.x-10,y),(self.x+10,self.y),(self.x, self.y - 10),(self.x,self.y + 10)]

            for next in self.neighbors:
                pass


        return None


            
