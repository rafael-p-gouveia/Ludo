import imp
from operator import imod
import pygame
from ludo.const import WIN_DIM, WIN_NAME, FPS
from ludo.screen import Screen

class Application:
    def __init__(self):
        self._screen = Screen()
        self._running = True

    def run(self):
        screen  = self._screen
        running = self._running
        while running:
            screen.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()



