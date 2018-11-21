import pygame
from data.settings import *
from data.Classes.Table import t
from data.Classes.Table import P1
from data.Classes.Table import P2
from data.Classes.Table import players


class Image:
    """Class for creating an image, if there is color and no image, it is only a colored sprite"""
    def __init__(self, image, x, y, scale, color, action):
        if(image!=None):
            self.image = image
        else:
            self.image = pygame.Surface(scale)
        if(scale!=None):
            self.image = pygame.transform.scale(self.image, scale)
        if(color!=None):
            self.image.fill(color)
        self.width = x
        self.height = y
        self.image_rect = self.image.get_rect()
        self.scale = scale
        self.image_rect.topleft = (x,y)
        if(action!=None):
            self.action = action
            self.show()
        else:
            self.show()

    def show(self):
        screen.blit(self.image, self.image_rect)

    def imgbut(self, event):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.show()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # is left button clicked
                if(self.width + self.scale[0] > cursor[0] > self.width and self.height + self.scale[1] > cursor[1] >self.height):
                    if self.image_rect.collidepoint(event.pos):
                        if(t.player_turn == 0):
                            if(self.action == 'P1FirstP2'):
                                P1.useFirstMoveOnEnemy(P2)
                            elif(self.action == 'P1SecondP2'):
                                P1.useSecondMoveOnEnemy(P2)
                            elif(self.action == 'P1ThirdP2'):
                                P1.useThirdMoveOnEnemy(P2)
                            elif(self.action == 'P1UltiP2'):
                                P1.useUltiMoveOnEnemy(P2)
                        elif(t.player_turn == 1):
                            if(self.action == 'P2FirstP1'):
                                P2.useFirstMoveOnEnemy(P1)
                            elif(self.action == 'P2SecondP1'):
                                P2.useSecondMoveOnEnemy(P1)
                            elif(self.action == 'P2ThirdP1'):
                                P2.useThirdMoveOnEnemy(P1)
                            elif(self.action == 'P2UltiP1'):
                                P2.useUltiMoveOnEnemy(P1)
