import pygame
from data.Classes.Cell import *

class Button:
    """Class for creating a button, the actions when clicked are in the functions dictionary in the main"""
    def __init__(self, msg, x, y, width, height, textX, textY, textcolor, inactive_color, active_color,  size,list_func, action): #"controls"
        pygame.sprite.Sprite.__init__(self)
        self.msg = msg
        self.x = x - height
        self.y = y
        self.width = width
        self.height = height
        self.textX = self.x + textX
        self.textY = self.y + textY
        self.textcolor = textcolor
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action #none
        self.size = size
        self.functions = list_func
        self.button()



    def button(self):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        functions = self.functions
        if(self.x + self.width > cursor[0] > self.x and self.y + self.height > cursor[1] > self.y):
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))
            if(click[0] == 1 and self.action != None):
                if(self.action in self.functions):
                    self.functions[self.action]()
        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))
        self.text_to_button()


    def text_to_button(self):
        textSurface, textRect = self.text_objects()
        textRect.center = (self.textX, self.textY)
        screen.blit(textSurface, textRect)


    def text_objects(self):
        if (self.size == "small"):
            textSurface = smallfont.render(self.msg, True, self.textcolor)
        if (self.size == "medium"):
            textSurface = mediumfont.render(self.msg, True, self.textcolor)
        if (self.size == "large"):
            textSurface = largefont.render(self.msg, True, self.textcolor)
        return textSurface, textSurface.get_rect()
