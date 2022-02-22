import pygame
import time
import random
import math
 
from pygame.locals import *
from pygame.time import Clock
from pygame.color import THECOLORS
pygame.init()

class Game:

	def __init__(self, size, grid):
		self.grid = grid
		self.clock = Clock()
		self.done = False
		self.FPS = 30
		self.screen = pygame.display.set_mode(size)
		self.screen.fill(THECOLORS["black"])


	def printscreen(self):
		date = time.gmtime()
		fileName =  "screenshot_" + \
				str(date[0]) + '-' + \
				str(date[1]) + '-' + \
				str(date[2]) + '-' + \
				str(date[3]-8) + '-' + \
				str(date[4]) + '-' + \
				str(date[5]) + \
				'.jpg'

		pygame.image.save(self.screen, fileName)

	def update(self):
		event = pygame.event.get()
	 
		for e in event:
			if(e.type == QUIT):
				self.done = True
	 
			elif(e.type == KEYDOWN):
	 
				if(e.key == K_p):
					self.printscreen()

				if(e.key == K_q):
					self.done = True



	def draw(self):
		self.clock.tick(self.FPS)
		self.screen.fill(THECOLORS["black"]) 
		self.grid.draw(self.screen)
		pygame.display.flip()

class Cell:
	
	def __init__(self, pos, size, color=THECOLORS["black"]):
		self.color = color
		self.box = pygame.Rect(pos, size)

	def setColor(self, color):
		self.color = color

	def draw(self, screen):
		pygame.draw.rect(screen, THECOLORS["white"], self.box, 1)
		pygame.draw.rect(screen, self.color, self.box)

class Grid:
	
	def __init__(self, gridSize, cellSize, pos=(0,0)):
		self.pos = pos	
		self.cells = {}
		for x in range(gridSize[0]):
			for y in range(gridSize[1]):
				p = (x * cellSize[0], y * cellSize[1])
				self.cells[(x, y)] = Cell(p, cellSize)

	def setCell(self, pos, color):
		self.cells[pos].setColor(color)

	def draw(self, screen):
		for cell in self.cells.values():
			cell.draw(screen)

if __name__ == "__main__":
	
	size = (640, 480)
	gridSize = (20, 30)
	cellSize = (size[0] / gridSize[0], size[1] / gridSize[1])
	grid = Grid(gridSize, cellSize)
	game = Game(size, grid)

	counter = 0

	while(not game.done):
		game.update()
		game.draw()

		color = (0,0,0) # random.choice(THECOLORS.values())
		pos = (counter % gridSize[0], counter/gridSize[0] % gridSize[1])
		grid.setCell(pos, color)		
		counter += 1