import random
from constants import DICE_IMG, DICE_DIM, DICE_SIZE, DICE_COORDS, DICE_SPEED
import pygame
#pygame.init()


class Dice():
    def __init__(self):
        self.img = []
        for index in DICE_IMG.keys():
            self.img.append(pygame.transform.smoothscale(
                pygame.image.load(DICE_IMG[index]).convert_alpha(),
                DICE_DIM
                ))
        self.dice_surface = pygame.Rect(DICE_COORDS, DICE_DIM)
        self.cur_face = 0


    def draw(self, window):
        window.blit(self.img[self.cur_face], DICE_COORDS)
    
    def is_clicked(self, pos):
        return self.dice_surface.collidepoint(pos)
    
    def roll(self, window, clk, time):
        timer = 0
        while timer < time:
            timer += clk.get_time()
            self.cur_face = random.randint(0, 5)
            self.draw(window)
            pygame.display.flip()
        return self.cur_face + 1

