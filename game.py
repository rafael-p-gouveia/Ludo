from board import Board
from constants import FPS, GREEN, BLUE, YELLOW, RED, WIN_NAME, WIN_DIM
import pygame
from pawn import Pawn
from dice import Dice

#fduidfaiubuiasduidsafbiusdfudhiu

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
        self.running = True
        self.green_pawns[0].spawn()
        self.blue_pawns[2].spawn()
        
        while self.running:
            self.clk.tick(FPS)
            self.board.draw(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
<<<<<<< HEAD
            self.dice.roll(self.window, self.clk)

    def update(self):
        self.clk.tick(FPS)
        self.board.draw(self.window)
        for pawn in self.green_pawns:
            pawn.draw(self.window)
        for pawn in self.yellow_pawns:
            pawn.draw(self.window)
        for pawn in self.blue_pawns:
            pawn.draw(self.window)
        for pawn in self.red_pawns:
            pawn.draw(self.window)
        
        self.green_pawns[0].move(1)
        self.blue_pawns[2].move(1)
=======
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(self.board.pos2tile(pos))

>>>>>>> f1947ea794cb3f2f5a9b65d15538473bbd873048
        
    def getWindow(self):
            return self.window
        
    def getClock(self):
            return self.clk
    
    def setConfig(self,config):
        if len(config) > 0:
            self.nPlayers = config[0]
            self.isOnline = config [1]
            '''
            if self.isOnline:
                blablabla = config[2]
                blablabula = config[3]
            '''


