from  data.settings import *

class Moves:
    def activateFirst(self, attacker_attributes, defender_attributes):
        if(attacker_attributes.blue >= 5 and attacker_attributes.red >= 3):
                attacker_attributes.blue -= 5
                attacker_attributes.red -= 3
                defender_attributes.health -= 15
                first_sound.play()

    def activateSecond(self, attacker_attributes, defender_attributes):
        if(attacker_attributes.red >= 5 and attacker_attributes.green >= 5 and attacker_attributes.yellow >=3):
                attacker_attributes.red -= 5
                attacker_attributes.green -= 5
                attacker_attributes.yellow -=3
                defender_attributes.health -= 20
                second_sound.play()

    def activateThird(self, attacker_attributes, defender_attributes):
        if(attacker_attributes.blue >= 2 and attacker_attributes.green >= 3 and attacker_attributes.yellow >=4):
                attacker_attributes.blue -= 2
                attacker_attributes.green -= 3
                attacker_attributes.yellow -=3
                defender_attributes.health -= 10
                third_sound.play()

    def activateUlti(self, attacker_attributes, defender_attributes):
        if(attacker_attributes.blue >= 7 and attacker_attributes.red >= 7 and attacker_attributes.green >= 7 and attacker_attributes.yellow >=7):
                attacker_attributes.blue -= 7
                attacker_attributes.red -= 7
                attacker_attributes.green -= 7
                attacker_attributes.yellow -= 7
                defender_attributes.health -= 35
                ulti_sound.play()
