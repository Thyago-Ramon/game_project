#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./Assets/MenuBg.png")
        self.rect = self.surf.get_rect()

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load("./assets/Menu.mp3")
        pygame.mixer_music.play(-1)


        # CARREGA AS IMAGENS
        while True:

            self.window.blit(self.surf, dest=self.rect)
            self.menu_text(50, "MOUTAIN", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "SHOOTER", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))

                else:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # CHECA TODOS OS EVENTOS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # FECHA JANELA
                    quit() # ENCERRA PYGAME
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # TECLA P BAIXO
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #TECLA P CIMA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN: #TECLA ENTER
                        return MENU_OPTIONS[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def Operation1(self, ):
        pass
