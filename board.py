from math import floor
from constants import BOARD_DIM, BOARD_IMG, BOARD_POS, TILE_SIZE
import pygame

from pawn import Pawn


class Board:
    def __init__(self):
        self.img = pygame.transform.smoothscale(
                    pygame.image.load(BOARD_IMG).convert_alpha(),
                    BOARD_DIM
                   )
    
    def draw(self, window):
        window.blit(self.img, BOARD_POS)
    
    def pos2tile(self, pos):
        x, y = pos
        row = y // TILE_SIZE
        col = x // TILE_SIZE
        return floor(row * 15 + col)
