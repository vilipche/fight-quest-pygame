import pygame
from  data.settings import *

class Cell(pygame.sprite.Sprite):
    """The class witch creates the sprites"""
    def __init__(self, input_sign, i, j,table,*groups):
        pygame.sprite.Sprite.__init__(self,*groups)
        self.image = self.findSign(input_sign)
        self.sign = input_sign
        self.rect = self.image.get_rect()
        self.i = i
        self.j = j
        self.table = table
        self.rect[0], self.rect[1] = self.i * (TILESIZE+2) + self.i+10, self.j * (TILESIZE+2) + self.j+10

    #function that gives the color of the sprite depending of the character of the element in the grid
    def findSign(self, input_sign):
        if (input_sign == '#'):
            return YELLOW_G
        if (input_sign == '@'):
            return GREEN_G
        if (input_sign == '$'):
            return RED_G
        if (input_sign == '%'):
            return BLUE_G
        if (input_sign == '!'):
            return HEART
        if (input_sign == '*'):
            return HIT
