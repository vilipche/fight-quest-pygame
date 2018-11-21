#importing from other folders
from data.settings import *
from data.Classes.Image import Image
from data.Classes.Button import Button
from data.Classes.Message import Message
from data.Classes.Table import t
from data.Classes.Table import P1
from data.Classes.Table import P2
from data.Classes.Table import players
import sys




class Menu:
    """Main menu class, all the functions are staticmethods due to the need to create more screens with different elements"""
    #first screen of the game
    @staticmethod
    def game_intro():
        intro = True
        while intro:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()
                    if(event.key == pygame.K_c):
                        intro = False

            screen.blit(background,[0,0])

            #EXAMPLE FOR IMAGE WITH COLOR FILLED ONLY: img = Image(None, WIDTH/2 ,HEIGHT/2, (170,250), RED)
            img = Image(logo, WIDTH/2-(590/2) ,HEIGHT/2-(300/2)-200, (590,300), None, None)

            b1_intro = Button("Start", 3*WIDTH/4  ,420,100,50, 100/2, 50/2, WHITE, RED, LIVER,"medium", Menu.func_butt(),'instructions')
            b2_intro = Button("Quit", WIDTH/4  ,420,100,50, 100/2, 50/2, WHITE, BLUE, LIVER,"medium",  Menu.func_butt(),'quit')

            pygame.display.update()
            clock.tick(15)

    #first instructions screen
    @staticmethod
    def instructions():
        instruct = True
        while instruct:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()

            screen.blit(background,[-530,0])

            m1_intro = Message("Game instructions", BLACK, 0, -300, "large" )
            m2_intro = Message("You are fighting against your opponent.",BLACK, 0, -255, "small")
            m3_intro = Message("The only way you can win is to",BLACK,0,-230, "small")
            m4_intro = Message("reduce your opponent's health to zero!",BLACK,0,-205, "small")
            m5_intro = Message("Play by matching three or more elements in a row or column.",BLACK,0,-180,  "small")
            el = Image(elements,WIDTH/2-115,HEIGHT/2-170,(240,100),None,None)
            m6_intro = Message("There are 4 tiles and each gives you 1 attribute point!",BLACK,0,-80, "small")
            spe = Image(special,WIDTH/2-120,HEIGHT/2-70,(230,100),None,None)
            m7_intro = Message("KO tiles reduce opponent's health for 5!",BLACK, 0, 30, "small")
            m8_intro = Message("Hearts refill your health!",BLACK, 0, 60, "small")

            b1_intro = Button("Next", 3*WIDTH/4, 500, 100, 50, 100/2, 50/2,CHAMPAGNEWHITE, RED, LIVER, "medium", Menu.func_butt(), "create")
            b1_intro = Button("Back", WIDTH/4, 500, 100, 50, 100/2, 50/2,CHAMPAGNEWHITE, BLUE, LIVER, "medium",  Menu.func_butt(),"start")

            pygame.display.update()
            clock.tick(10)
    #second instructions screen
    @staticmethod
    def create():
        create = True
        while create:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()

            screen.blit(background,[-840,0])
            m1_intro = Message("When you have enogh points, use your skills",CHAMPAGNEWHITE,0,-250, "small")
            m2_intro = Message("to damage and hit your opponent!",CHAMPAGNEWHITE,0,-220, "small")

            spe = Image(moves,WIDTH/2-120,HEIGHT/2-190,(280,150),None,None)

            m4_intro = Message("There are 4 skills and each reduces oponent's",CHAMPAGNEWHITE,0,-20, "small")
            m5_intro = Message("health with a different value (-15,-20,-10,-35).",CHAMPAGNEWHITE,0,10, "small")
            m6_intro = Message("The first player whose health is zero loses.",CHAMPAGNEWHITE,0,60, "small")
            m6_intro = Message("HAVE FUN AND GOOD LUCK!",CHAMPAGNEWHITE,0,140, "medium")

            b1_create = Button("Next", 3*WIDTH/4, 620 , 100, 50, 100/2, 50/2, CHAMPAGNEWHITE, RED, LIVER,"medium", Menu.func_butt(), "play")
            b1_create = Button("Back", WIDTH/4, 620 , 100, 50, 100/2, 50/2, CHAMPAGNEWHITE, BLUE, LIVER,"medium", Menu.func_butt(), "instructions")

            pygame.display.update()
            clock.tick(10)


    #final screen
    @staticmethod
    def finish():
        finish = True
        winning_sound.play()
        while finish:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        pygame.quit()
                        sys.exit()
            if(P1.attributes.health <= 0):
                screen.blit(FINISH2,[0,0])
            else:
                screen.blit(FINISH1,[0,0])

            b1_create = Button("QUIT", WIDTH/2, 620 , 100, 50, 100/2, 50/2, CHAMPAGNEWHITE, BLUE, LIVER,"medium", Menu.func_butt(),"quit")

            pygame.display.update()
            clock.tick(10)

    @staticmethod
    def game_loop():
        # Game loop
        running = True
        start_bell.play()
        while running:
            # keep loop running at the right speed
            clock.tick(FPS)
            # Process input (events)

            # Draw / render
            screen.blit(background_main,[0,0])
            back_score = Image(BACK,WIDTH/2-4.1*50-125/2 , HEIGHT/2+160, (535,200), None, None) #Image P1

            #images for the moves for player 1
            move1_1 = Image(MOVE_1,(WIDTH/2-1.5*50-125/2) , HEIGHT-155-23/2, (125,23), None, "P1FirstP2")
            move2_1 = Image(MOVE_2,(WIDTH/2-1.5*50-125/2) , HEIGHT-120-23/2, (125,23), None, "P1SecondP2")
            move3_1 = Image(MOVE_3,(WIDTH/2-1.5*50-125/2) , HEIGHT-85-23/2, (125,23), None, "P1ThirdP2")
            move4_1 = Image(MOVE_4,(WIDTH/2-1.5*50-125/2) , HEIGHT-50-23/2, (125,23), None, "P1UltiP2")

            #images for the moves for player 2
            move1_2 = Image(MOVE_1,(WIDTH/2+1.49*50-125/2) , HEIGHT-155-23/2, (125,23), None, "P2FirstP1")
            move2_2 = Image(MOVE_2,(WIDTH/2+1.49*50-125/2) , HEIGHT-120-23/2, (125,23), None, "P2SecondP1")
            move3_2 = Image(MOVE_3,(WIDTH/2+1.49*50-125/2) , HEIGHT-85-23/2, (125,23), None, "P2ThirdP1")
            move4_2 = Image(MOVE_4,(WIDTH/2+1.49*50-125/2) , HEIGHT-50-23/2, (125,23), None, "P2UltiP1")

            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False

                t.event_handler(event)

                move1_1.imgbut(event)
                move2_1.imgbut(event)
                move3_1.imgbut(event)
                move4_1.imgbut(event)

                move1_2.imgbut(event)
                move2_2.imgbut(event)
                move3_2.imgbut(event)
                move4_2.imgbut(event)

                t.removeMarked()

            # Update

            t.current_player() #ACTIVE SQUARE, WHO IS PLAYING

            player1 = Image(pic1,(WIDTH/2-4.5*50-50/2) , HEIGHT-140-50/2, (50,50), None, None) #Image P1
            player2 = Image(pic2,(WIDTH/2+4.5*50-50/2) , HEIGHT-140-50/2, (50,50), None, None) #Image P2


            P1.life_status() #updating the health bar
            P2.life_status()
            health_status_P1 = Message(str(P1.attributes.health), BLACK, -WIDTH/4-95, HEIGHT/4+100, "medium")
            health_status_P2 = Message(str(P2.attributes.health), BLACK, WIDTH/4+95, HEIGHT/4+100, "medium")


            #for player 1
            nameP1 = Message("Player 1", BLACK, -200, 176, "medium")
            nameP1 = Message("Player 2", BLACK, 200, 176, "medium")

            #icons for the score
            red = Image(RED_G,(WIDTH/2-3.65*50-22/2) , HEIGHT-155-22/2, (22,22), None, None)
            blue = Image(BLUE_G,(WIDTH/2-3.65*50-22/2) , HEIGHT-129-22/2, (22,22), None, None)
            green = Image(GREEN_G,(WIDTH/2-3.65*50-22/2) , HEIGHT-103-22/2, (22,22), None, None)
            yellow = Image(YELLOW_G,(WIDTH/2-3.65*50-22/2) , HEIGHT-77-22/2, (22,22), None, None)

            Message(str(P1.attributes.red),BLACK,-162,215, "small")
            Message(str(P1.attributes.blue),BLACK,-162,240, "small")
            Message(str(P1.attributes.green),BLACK,-162,265, "small")
            Message(str(P1.attributes.yellow),BLACK,-162,290, "small")

            #for player 2
            #icons for the score
            red = Image(RED_G,(WIDTH/2+3.65*50-22/2) , HEIGHT-155-22/2, (22,22), None, None)
            blue = Image(BLUE_G,(WIDTH/2+3.65*50-22/2) , HEIGHT-129-22/2, (22,22), None, None)
            green = Image(GREEN_G,(WIDTH/2+3.65*50-22/2) , HEIGHT-103-22/2, (22,22), None, None)
            yellow = Image(YELLOW_G,(WIDTH/2+3.65*50-22/2) , HEIGHT-77-22/2, (22,22), None, None)

            Message(str(P2.attributes.red),BLACK,165,215, "small")
            Message(str(P2.attributes.blue),BLACK,165,240, "small")
            Message(str(P2.attributes.green),BLACK,165,265, "small")
            Message(str(P2.attributes.yellow),BLACK,165,290, "small")


            #the values of the skills(moves)
            #Image(self, image, x, y, scale, color, action)
            first_damage = Image(damage_first, WIDTH/2-26/2, HEIGHT-155-26/2, (26, 26), None, None)
            second_damage = Image(damage_second, WIDTH/2-26/2, HEIGHT-120-26/2, (26, 26), None, None)
            third_damage = Image(damage_third, WIDTH/2-26/2, HEIGHT-85-26/2, (26, 26), None, None)
            ulti_damage = Image(damage_ulti, WIDTH/2-26/2, HEIGHT-50-26/2, (26, 26), None, None)

            all_sprites.draw(screen)
            # *after* drawing everything, flip the display
            pygame.display.flip()

            if(P1.attributes.health <= 0):
                f = Menu.finish()
            elif(P2.attributes.health <= 0):
                f = Menu.finish()

        pygame.quit()
        quit()
    #function for quiting the game
    @staticmethod
    def exit_screen():
        pygame.display.quit()
        sys.exit()

    @staticmethod
    def func_butt():
        #functions for the buttons
        functions = {'quit': Menu.exit_screen,
                         'instructions': Menu.instructions,
                         'create': Menu.create,
                         'play': Menu.game_loop,
                         'start': Menu.game_intro
                         }
        return functions
