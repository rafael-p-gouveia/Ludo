from board import Board
from constants import FPS, GREEN, BLUE, WIN_NAME, WIN_DIM
import pygame
from pawn import Pawn

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode(WIN_DIM)
        pygame.display.set_caption(WIN_NAME)
        self.board = Board()
        self.clk = pygame.time.Clock()
        self.running = True
        self.green_pawns = [Pawn(GREEN, i - 4) for i in range(0, 4)]
        self.blue_pawns = [Pawn(BLUE, i - 12) for i in range(0, 4)]
    
    def run(self):
        self.green_pawns[0].spawn()
        self.blue_pawns[2].spawn()
        while self.running:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        self.clk.tick(FPS)
        self.board.draw(self.window)
        for pawn in self.green_pawns:
            pawn.draw(self.window)
        for pawn in self.blue_pawns:
            pawn.draw(self.window)
        self.green_pawns[0].move(1)
        self.blue_pawns[2].move(1)
        
        pygame.display.flip()

    def getWindow(self):
            return self.window
        
    def getClock(self):
            return self.clk

