from board import Board
from constants import FPS, WIN_NAME, WIN_DIM
import pygame
from pawn import Pawn

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode(WIN_DIM)
        pygame.display.set_caption(WIN_NAME)
        self.board = Board()
        self.clk = pygame.time.Clock()
        self.running = True

    
    def run(self):
        while self.running:
            self.clk.tick(FPS)
            self.board.draw(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(self.board.pos2tile(pos))

        
    def getWindow(self):
            return self.window
        
    def getClock(self):
            return self.clk

