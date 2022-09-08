from game import Game
from menu import Menu
import pygame



def main():
    pygame.init()
    game = Game()
    menu = Menu(game.getWindow(), game.getClock())
    menu.title_screen_run()
    config = menu.getConfig()
    game.setConfig(config)
    game.run()


if __name__ == "__main__":
    main()