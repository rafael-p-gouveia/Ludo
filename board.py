from constants import BOARD_DIM, BOARD_IMG, BOARD_POS
import pygame


class Board:
    def __init__(self):
        self.img = pygame.transform.smoothscale(
                    pygame.image.load(BOARD_IMG).convert_alpha(),
                    BOARD_DIM
                   )
    
    def draw(self, window):
        window.blit(self.img, BOARD_POS)