import sys
import time
import pygame
from algorithms import A_star, dijskstra, bfs
from settings import *
import pandas as pd
from index import Index


class Aplication:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGTH, WIDTH))
        pygame.display.set_caption('Path finding')
        self.isRunning = True
        self.grid = Grid()
        self.CLOCK = pygame.time.Clock()    
        self.isPressed = False
        self.draw_mode = 'wall'
        self.ready = True
        self.first = True
        self.pause = False
        self.algorithm = 'dijkstra'
        self.algorithm_button = False
        self.menu = False
        self.alg_available = {'A_star': 'A*', 'dijkstra': 'Dijkstra', 'bfsr': 'BFS (Random mode)', 'bfs': 'BFS (Classic mode)'}
        self.index = Index(self.alg_available)
        self.pause = False
        
    def run(self):
        while self.isRunning:
            self.screen.fill(white_dirty)

            if not self.menu:
                self.close_menu = False
            self.event_manager()
            if self.ready:
                self.grid.change_cell(self.isPressed, self.draw_mode)
            else:
                if not self.pause:
                    if self.grid.end == None or self.grid.start == None:
                        self.ready = True
                        continue
                    elif self.first:
                        if self.algorithm == 'bfs':
                            self.solver = bfs.BFS(self.grid)
                        elif self.algorithm == 'dijkstra':
                            self.solver = dijskstra.Dijsktra(self.grid)
                        elif self.algorithm == 'A_star':
                            self.solver = A_star.AStar(self.grid)
                        elif self.algorithm == 'bfsr':
                            self.solver = bfs.BFS(self.grid, True)
                        self.first = False
                    
                    self.win = self.solver.run()
                    if self.win == True:
                        self.ready = True
                        if len(self.solver.path) == 0:
                            print('Non traceable path')
                        else:
                            self.grid.display_path(self.solver.path)

            self.grid.draw_grid()
            self.draw_cover()
            self.menu = self.index.draw_index(self.draw_mode, self.algorithm, self.ready)
            pygame.display.update()

    def draw_cover(self):
        for i in range(0, HEIGTH, SQUARE):
            pygame.draw.line(self.screen, black, (i, HEADER), (i, WIDTH), 1)
        for j in range(HEADER, WIDTH, SQUARE):
            pygame.draw.line(self.screen, black, (0, j), (HEIGTH, j), 1)

    def event_manager(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and not self.menu:
                    if event.key == pygame.K_w:
                        self.draw_mode = 'wall'
                    if event.key == pygame.K_s:
                        self.draw_mode = 'start'
                    if event.key == pygame.K_e:
                        self.draw_mode = 'end'
                    if event.key == pygame.K_d:
                        self.draw_mode = 'erase'
                    if event.key == pygame.K_SPACE:
                        self.ready = False
                    if event.key == pygame.K_RETURN:
                        self.grid.save_map()
                    if event.key == pygame.K_l:
                        self.grid.load_map()
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                    if event.key == pygame.K_r and self.win == True:
                        self.grid.soft_reset()
                        self.win = False
                        self.first = True
                    if event.key == pygame.K_1:
                        self.algorithm = 'A_star'
                    if event.key == pygame.K_2:
                        self.algorithm = 'dijkstra'
                    if event.key == pygame.K_3:
                        self.algorithm = 'bfs'
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.menu:
                        self.isPressed = True
                    pos = pygame.mouse.get_pos()

                    if pos[0] > 20 and pos[0] < 235 and pos[1] > 20 and pos[1] < 60 and not self.menu and self.ready:
                        self.index.algorithm_bool = True

                    if pos[0] > 1400 and pos[0] < 1465 and pos[1] > 20 and pos[1] < 40 and not self.menu:
                        self.index.reset_bool = True
                        self.grid.soft_reset()
                        self.solver.stop()
                        self.win = False
                        self.first = True
                        self.ready = True

                    if pos[0] > 1400 and pos[0] < 1465 and pos[1] > 50 and pos[1] < 70 and not self.menu:
                        self.index.reinit_bool = True
                        self.grid = Grid()
                        self.solver.stop()
                        self.win = False
                        self.first = True
                    if pos[0] > 1480 and pos[0] < 1545 and pos[1] > 20 and pos[1] < 40 and not self.menu:
                        self.index.save_bool = True

                    if pos[0] > 1480 and pos[0] < 1545 and pos[1] > 50 and pos[1] < 70 and not self.menu:
                        self.index.load_bool = True

                    if pos[0] > 1320 and pos[1] > 20 and pos[0] < 1385 and pos[1] < 70 and self.ready:
                        self.ready = False
                        self.index.go_bool = True
                    if pos[0] > 1320 and pos[1] > 20 and pos[0] < 1385 and pos[1] < 70 and not self.ready and not self.index.go_bool:
                        self.index.go_bool = True
                        self.pause = not self.pause
                        
                    x, y, longx, longy = HEIGTH / 4, WIDTH / 4, HEIGTH / 2, WIDTH / 2
                    if self.index.algorithm_menu_show:
                        for i, alg in enumerate(self.alg_available.keys()):
                            margenx, margeny = x + 40, y + 100 + (30 + sep) * i
                            if pos[0] > margenx and pos[0] < margenx + longx - 100 and pos[1] > margeny and pos[1] < margeny + 40 and self.menu:
                                self.algorithm = alg
                    if self.index.save_menu_show:
                        for i in range(6):
                            margenx, margeny = x + 40, y + 100 + (30 + sep) * i
                            if pos[0] > margenx and pos[0] < margenx + longx - 100 and pos[1] > margeny and pos[1] < margeny + 40 and self.menu:
                                self.index.slot = i
                    if self.index.load_menu_show:
                        for i in range(6):
                            margenx, margeny = x + 40, y + 100 + (30 + sep) * i
                            if pos[0] > margenx and pos[0] < margenx + longx - 100 and pos[1] > margeny and pos[1] < margeny + 40 and self.menu:
                                self.index.slot = i
                    
                    if pos[0] > longx-70 and pos[1] > y + longy - 40 and pos[0] < longx + 20 and pos[1] < y + longy - 10 and self.menu and self.index.algorithm_menu_show:
                        self.index.close_menu = True
                    if pos[0] > longx-70 and pos[1] > y + longy - 40 and pos[0] < longx + 60 and pos[1] < y + longy - 10 and self.menu and self.index.save_menu_show:
                        self.index.close_menu = True
                        self.grid.save_map(self.index.slot)
                    if pos[0] > longx-70 and pos[1] > y + longy - 40 and pos[0] < longx + 60 and pos[1] < y + longy - 10 and self.menu and self.index.load_menu_show:
                        self.index.close_menu = True
                        self.grid.load_map(self.index.slot)

                    if pos[0] > 1100 and pos[1] > 20 and pos[0] < 1115 and pos[1] < 35:
                        self.draw_mode = 'start'
                    if pos[0] > 1100 and pos[1] > 45 and pos[0] < 1115 and pos[1] < 60:
                        self.draw_mode = 'end'
                    if pos[0] > 1200 and pos[1] > 20 and pos[0] < 1215 and pos[1] < 35:
                        self.draw_mode = 'wall'
                    if pos[0] > 1200 and pos[1] > 45 and pos[0] < 1215 and pos[1] < 60:
                        self.draw_mode = 'erase'
                            
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.isPressed = False
                    self.index.algorithm_bool = False
                    self.index.save_bool = False
                    self.index.load_bool = False
                    self.index.reinit_bool = False
                    self.index.reset_bool = False
                    self.index.close_menu = False
                    self.index.go_bool = False


class Grid:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        cell_state = {}
        for i in range(0, HEIGTH, SQUARE):
            for j in range(HEADER, WIDTH, SQUARE):
                cell_state[(i, j)] = 0
        self.cell_state = cell_state
        self.start = None
        self.end = None
   
    def draw_grid(self):
        for i in range(0, HEIGTH, SQUARE):
            for j in range(HEADER, WIDTH, SQUARE):
                rect = pygame.Rect(i, j, SQUARE, SQUARE)
                if self.cell_state[(i, j)] == 0:
                    pygame.draw.rect(self.screen, grey, rect)
                elif self.cell_state[(i, j)] == 1:
                    pygame.draw.rect(self.screen, black, rect)
                elif self.cell_state[(i, j)] == 2 or self.cell_state[(i, j)] == 7:
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
            if y >= HEADER:
                if mode == 'wall':
                    self.cell_state[(x,y)] = 1
                elif mode == 'erase':
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
            self.cell_state[node] = 7

    def soft_reset(self):
        for i in range(0, HEIGTH, SQUARE):
            for j in range(HEADER, WIDTH, SQUARE):
                if self.cell_state[(i,j)] != 1:
                    self.cell_state[(i,j)] = 0
    
    def save_map(self, slot):
        data = pd.DataFrame(columns=['x', 'y', 'val'])
        row = 0
        for i in range(0, HEIGTH, SQUARE):
            for j in range(HEADER, WIDTH, SQUARE):
                data.loc[row, 'x'] = i
                data.loc[row, 'y'] = j
                if self.cell_state[(i,j)] != 1:
                    data.loc[row, 'val'] = 0
                else:
                    data.loc[row, 'val'] = 1
                row += 1
        file = 'maps/slot_{}.csv'.format(slot)
        data.to_csv(file, index = False)
    
    def load_map(self, slot):
        file = 'maps/slot_{}.csv'.format(slot)
        data = pd.read_csv(file)
        for i in range(len(data)):
            pos = (data.loc[i, 'x'], data.loc[i, 'y'])
            self.cell_state[pos] = data.loc[i, 'val']

    def update_grid(self, aug):
        amp = aug * 10
        global SQUARE
        print(int(WIDTH / SQUARE))

        SQUARE = SQUARE + amp
        new_alt = int(WIDTH / SQUARE)
        new_amp = int(HEIGTH / SQUARE)
        new_cell = {}
        for i in range(new_alt):
            for j in range(new_amp):
                if (i * (SQUARE-amp), j * (SQUARE-amp)) in self.cell_state.keys():
                    new_cell[(i * SQUARE, j * SQUARE)] = self.cell_state[(i * (SQUARE-amp), j * (SQUARE-amp))]
                else:
                    new_cell[(i * SQUARE, j * SQUARE)] = 0
        self.cell_state = new_cell

                

if __name__ == '__main__':
    app = Aplication()
    app.run()