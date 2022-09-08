from math import floor
from constants import BLUE, BOARD_DIM, BOARD_IMG, BOARD_POS, GREEN, RED, TILE_SIZE, YELLOW
import pygame

from pawn import Pawn


class Board:
    def __init__(self):
        self.img = pygame.transform.smoothscale(
                    pygame.image.load(BOARD_IMG).convert_alpha(),
                    BOARD_DIM
                   )
        self.pieces = [[],[],[],[]]
        self.pieces[BLUE] = [Pawn(BLUE, i - 12) for i in range(0, 4)]
        self.pieces[RED] = [Pawn(RED, i - 16) for i in range(0, 4)]
        self.pieces[GREEN] = [Pawn(GREEN, i - 4) for i in range(0, 4)]
        self.pieces[YELLOW] = [Pawn(YELLOW, i - 8) for i in range(0, 4)]

    
    def draw(self, window):
        window.blit(self.img, BOARD_POS)
        for pawn_set in self.pieces:
            for pawn in pawn_set:
                pawn.draw(window)
        pygame.display.flip()

    
    def pos2tile(self, pos):
        x, y = pos
        row = y // TILE_SIZE
        col = x // TILE_SIZE
        return floor(row * 15 + col)
