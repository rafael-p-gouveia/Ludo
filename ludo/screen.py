import imp
import pygame
from ludo.const import BOARD_DIM, BOARD_IMG, BOARD_POS, FPS, WIN_DIM, WIN_NAME
import os

class Screen:
    def __init__(self):
        self._window = pygame.display.set_mode(WIN_DIM)
        self._board_img = pygame.image.load(os.path.join(BOARD_IMG)).convert()
        self._board_img = pygame.transform.smoothscale(self._board_img, BOARD_DIM)
        self._clk = pygame.time.Clock()
        pygame.display.set_caption(WIN_NAME)
    
    def update(self):
        self._clk.tick(FPS)
        self._window.blit(self._board_img, BOARD_POS)
        pygame.display.flip()



