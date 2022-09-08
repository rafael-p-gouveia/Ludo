import os
# Window Data
WIN_DIM  = WIDTH, HEIGHT = (510, 510)
WIN_HEIGHT = HEIGHT
WIN_WIDTH = WIDTH
WIN_NAME = "L U D O !"
FPS      = 60

########################################################################

# Board Data

BOARD_POS = (0, 0)
BOARD_DIM = WIN_DIM

NUM_TILES = 15
TILE_DIM  = BOARD_DIM[0] / NUM_TILES, BOARD_DIM[1] / NUM_TILES
TILE_SIZE = TILE_DIM[0]

BOARD_IMG   = "img/board.png"

########################################################################

# Dice Data

DICE_DIM = TILE_DIM
DICE_SIZE = DICE_DIM[0]

DICE_COORDS = (BOARD_POS[0] + BOARD_DIM[0]/2 - DICE_DIM[0]/2, BOARD_POS[1] + BOARD_DIM[1]/2 - DICE_DIM[1]/2)
DICE_SPEED = 18

DICE_IMG = {
    1 : os.path.join('img/dice_1.png'),
    2 : os.path.join('img/dice_2.png'),
    3 : os.path.join('img/dice_3.png'),
    4 : os.path.join('img/dice_4.png'),
    5 : os.path.join('img/dice_5.png'),
    6 : os.path.join('img/dice_6.png')
}

########################################################################

# Pawn Data

BLUE   = 1
RED    = 2
YELLOW = 4
GREEN  = 8

PAWN_IMG = {
    BLUE  : os.path.join("img/blue_p.png"),
    RED   : os.path.join("img/red_p.png"),
    YELLOW: os.path.join("img/yellow_p.png"),
    GREEN : os.path.join("img/green_p.png")
}

# Pawn paths
PAWN_PATH = {
    BLUE : [
        133, 132, 131, 130, 129, 143, 158, 173, 188, 203, 218, 217, 216,
        201, 186, 171, 156, 141, 125, 124, 123, 122, 121, 120, 105, 90,
        91, 92, 93, 94, 95, 81, 66, 51, 36, 21, 6, 7, 8, 23, 38, 53, 68,
        83, 99, 100, 101, 102, 103, 104, 119, 118, 117, 116, 115, 114, 113],

    RED : [
        201, 186, 171, 156, 141, 125, 124, 123, 122, 121, 120, 105, 90,
        91, 92, 93, 94, 95, 81, 66, 51, 36, 21, 6, 7, 8, 23, 38, 53, 68,
        83, 99, 100, 101, 102, 103, 104, 119, 134, 133, 132, 131, 130, 129,
        143, 158, 173, 188, 203, 218, 217, 202, 187, 172, 157, 142, 127],

    YELLOW : [
        23, 38, 53, 68, 83, 99, 100, 101, 102, 103, 104, 119, 134, 133,
        132, 131, 130, 129, 143, 158, 173, 188, 203, 218, 217, 216, 201,
        186, 171, 156, 141, 125, 124, 123, 122, 121, 120, 105, 90, 91, 92,
        93, 94, 95, 81, 66, 51, 36, 21, 6, 7, 22, 37, 52, 67, 82, 97],

    GREEN : [
        91, 92, 93, 94, 95, 81, 66, 51, 36, 21, 6, 7, 8, 23, 38, 53, 68, 83,
        99, 100, 101, 102, 103, 104, 119, 134, 133, 132, 131, 130, 129, 143,
        158, 173, 188, 203, 218, 217, 216, 201, 186, 171, 156, 141, 125, 124,
        123, 122, 121, 120, 105, 106, 107, 108, 109, 110, 111]
    }


# Pawn houses, they don't align perfectly the same way the tiles do, so their
# position on screen was hard coded
SPAWN_IDX2POS  = {
    -1: (55, 55),   # Green
    -2: (117, 55),
    -3: (55, 117),
    -4: (117, 117),
    -5: (360, 55),  # Yellow
    -6: (422, 55),
    -7: (55, 422),
    -8: (422, 422),
    -9: (360, 359), # Blue
   -10: (422, 359),
   -11: (360, 421),
   -12: (422, 421),
   -13: (55, 359),  # Red
   -14: (117, 359),
   -15: (55, 421),
   -16: (117, 421)
}

# Cood of imune tiles, when staying over it the pawn is imune
IMUNE_TILES = [36, 102, 188, 122]
