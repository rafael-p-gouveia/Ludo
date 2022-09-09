from time import sleep
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
        self.clk = pygame.time.Clock()
        
        self.board = Board()
        self.dice = Dice()
        self.pieces = [[],[],[],[]]

        self.pieces[BLUE] = [Pawn(BLUE, i - 12) for i in range(0, 4)]
        self.pieces[RED] = [Pawn(RED, i - 16) for i in range(0, 4)]
        self.pieces[GREEN] = [Pawn(GREEN, i - 4) for i in range(0, 4)]
        self.pieces[YELLOW] = [Pawn(YELLOW, i - 8) for i in range(0, 4)]

        self.turn = BLUE
        self.running = False
    
    def run(self):
        self.running = True
        
        while self.running:
            self.clk.tick(FPS)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO check if its the turn of whoever is clicking
                    pos = pygame.mouse.get_pos()
                    if self.dice.is_clicked(pos):
                        self.on_dice_click()
                        pass
                    for pawn in self.pieces[self.turn]:
                        if pawn.is_clicked(pos):
                            self.on_pawn_click(pawn)
                    
                    print(self.board.pos2tile(pos))

    def on_dice_click(self):
        self.dice.roll(self.window, self.clk, 2000)
        pass
        
    def on_pawn_click(self, pawn):
        pass

    
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

    def draw(self):
        self.board.draw(self.window)
        for pawn_set in self.pieces:
            for pawn in pawn_set:
                pawn.draw(self.window)
        self.dice.draw(self.window)
        pygame.display.flip()


