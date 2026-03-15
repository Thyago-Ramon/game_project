#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()

        # cria uma janela 640x480
        self.window = pygame.display.set_mode(size=(640, 480))
        pygame.display.set_caption("Meu primeiro jogo")

    def run(self, ):
        running = True
        while running:
            menu=Menu(self.window)
            menu.run()


        # loop principal

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


