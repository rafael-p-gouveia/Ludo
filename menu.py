import pygame
pygame.init()
from button import Button
from constants import WIN_HEIGHT, WIN_WIDTH, FPS
from sys import exit

class Menu():
    def __init__(self,window, clock):
        self.window = window
        self.clock = clock
        self.config = []
        self.menu_font = pygame.font.Font(None, 40)
        self.running = False
    
    #def screen_online_config_run():
    
    def screen_online_offline_run(self, nPlayers):
        text_on_off = self.menu_font.render('Select mode', False, 'Blue')

        if nPlayers > 1:
            colorTxt = 'White'
            colorBg = 'Blue'
        else:
            colorTxt = 'gray70'
            colorBg = 'gray50'

        button_online = Button(WIN_WIDTH/2 - 50, WIN_HEIGHT/2,'Online', colorBg = colorBg, colorTxt = colorTxt)
        button_offline = Button(WIN_WIDTH/2 - 50, WIN_HEIGHT/2 + 65, 'Offline')
        button_back = Button(WIN_WIDTH/2 - 50, WIN_HEIGHT/2 + 130, 'BACK', colorBg = 'Red')

        while self.running:
            pressed = False
            mx,my = pygame.mouse.get_pos()
            self.window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
    
            button_online.printButton(self.window)
            if button_online.hasBeenHovered((mx,my)):
                if pressed:
                    if nPlayers > 1:
                        self.config = [nPlayers,True]
                        #self.screen_online_config_run()
                        print('online')

            button_offline.printButton(self.window)
            if button_offline.hasBeenHovered((mx,my)):
                if pressed:
                    self.config = [nPlayers, False]
                    self.running = False
                    print('offline')

            button_back.printButton(self.window)
            if button_back.hasBeenHovered((mx,my)):
                if pressed:
                    return

            self.window.blit(text_on_off,(WIN_WIDTH/2 - 70, 20))
            pygame.display.update()
            self.clock.tick(FPS)
    
    def screen_num_players_run(self):
        text_num_player = self.menu_font.render('How many players?', False, 'Blue')
    
        buttons = {'4':Button(WIN_WIDTH/2 - 100, WIN_HEIGHT/2,'4'),'3':Button(WIN_WIDTH/2, WIN_HEIGHT/2,'3'),
        '2':Button(WIN_WIDTH/2 - 100, WIN_HEIGHT/2 + 65,'2'), '1':Button(WIN_WIDTH/2, WIN_HEIGHT/2 + 65,'1'),
        'BACK':Button(WIN_WIDTH/2 - 50, WIN_HEIGHT/2 + 130, 'BACK', colorBg = 'Red')}
        
        while self.running:
            pressed = False
            mx,my = pygame.mouse.get_pos()
            self.window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
            
            for key in buttons.keys():
                buttons[key].printButton(self.window);
                if buttons[key].hasBeenHovered((mx,my)) and pressed:
                    if key == 'BACK':
                        return
                    else:
                        return self.screen_online_offline_run(int(key))

            self.window.blit(text_num_player,(WIN_WIDTH/2 - 140, 20))
            pygame.display.update()
            self.clock.tick(FPS)
    
    def title_screen_run(self):
        self.running = True
        text_title = self.menu_font.render('L U D O !', False , 'Blue')

        while self.running:
            pressed = False
            mx,my = pygame.mouse.get_pos()
            self.window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True

            button_play = Button(WIN_WIDTH/2 - 45, WIN_WIDTH/2 + 15, 'PLAY', colorBg = 'Green')
            button_back = Button(WIN_WIDTH/2 - 45, WIN_WIDTH/2 + 80, 'QUIT', colorBg = 'Red')

            #blablabla
            button_play.printButton(self.window)
            if button_play.hasBeenHovered((mx,my)):
                if pressed:
                    self.screen_num_players_run()
                    if not self.running:
                        break

            button_back.printButton(self.window)
            if button_back.hasBeenHovered((mx,my)):
                if pressed:
                    pygame.quit()
                    exit()
            
            self.window.blit(text_title,(WIN_WIDTH/2 - 70, 20))
            pygame.display.update()
            self.clock.tick(FPS)
    
    def getConfig(self):
        return self.config


