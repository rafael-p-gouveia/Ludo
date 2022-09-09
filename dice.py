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


    def draw(self, window, n):
        window.blit(self.img[n], DICE_COORDS)

    def roll(self, window, clock):
        rolling = True
        n = 0
        while rolling:
            
            pressed = False
            mx,my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
            
            if self.dice_surface.collidepoint((mx,my)):
                if pressed:
                    n = random.randint(0,5)
                    self.draw(window, n)
                    return n
                    

            self.draw(window, n)
            pygame.display.flip()
            n += 1
            n %= 6
            clock.tick(DICE_SPEED)
