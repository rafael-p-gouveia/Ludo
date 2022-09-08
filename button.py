import pygame
pygame.init()

class Button():
    def __init__(self, positionX, positionY, text, action = None, colorBg = 'Blue',
    colorTxt = 'White', font = pygame.font.Font(None, 40)):
        self.positionX = positionX
        self.positionY = positionY
        self.text = text
        self.action = action
        self.colorBg = colorBg
        self.colorTxt = colorTxt
        self.font = font

        self.text_surface = font.render(text, False, colorTxt)
        self.casing_surface = pygame.Rect((positionX,positionY), (100,65))
        self.inner_surface = pygame.Rect((positionX+3,positionY+3), (94,59))
        

    def printButton(self, screen):
        pygame.draw.rect(screen, (100,100,100), self.casing_surface)
        pygame.draw.rect(screen, self.colorBg, self.inner_surface)
        screen.blit(self.text_surface,(self.positionX+4,self.positionY+4))

    
    def hasBeenHovered(self, mouseCoordinates):
        if self.inner_surface.collidepoint(mouseCoordinates):
            return True
        else:
            return False
    
    #def doAction(self, parameters = None):
    #    self.action(parameters)