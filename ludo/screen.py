import imp
import pygame
from ludo.const import *
import os

class Screen:
    def update(self):
        self._clk.tick(FPS)
        self._window.blit(self._board, BOARD_POS)
        pygame.display.flip()

    def _load_img(self, path, dim):
        img = pygame.image.load(os.path.join(path)).convert()
        img = pygame.transform.smoothscale(img, dim)
        return img


    def __init__(self):
        self._window = pygame.display.set_mode(WIN_DIM)
        self._board = self._load_img(BOARD_PTH, BOARD_DIM)
        self._green = self._load_img(GREEN_PTH, TILE_DIM)
        self._yellow = self._load_img(YELLOW_PTH, TILE_DIM)
        self._red = self._load_img(RED_PTH, TILE_DIM)
        self._blue = self._load_img(BLUE_PTH, TILE_DIM)
        self._clk = pygame.time.Clock()
        pygame.display.set_caption(WIN_NAME)
    
        

