from typing import final
import pygame
from settings import *

class Index:
    def __init__(self, alg_available):
        self.screen = pygame.display.get_surface()
        self.algorithm_menu_show = False
        self.alg_available = alg_available
        self.algorithm_bool = False
        self.close_menu = False
        self.save_bool = False
        self.load_bool = False
        self.reset_bool = False
        self.reinit_bool = False
        self.save_menu_show = False
        self.load_menu_show = False
        self.go_bool = False
        self.slot = 0

    def algorithm_button(self):
        buttonfont = pygame.font.SysFont('Arial',25)
        text = buttonfont.render("Cambiar algoritmo" , True , black)
        if self.algorithm_bool:
            pygame.draw.rect(self.screen, blue, [20, 20, 215, 40], border_radius=8)
        else:
            pygame.draw.rect(self.screen, grey, [20, 20, 215, 40],border_radius=8)
        pygame.draw.rect(self.screen, black, [20, 20, 215, 40],border_radius=8, width=2)
        self.screen.blit(text, (24, 25))

    def display_algorithm_menu(self, algorithm):
        x, y, longx, longy = HEIGTH / 4, WIDTH / 4, HEIGTH / 2, WIDTH / 2
        pygame.draw.rect(self.screen, grey_menu, [x, y, longx, longy], border_radius=10)
        pygame.draw.rect(self.screen, black, [x, y, longx, longy], border_radius=10, width=3)

        menufont = pygame.font.SysFont('Arial', 45)
        optionfont = pygame.font.SysFont('Arial', 25)
        self.screen.blit(menufont.render("Algoritmos disponibles", True , black), (x + 150, y + 20))
        start_options = y + 100
        for index, alg in enumerate(self.alg_available.keys()):
            margenx, margeny = x + 40, start_options + (30 + sep) * index
            pygame.draw.rect(self.screen, blue, [margenx, margeny, longx-100, 40], border_radius=10)
            self.screen.blit(optionfont.render(self.alg_available[alg], True, black), (margenx + 20, margeny + 6))
            if alg == algorithm:
                pygame.draw.rect(self.screen, green, [margenx, margeny, longx-100, 40], border_radius=10, width=2)
            else:
                pygame.draw.rect(self.screen, black, [margenx, margeny, longx-100, 40], border_radius=10, width=2)
        
        pygame.draw.rect(self.screen, purple, [longx-70, y + longy - 40, 90, 30], border_radius=3)
        pygame.draw.rect(self.screen, black, [longx-70, y + longy - 40, 90, 30], border_radius=3, width=2)
        self.screen.blit(optionfont.render("Cerrar", True , black), (longx-60, y + longy - 40))

    def current_algorithm(self, algorithm):
        buttonfont = pygame.font.SysFont('Arial',30)
        text = buttonfont.render('Algoritmo actual: ' + self.alg_available[algorithm], False, black)
        # pygame.draw.rect(self.screen, grey, [290, 20, 215, 40],border_radius=8)
        self.screen.blit(text, (280, 20))

    def info_panel(self):
        statfont = pygame.font.SysFont('Arial',22)
        timer = statfont.render('Tiempo: ', True, black)
        iters = statfont.render('Iteraciones: ', True, black)
        
        self.screen.blit(timer, (HEIGTH / 2 + 30, 10))
        self.screen.blit(iters, (HEIGTH / 2 + 30, 40))

    def draw_mode_index(self, mode):
        pygame.draw.rect(self.screen, green, [1100, 20, 15, 15], border_radius=8)
        pygame.draw.rect(self.screen, red, [1100, 45, 15, 15], border_radius=8)
        pygame.draw.rect(self.screen, black, [1200, 20, 15, 15], border_radius=8)
        pygame.draw.rect(self.screen, grey, [1200, 45, 15, 15], border_radius=8)


        if mode == 'start':
            pygame.draw.rect(self.screen, blue, [1100, 20, 15, 15], border_radius=8, width=2)
        else:
            pygame.draw.rect(self.screen, black, [1100, 20, 15, 15], border_radius=8, width=2)
        if mode == 'end':
            pygame.draw.rect(self.screen, blue, [1100, 45, 15, 15], border_radius=8, width=2)
        else:
            pygame.draw.rect(self.screen, black, [1100, 45, 15, 15], border_radius=8, width=2)
        if mode == 'wall':
            pygame.draw.rect(self.screen, blue, [1200, 20, 15, 15], border_radius=8, width=2)
        else:
            pygame.draw.rect(self.screen, black, [1200, 20, 15, 15], border_radius=8, width=2)
        if mode == 'erase':
            pygame.draw.rect(self.screen, blue, [1200, 45, 15, 15], border_radius=8, width=2)
        else:
            pygame.draw.rect(self.screen, black, [1200, 45, 15, 15], border_radius=8, width=2)

        statfont = pygame.font.SysFont('Arial',20)
        start = statfont.render('Inicio', True, black)
        end = statfont.render('Final', True, black)
        wall = statfont.render('Muro', True, black)
        erase = statfont.render('Borrar', True, black)

        self.screen.blit(start, (1130, 15))
        self.screen.blit(end, (1130, 40))
        self.screen.blit(wall, (1230, 15))
        self.screen.blit(erase, (1230, 40))

    def reset_button(self):
        buttonfont = pygame.font.SysFont('Arial', 15)
        text = buttonfont.render("Reset", True, black)
        if self.reset_bool:
            pygame.draw.rect(self.screen, blue, [1400, 20, 65, 20], border_radius=8)
        else:
            pygame.draw.rect(self.screen, grey, [1400, 20, 65, 20],border_radius=8)
        pygame.draw.rect(self.screen, black, [1400, 20, 65, 20],border_radius=8, width=2)
        self.screen.blit(text, (1410, 22))
    
    def save_button(self):
        buttonfont = pygame.font.SysFont('Arial', 15)
        text = buttonfont.render("Guardar", True, black)
        if self.save_bool:
            pygame.draw.rect(self.screen, blue, [1480, 20, 65, 20], border_radius=8)
        else:
            pygame.draw.rect(self.screen, grey, [1480, 20, 65, 20],border_radius=8)
        pygame.draw.rect(self.screen, black, [1480, 20, 65, 20],border_radius=8, width=2)
        self.screen.blit(text, (1485, 22))

    def reinit_button(self):
        buttonfont = pygame.font.SysFont('Arial', 15)
        text = buttonfont.render("Reiniciar", True, black)
        if self.reinit_bool:
            pygame.draw.rect(self.screen, blue, [1400, 50, 65, 20], border_radius=8)
        else:
            pygame.draw.rect(self.screen, grey, [1400, 50, 65, 20],border_radius=8)
        pygame.draw.rect(self.screen, black, [1400, 50, 65, 20],border_radius=8, width=2)
        self.screen.blit(text, (1405, 52))

    def load_button(self):
        buttonfont = pygame.font.SysFont('Arial', 15)
        text = buttonfont.render("Cargar", True, black)
        if self.load_bool:
            pygame.draw.rect(self.screen, blue, [1480, 50, 65, 20], border_radius=8)
        else:
            pygame.draw.rect(self.screen, grey, [1480, 50, 65, 20],border_radius=8)
        pygame.draw.rect(self.screen, black, [1480, 50, 65, 20],border_radius=8, width=2)
        self.screen.blit(text, (1490, 52))

    def save_menu(self):
        x, y, longx, longy = HEIGTH / 4, WIDTH / 4, HEIGTH / 2, WIDTH / 2
        pygame.draw.rect(self.screen, grey_menu, [x, y, longx, longy], border_radius=10)
        pygame.draw.rect(self.screen, black, [x, y, longx, longy], border_radius=10, width=3)

        menufont = pygame.font.SysFont('Arial', 45)
        optionfont = pygame.font.SysFont('Arial', 25)
        self.screen.blit(menufont.render("Guardar", True , black), (x + 150, y + 20))
        start_options = y + 100
        for index, slot in enumerate(['Slot 1', 'Slot 2', 'Slot 3', 'Slot 4', 'Slot 5', 'Slot 6']):
            margenx, margeny = x + 40, start_options + (30 + sep) * index
            pygame.draw.rect(self.screen, blue, [margenx, margeny, longx-100, 40], border_radius=10)
            self.screen.blit(optionfont.render(slot, True, black), (margenx + 20, margeny + 6))
            if self.slot == index:
                pygame.draw.rect(self.screen, green, [margenx, margeny, longx-100, 40], border_radius=10, width=2)
            else:
                pygame.draw.rect(self.screen, black, [margenx, margeny, longx-100, 40], border_radius=10, width=2)
        
        pygame.draw.rect(self.screen, purple, [longx-70, y + longy - 40, 130, 30], border_radius=3)
        pygame.draw.rect(self.screen, black, [longx-70, y + longy - 40, 130, 30], border_radius=3, width=2)
        self.screen.blit(optionfont.render("Confirmar", True , black), (longx-60, y + longy - 40))

    def load_menu(self):
        x, y, longx, longy = HEIGTH / 4, WIDTH / 4, HEIGTH / 2, WIDTH / 2
        pygame.draw.rect(self.screen, grey_menu, [x, y, longx, longy], border_radius=10)
        pygame.draw.rect(self.screen, black, [x, y, longx, longy], border_radius=10, width=3)

        menufont = pygame.font.SysFont('Arial', 45)
        optionfont = pygame.font.SysFont('Arial', 25)
        self.screen.blit(menufont.render("Cargar", True , black), (x + 150, y + 20))
        start_options = y + 100
        for index, slot in enumerate(['Slot 1', 'Slot 2', 'Slot 3', 'Slot 4', 'Slot 5', 'Slot 6']):
            margenx, margeny = x + 40, start_options + (30 + sep) * index
            pygame.draw.rect(self.screen, blue, [margenx, margeny, longx-100, 40], border_radius=10)
            self.screen.blit(optionfont.render(slot, True, black), (margenx + 20, margeny + 6))
            if self.slot == index:
                pygame.draw.rect(self.screen, green, [margenx, margeny, longx-100, 40], border_radius=10, width=2)
            else:
                pygame.draw.rect(self.screen, black, [margenx, margeny, longx-100, 40], border_radius=10, width=2)
        
        pygame.draw.rect(self.screen, purple, [longx-70, y + longy - 40, 130, 30], border_radius=3)
        pygame.draw.rect(self.screen, black, [longx-70, y + longy - 40, 130, 30], border_radius=3, width=2)
        self.screen.blit(optionfont.render("Confirmar", True , black), (longx-60, y + longy - 40))
    
    def start_button(self, ready):
        buttonfont = pygame.font.SysFont('Arial', 35)
        pausefont = pygame.font.SysFont('Arial', 25)
        if self.go_bool:
            pygame.draw.rect(self.screen, blue, [1320, 20, 65, 50], border_radius=8)
        else:
            pygame.draw.rect(self.screen, green, [1320, 20, 65, 50], border_radius=8)
        if ready:
            text = buttonfont.render("Go!", True, black)
            self.screen.blit(text, (1325, 22))
        else:
            text = pausefont.render("Stop", True, black)
            self.screen.blit(text, (1325, 27))
        pygame.draw.rect(self.screen, black, [1320, 20, 65, 50], border_radius=8, width=2)


    def draw_index(self, mode, algorithm, ready):
        self.algorithm_button()
        self.current_algorithm(algorithm)
        self.info_panel()
        self.draw_mode_index(mode)
        self.reset_button()
        self.reinit_button()
        self.save_button()
        self.load_button()
        self.start_button(ready)

        if self.algorithm_bool:
            self.algorithm_menu_show = True
        if self.close_menu:
            self.algorithm_menu_show = False
        if self.algorithm_menu_show:
            self.display_algorithm_menu(algorithm)
            return True
        if self.save_bool:
            self.save_menu_show = True
        if self.close_menu:
            self.save_menu_show = False
        if self.save_menu_show:
            self.save_menu()
            return True
        if self.load_bool:
            self.load_menu_show = True
        if self.close_menu:
            self.load_menu_show = False
        if self.load_menu_show:
            self.load_menu()
            return True
        return False

class Button:
    pass