import pygame

#all of the global variables used in the classes

WIDTH = 540
HEIGHT = 740
FPS = 30
TILESIZE = 62


# define color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTGREEN = (0,230,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (230,230,0)
CHAMPAGNEWHITE = (237, 221, 212)
GUNMETAL  = (40,61,59)
TEAL = (25,114,120)
LIGHTRED = (196,69,54)
LIVER = (119, 46, 37)
SILVER = (131,139,139)
ORANGE = (255,69,0)
DARKRED = (139,0,0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIGHT Quest!")

smallfont = pygame.font.SysFont("arial", 20)
mediumfont = pygame.font.SysFont("arial", 30)
largefont = pygame.font.SysFont("arial", 50)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# LOAD MENU GRAPHIC
logo = pygame.image.load('data/images/gamef.png').convert_alpha()
pic1 = pygame.image.load('data/images/char1.png').convert()
pic2 = pygame.image.load('data/images/char2.png').convert()
background = pygame.image.load('data/images/background.jpg')
background_main = pygame.transform.scale(background,(540,840))

BACK = pygame.image.load('data/images/back.png').convert()

damage_first = pygame.image.load('data/images/moves/damage_first.png').convert()
damage_second = pygame.image.load('data/images/moves/damage_second.png').convert()
damage_third = pygame.image.load('data/images/moves/damage_third.png').convert()
damage_ulti = pygame.image.load('data/images/moves/damage_ulti.png').convert()


elements = pygame.image.load('data/images/elements.png')
special = pygame.image.load('data/images/special.png')
moves = pygame.image.load('data/images/moves_desc.png')


#sprites on the grid
RED_G = pygame.image.load('data/images/red/red.png')
RED_G = pygame.transform.scale(RED_G,(58,56))
BLUE_G = pygame.image.load('data/images/blue/blue.png')
BLUE_G = pygame.transform.scale(BLUE_G,(56,56))
GREEN_G = pygame.image.load('data/images/green/green.png')
GREEN_G = pygame.transform.scale(GREEN_G,(56,56))
YELLOW_G = pygame.image.load('data/images/yellow/yellow.png')
YELLOW_G = pygame.transform.scale(YELLOW_G,(56,56))
HEART = pygame.image.load('data/images/like.png')
HEART = pygame.transform.scale(HEART,(56,56))
HIT = pygame.image.load('data/images/knockout.png')
HIT = pygame.transform.scale(HIT,(56,56))

#MOVES images
MOVE_1 = pygame.image.load('data/images/moves/move1.png')
MOVE_2 = pygame.image.load('data/images/moves/move2.png')
MOVE_3 = pygame.image.load('data/images/moves/move3.png')
MOVE_4 = pygame.image.load('data/images/moves/move4.png')


#sound
start_bell = pygame.mixer.Sound("data/sounds/start_bell.wav")
start_bell.set_volume(0.1)

first_sound = pygame.mixer.Sound("data/sounds/first.wav")
first_sound.set_volume(0.5)

second_sound = pygame.mixer.Sound("data/sounds/second.wav")
second_sound.set_volume(0.5)

third_sound = pygame.mixer.Sound("data/sounds/third.wav")
third_sound.set_volume(0.5)

ulti_sound = pygame.mixer.Sound("data/sounds/ulti.wav")

invalid_move = pygame.mixer.Sound("data/sounds/invalid_move.wav")
valid_move = pygame.mixer.Sound("data/sounds/valid_move.wav")

winning_sound = pygame.mixer.Sound("data/sounds/tada.wav")

#finish screen picture
FINISH1 = pygame.image.load('data/images/finish.png')
FINISH2 = pygame.image.load('data/images/finish2.png')
