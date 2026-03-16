#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()

        # cria uma janela com dimensões do arquivo Const.
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Meu primeiro jogo")

    def run(self, ):
        while True:
            menu=Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()
                quit()

            else:
                pass






