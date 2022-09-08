from constants import NUM_TILES, PAWN_IMG, PAWN_PATH, SPAWN_IDX2POS, TILE_DIM, TILE_SIZE
from math import floor
import pygame

class Pawn:
    def draw(self, window):
        window.blit(self.img, self._tile2winpos())

    def move(self, n):
        if self.idx >= self.final_idx:
            return
        if self.idx + n >= self.final_idx:
            self.idx = self.final_idx
            self.final_idx -= 1
        else:
            self.idx += n

    def kill(self):
        self.idx = self.spawn_idx

    def spawn(self):
        self.idx = 0
        
    def __init__(self, color, spawn_idx) -> None:
        self.color = color
        self.spawn_idx = spawn_idx
        self.idx = spawn_idx
        self.final_idx = len(PAWN_PATH[color]) - 1
        self.img = pygame.transform.smoothscale(
                    pygame.image.load(PAWN_IMG[self.color]).convert_alpha(),
                    TILE_DIM
                   )

    def _tile2winpos(self):
        if self.idx < 0:
            return SPAWN_IDX2POS[self.idx]
        tile = PAWN_PATH[self.color][self.idx]
        return (tile % NUM_TILES * TILE_SIZE, floor(tile / NUM_TILES) * TILE_SIZE)

        