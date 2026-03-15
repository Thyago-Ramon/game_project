import pygame

pygame.init()

# cria uma janela 640x480
screen = pygame.display.set_mode(size=(640, 480))
pygame.display.set_caption("Meu primeiro jogo")

# loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()