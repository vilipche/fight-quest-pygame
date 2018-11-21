import random
import copy
import pygame
from data.Classes.Cell import *
from  data.settings import *
from data.Classes.Player import Player

#the players
P1 = Player("player1",WIDTH/2-5*50,680)
P2 = Player("player2",WIDTH/2+3*50,680)
players = [P1,P2]

class Table:
    """The table that the player will interact with"""
    def __init__(self, row, column):
        self.sizeRow = row
        self.sizeColumn = column
        self.tiles = ['#', '@', '$', '%','!','*']
        self.grille = []
        self.tilesGrille()
        self.checkNotThree()
        self.selected_tiles = []
        self.cells = [] #sprites
        self.createCells()
        self.pos = []
        self.marked = []
        self.hasMatch = False
        self.player_turn = 0

    #function of the creation of the sprites
    def createCells(self):
        self.cells = [[Cell(self.grille[x][y], y, x, self.grille, all_sprites) for y in range(8)] for x in range(8)]

    #function for creating the grid (grid with all zeros)
    def creeGrille(self):
        self.grille = []
        for i in range(self.sizeRow):
            ligne = [0] * self.sizeColumn
            self.grille.append(ligne)
        return self.grille

    #function that replaces the zeros from the previoisly created grid with a random element from the list tiles
    def tilesGrille(self):
        self.grille = self.creeGrille()
        for i in range(self.sizeRow):
            for j in range(self.sizeColumn):
                self.grille[i][j] = random.choice(self.tiles)
        return self.grille

    # function that takes an element from the list and recreates the list without that element
    def replaceTiles(self, liste, tile):
        liste = self.tiles.copy()
        for i in liste:
            if i == tile:
                liste.remove(i)
        return liste

    '''the functions from 1 to 4 are functions which check if in the first grid, that is created before any switching by the user,
    has a match of elements .They generate a grid without any matches. '''

    #1
    def checkRow(self):
        for i in range(self.sizeRow):
            for j in range(self.sizeColumn - 2):
                if (self.grille[i][j] == self.grille[i][j + 1] == self.grille[i][j + 2]):
                    t = copy.copy(self.tiles)  # makes a copy of tiles list
                    c = self.replaceTiles(t, self.grille[i][j + 2])
                    self.grille[i][j + 2] = random.choice(c)  # adds randomly the element to the last of the 3
        return self.grille
    #2
    def checkColumn(self):
        for i in range(self.sizeRow - 2):
            for j in range(self.sizeColumn):
                if (self.grille[i][j] == self.grille[i + 1][j] == self.grille[i + 2][j]):
                    t = copy.copy(self.tiles)
                    c = self.replaceTiles(t, self.grille[i + 2][j])
                    self.grille[i + 2][j] = random.choice(c)
        return self.grille
    #3
    def testCheck(self, c):
        g = copy.deepcopy(self.grille)
        row = self.checkRow()
        r = copy.deepcopy(row)
        column = self.checkColumn()
        c = copy.deepcopy(column)
        return c
    #4
    def checkNotThree(self):
        c = copy.deepcopy(self.grille)
        r = self.testCheck(c)
        i = 0
        while (r != c):
            c = copy.deepcopy(r)
            r = self.testCheck(c)
        self.grille = copy.deepcopy(c)
        return self.grille


    #function for dispalying the grid (not the sprites on the screen)
    def affiche(self):
        for i in range(self.sizeRow):
            for j in range(self.sizeColumn):
                print(self.grille[i][j] + " ", end='')
            print("\n")


    #function that check if there is a match in a row (this function it's used after the user does the switching of elements)
    #it creates a list of the positions of the matching elements of the grid
    def threeMatriceRow(self):
        match = False
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])-1):
                if(match == False):
                    if(self.grille[i][j] == self.grille[i][j+1]):
                        match = True
                        first = True
                elif(self.grille[i][j] == self.grille[i][j+1]):
                    if(first == True):
                        self.marked.append((i,j-1))
                        self.marked.append((i,j))
                        self.marked.append((i,j+1))
                        first = False
                    else:
                        self.marked.append((i,j+1))
                else:
                    match = False
            match = False

    #function that check if there is a match in a column (this function it's used after the user does the switching of elements)
    #it creates a list of the positions of the matching elements of the grid (this is the same list as the list from the function threeMatriceRow()
    def threeMatriceColumn(self):
        match = False
        for j in range(len(self.grille[0])):
            for i in range(len(self.grille)-1):
                if(match == False):
                    if(self.grille[i][j] == self.grille[i+1][j]):
                        match = True
                        first = True
                elif(self.grille[i][j] == self.grille[i+1][j]):
                    if(first == True):
                        self.marked.append((i-1,j))
                        self.marked.append((i,j))
                        self.marked.append((i+1,j))
                        first = False
                    else:
                        self.marked.append((i+1,j))
                else:
                    match = False
            match = False


    #function that checks if length of the previoisly created list of the positions of matching elements is bigger than 0
    #if it is, there is a match
    def setMarked(self):
        self.threeMatriceRow()
        self.threeMatriceColumn()
        self.marked = list(set(self.marked))
        if(len(self.marked) > 0):
            print("we have a match!")
            self.hasMatch = True
            self.add_points()
        else:
            print("no match")
            self.hasMatch = False


    def playSound(self):
        if(self.hasMatch):
            valid_move.play()
        else:
            invalid_move.play()

    #function that replaces all the matching elements with 0, it also switches the sign of the sprite and the color coresponding to the sign 0 (BLACK)
    def removeMarked(self):
        if(self.hasMatch):
            for i in range(len(self.marked)):
                prvo = self.marked[i][0]
                vtoro = self.marked[i][1]
                self.grille[prvo][vtoro] = '0'
                self.cells[prvo][vtoro].sign = self.grille[prvo][vtoro]


            self.marked = []

    #function that does the change of elements from the grid/the sprites
    def change(self,pos,element1,element2):
                #firstly the grid is being changed
                self.grille[pos[0][0]][pos[0][1]], self.grille[pos[1][0]][pos[1][1]] = self.grille[pos[1][0]][pos[1][1]], self.grille[pos[0][0]][pos[0][1]]
                self.setMarked()#the function for checking if there is a match is called here, so that if there is no match the elements in the grid would return at their places
                if(self.hasMatch):
                    #changing the grid in the sprite
                    element1.i, element1.j, element2.i, element2.j = element2.i, element2.j, element1.i, element1.j

                    #changing the sprites as rects
                    element1.rect.center,element2.rect.center = element2.rect.center,element1.rect.center

                    #changing the sprites as elements
                    q = self.cells[pos[0][0]][pos[0][1]]
                    self.cells[pos[0][0]][pos[0][1]] = self.cells[pos[1][0]][pos[1][1]]
                    self.cells[pos[1][0]][pos[1][1]] = q

                else:
                   self.grille[pos[1][0]][pos[1][1]], self.grille[pos[0][0]][pos[0][1]] = self.grille[pos[0][0]][pos[0][1]], self.grille[pos[1][0]][pos[1][1]]



    #function that does the check if the elemnts we want to switch are adjusted (they are in a same row/column)
    def check_states(self,sprite,a,b):
        self.selected_tiles.append(sprite)
        #a list of spites is created so that the check can be made after the second click of an element of the grid
        #(if the length of the list is 2 that means that we have selected 2 sprites that we want to change places)
        print(sprite)
        pos = self.pos
        pos.append((b, a))
        if len(self.selected_tiles) == 2:
            print("-------------")
            self.affiche()

            # <--
            if(pos[0][0] == pos[1][0] and pos[0][1]+1 == pos[1][1]):
                print("right")
                self.change(pos,self.selected_tiles[0],self.selected_tiles[1])


            # <--
            elif(pos[0][0] == pos[1][0] and pos[0][1]-1 == pos[1][1]):
                print("left")
                self.change(pos,self.selected_tiles[0],self.selected_tiles[1])


            # ^
            elif(pos[0][0]-1 == pos[1][0] and pos[0][1] == pos[1][1]):
                print("top")
                self.change(pos,self.selected_tiles[0],self.selected_tiles[1])


            # v
            elif(pos[0][0]+1 == pos[1][0] and pos[0][1] == pos[1][1]):
                print("bottom")
                self.change(pos,self.selected_tiles[0],self.selected_tiles[1])

           #if the user clicks the same sprite/elements twice nothing happens
            elif(pos[0][0] == pos[1][0] and pos[0][1] == pos[1][1]):
                pass
                #invalid_move.play()

            else:
                #invalid_move.play()
                print("elements not adjascent")

            self.playSound()


            self.selected_tiles.clear()
            self.removeMarked()#the function for checking if there is a match and replacing the matched elements with zeros is called
            self.falling()#the function for replacing the 0 elements/sprites with their upper element/sprite
            if(self.player_turn == 0):
                self.player_turn = 1
            else:
                self.player_turn = 0

            pos.clear()

    #function that replaces the zero elements/sprites with their upper element/s
    def falling(self):
        turn = 0
        while(turn<len(self.grille)):
            for i in range(len(self.grille)-1):
                for j in range(len(self.grille[0])):
                    if(self.grille[i+1][j] == '0'):
                        self.grille[i+1][j], self.grille[i][j] = self.grille[i][j], self.grille[i+1][j]
                        self.cells[i+1][j].sign = self.grille[i+1][j]
                        self.cells[i+1][j].image = Cell.findSign(self,self.cells[i+1][j].sign)

            turn += 1
        for i in range(len(self.grille)-7):
                for j in range(len(self.grille[0])):
                    if(self.grille[i][j] == '0'):
                        self.cells[i][j].sign = self.grille[i][j]
                        self.cells[i][j].image = Cell.findSign(self,self.cells[i][j].sign)
        self.affiche()
        self.new_element()#function that in the frist row adds random new elements after a match
        self.setMarked()
        #loop that finds matching elements/sprites until there is no match
        while(self.hasMatch == True):
            self.removeMarked()
            self.falling()
            self.setMarked()




    #function that after the match of elements/sprites to the first row adds a new random element/sprite
    def new_element(self):
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                if(self.grille[i][j] == '0'):
                    self.grille[i][j] = random.choice(self.tiles)
                    self.cells[i][j].sign = self.grille[i][j]
                    self.cells[i][j].image = Cell.findSign(self,self.cells[i][j].sign)

        print("___after falling___")
        self.affiche()

    #function tha registers the click of the mouse and after the 2 click does the switching
    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # is left button clicked
                for x in range(8):
                    for y in range(8):
                        if self.cells[x][y].rect.collidepoint(event.pos):  # is mouse over button
                            self.check_states(self.cells[x][y],self.cells[x][y].i, self.cells[x][y].j)
                            return



    #function for adding points after every match
    def add_points(self):
        for i in range(len(self.marked)):
            prvo = self.marked[i][0]
            vtoro = self.marked[i][1]
            if(self.grille[prvo][vtoro] == "$"):
                players[self.player_turn].attributes.red += 1

            elif(self.grille[prvo][vtoro] == "@"):
                players[self.player_turn].attributes.green += 1

            elif(self.grille[prvo][vtoro] == "#"):
                players[self.player_turn].attributes.yellow += 1

            elif(self.grille[prvo][vtoro] == "%"):
                players[self.player_turn].attributes.blue += 1

            elif(self.grille[prvo][vtoro] == "*"): #KO
                if(self.player_turn == 0):
                    if(players[self.player_turn+1].attributes.health > 0):
                        players[self.player_turn+1].attributes.health -= 5
                    else:
                        players[self.player_turn+1].attributes.health = 0

                else:
                    if(players[self.player_turn-1].attributes.health > 0):
                        players[self.player_turn-1].attributes.health -= 5
                    else:
                        players[self.player_turn-1].attributes.health = 0


            else: #extra life
                if(players[self.player_turn].attributes.health < 100):
                    players[self.player_turn].attributes.health += (100-players[self.player_turn].attributes.health)

                else:
                    players[self.player_turn].attributes.health += 0
            players[self.player_turn].status()

    def current_player(self):
        """which is the current player"""
        if(self.player_turn == 0):
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2-5.2*50, HEIGHT-175, 120, 5))
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2-5.2*50, HEIGHT-175, 5, 140))
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2-2.9*50, HEIGHT-175, 5, 140))
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2-5.2*50, HEIGHT-35, 120, 5))

        else:
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2+2.8*50, HEIGHT-175, 120, 5))
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2+2.8*50, HEIGHT-175, 5, 140))
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2+5.1*50, HEIGHT-175, 5, 140))
            pygame.draw.rect(screen, DARKRED, pygame.Rect(WIDTH/2+2.8*50, HEIGHT-35, 120, 5))


t = Table(8,8)
