from queue import PriorityQueue
import pygame
import math

# class AStar:
#     def __init__(self, startPos, goalPos):
#         self.startPos = startPos
#         self.goalPos = goalPos

#         self.count = 0
#         self.openSet = PriorityQueue()
#         self.openSet.put((0,self.count,self.startPos))
#         self.cameFrom = {}
#         self.gScore = {spot: float("inf")}
#         self.gScore[startPos] = 0

#         self.fScore = {spot: float("inf")}
#         self.fScore[startPos] = self.__calcH(self.startPos,self.goalPos)

#         self.openSetHash = {self.startPos}




#     def __calcH(self,startPos, goalPos ):
#         return abs (startPos[0] – goalPos[0]]) + abs (startPos[1] – goalPos[1]])


#     def __algo(self):
#         while not self.openSetHash.empty():
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()

#             self.current = self.openSet.get()[2]
#             self.openSetHash.remove(self.current)
#             if self.current == self.goalPos:
#                 return True
#             for neighbor in self.current.neighbors:
#                 self.tempGScore = self.gScore[self.current]+1

#                 if self.tempGScore < self.gScore[neighbor]:
#                     self.cameFrom = self.current
#                     self.gScore[neighbor] = self.tempGScore
#                     self.fScore[neighbor] = self.tempGScore + self.__calcH(self.startPos)
            
