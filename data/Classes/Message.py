import pygame
from data.settings import *


class Message:
    """Class for creating a message to appear on screen"""
    def __init__(self, msg, color, moveX, moveY, size):
        self.msg = msg
        self.color = color
        self.moveX = moveX
        self.moveY = moveY
        self.size = size
        self.message()

    def message(self):
        textSurface, textRect = self.text_objects()
        textRect.center = (WIDTH / 2) + self.moveX, (HEIGHT / 2) + self.moveY
        screen.blit(textSurface, textRect)


    def text_objects(self):
        if (self.size == "small"):
            textSurface = smallfont.render(self.msg, True, self.color)
        if (self.size == "medium"):
            textSurface = mediumfont.render(self.msg, True, self.color)
        if (self.size == "large"):
            textSurface = largefont.render(self.msg, True, self.color)
        return textSurface, textSurface.get_rect()
