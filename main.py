import sys
import time
import pygame
from A_star import AStar
from settings import *

class Aplication:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGTH, WIDTH))
        pygame.display.set_caption('Path finding')
        self.isRunning = True
        self.grid = Grid()
        self.CLOCK = pygame.time.Clock()
    def run(self):
        isPressed = False
        draw_mode = 'wall'
        ready = True
        first = True
        i = 0
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        draw_mode = 'wall'
                    if event.key == pygame.K_s:
                        draw_mode = 'start'
                    if event.key == pygame.K_e:
                        draw_mode = 'end'
                    if event.key == pygame.K_d:
                        draw_mode = 'erase'
                    if event.key == pygame.K_SPACE:
                        ready = False
                    if event.key == pygame.K_p and ready == False:
                        ready = not ready
                    if event.key == pygame.K_r and win == True:
                        self.grid = Grid()
                        win = False
                        first = True
                elif event.type == pygame.MOUSEWHEEL:
                    self.grid.update_grid()
                #     global SQUARE
                #     print(event.y)
                #     SQUARE = SQUARE + event.y * 5
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    isPressed = False
            if ready:
           
                self.grid.change_cell(isPressed, draw_mode)
                self.screen.fill(grey)
            
            else:
                if self.grid.end == None or self.grid.start == None:
                    ready = True
                    continue
                elif first:
                    self.solver = AStar(self.grid)
                    first = False
                i += 1
                win = self.solver.run()
                time.sleep(0.01)
                if win == True:
                    ready = True
                    if len(self.solver.path) == 0:
                        print('Non traceable path')
                    else:
                        self.grid.display_path(self.solver.path)


            self.grid.draw_grid()
            self.draw_cover()
            pygame.display.update()

    def draw_cover(self):
        for i in range(0, WIDTH, SQUARE):
            pygame.draw.line(self.screen, black, (i, 0), (i, HEIGTH), 1)
        for j in range(0, HEIGTH, SQUARE):
            pygame.draw.line(self.screen, black, (0, j), (WIDTH, j), 1)

class Grid:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        cell_state = {}
        for i in range(0, WIDTH, SQUARE):
            for j in range(0, HEIGTH, SQUARE):
                cell_state[(i, j)] = 0
        self.cell_state = cell_state
        self.start = None
        self.end = None
   
    def draw_grid(self):
        for i in range(0, WIDTH, SQUARE):
            for j in range(0, HEIGTH, SQUARE):
                rect = pygame.Rect(i, j, SQUARE, SQUARE)
                if self.cell_state[(i, j)] == 0:
                    pygame.draw.rect(self.screen, grey, rect)
                elif self.cell_state[(i, j)] == 1:
                    pygame.draw.rect(self.screen, black, rect)
                elif self.cell_state[(i, j)] == 2:
                    pygame.draw.rect(self.screen, green, rect)
                elif self.cell_state[(i,j)] == 3:
                    pygame.draw.rect(self.screen, red, rect)
                elif self.cell_state[(i,j)] == 4:
                    pygame.draw.rect(self.screen, blue, rect)
                elif self.cell_state[(i,j)] == 5:
                    pygame.draw.rect(self.screen, purple, rect)
                elif self.cell_state[(i,j)] == 6:
                    pygame.draw.rect(self.screen, maroon, rect)

    def change_cell(self, isPressed, mode):
        if isPressed == False:
            pass
        else:
            pos = pygame.mouse.get_pos()
            x = (pos[0] // SQUARE) * SQUARE
            y = (pos[1] // SQUARE) * SQUARE
            if mode == 'wall':
                self.cell_state[(x,y)] = 1

            if mode == 'erase':
                self.cell_state[(x,y)] = 0
                
            elif mode == 'start':
                for index in self.cell_state.keys():
                    if self.cell_state[index] == 2:
                        self.cell_state[index] = 0
                self.cell_state[(x,y)] = 2
                self.start = (x,y)

            elif mode == 'end':
                for index in self.cell_state.keys():
                    if self.cell_state[index] == 3:
                        self.cell_state[index] = 0
                self.cell_state[(x,y)] = 3
                self.end = (x,y)

    def display_path(self, path):
        for node in path:
            self.cell_state[node] = 2

# class Film:
#     def __init__(self, screen):
#         pygame.camera.init()
#         self.cam = pygame.camera.Camera('/dev/video', )


if __name__ == '__main__':
    app = Aplication()
    app.run()