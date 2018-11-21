from data.Classes.Attributes import Attributes
from data.Classes.Moves import Moves
from  data.settings import *


class Player:
    """Class for the player that plays the game and the opposing player"""
    def __init__(self, name, posX, posY):
        self.attributes = Attributes()
        self.moves = Moves()
        self.name = name
        self.health_color = WHITE
        self.posX = posX
        self.posY = posY

    #for the life bars
    def life_status(self):
        if self.attributes.health > 75:
            self.health_color = GREEN
        elif self.attributes.health > 50:
            self.health_color = YELLOW
        elif self.attributes.health > 25:
            self.health_color = ORANGE
        else:
            self.health_color = RED
        pygame.draw.rect(screen, self.health_color,(self.posX,self.posY,self.attributes.health,20))

    #using the moves(skills)
    def useFirstMoveOnEnemy(self, enemy):
        self.moves.activateFirst(self.attributes, enemy.attributes)
        self.status()
        enemy.status()

    def useSecondMoveOnEnemy(self, enemy):
        self.moves.activateSecond(self.attributes, enemy.attributes)
        self.status()
        enemy.status()

    def useThirdMoveOnEnemy(self, enemy):
        self.moves.activateThird(self.attributes, enemy.attributes)
        self.status()
        enemy.status()

    def useUltiMoveOnEnemy(self, enemy):
        self.moves.activateUlti(self.attributes, enemy.attributes)
        self.status()
        enemy.status()

    def status(self):
        print("Player: {}\nHealth: {}\nBlue: \t{}\nRed: \t{}\nYellow: {}\nGreen: \t{}".format(self.name, self.attributes.health, self.attributes.blue, self.attributes.red, self.attributes.yellow, self.attributes.green))
