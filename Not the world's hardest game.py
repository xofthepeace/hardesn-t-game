import pygame
import random
import time
import math

###### GLOBALS  ########
BACKROUND_COLOR = (225, 233, 245)
BLACK = (0, 0, 0)
COLOR = (255, 100, 98)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (47, 245, 123)

ENEMY_SPACE = 60
clock = pygame.time.Clock()

RED = (255, 0, 0)
COLOR = BLACK

BUTTON_SIZE = (200, 50)

DEBUG_MODE = False
TITLESCREEN = 0
HOW_TO_PLAY = 1
L1_INFO = 2
LEVEL_1 = 3
GAME_OVER = 4
L2_INFO = 5
LEVEL_2 = 6
L3_INFO = 7
LEVEL_3 = 8
L4_INFO = 9
LEVEL_4 = 10
L5_INFO = 11
LEVEL_5 = 12
L6_INFO = 13
LEVEL_6 = 14
L7_INFO = 15
LEVEL_7 = 16
YOU_WIN = 17

STATE = TITLESCREEN

keys_down = [False, False, False, False]
UP_KEY = 0
DOWN_KEY = 1
LEFT_KEY = 2
RIGHT_KEY = 3

all_sprites_list = pygame.sprite.Group()






##########################





# Sprite Class (all other classes will inherit from this one)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width): 
            super().__init__()

            self.image = pygame.Surface([width, height]) 
            self.image.fill(BACKROUND_COLOR) 
            self.image.set_colorkey(COLOR)
            self.x_vel = 0
            self.y_vel = 0

            pygame.draw.rect(self.image, 
                             color, 
                             pygame.Rect(0, 0, width, height)) 
      
            self.rect = self.image.get_rect()


           

###################################

class Player(Sprite):
    def __init__(self, color, height, width):
            super().__init__(color, height, width)

    def update_pos(self, keys_down):
        SPEED_FACTOR = 1

        UP_KEY = 0
        DOWN_KEY = 1
        LEFT_KEY = 2
        RIGHT_KEY = 3
        # print(keys_down)

        if(keys_down[UP_KEY] and keys_down[DOWN_KEY]):
            self.y_vel = 0

        if(keys_down[LEFT_KEY] and keys_down[RIGHT_KEY]):
            self.x_vel = 0

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        


###################################

class Goal(Sprite):
    def __init__(self):
        super().__init__(YELLOW, 40, 40)

        self.x_vel = -3

    # for level 6 only
    def update_pos(self):
        min_x = 90
        max_x = 610
        
        
        if(self.rect.x >= max_x):
            self.x_vel = -2
        elif(self.rect.x <= min_x):
            self.x_vel = 2
        
        self.rect.x += self.x_vel
    

###################################


class Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__(GREEN, 40, 40)
        self.rect.x = x
        self.rect.y = y
        self.x_vel = 0
        self.y_vel = 3

        self.angle = 0
        self.radius = 100

        # used for level 6
        self.max_x = 0
        self.min_x = 0
        

        # for level 4 chasing movement
        self.toggle = True
        self.slow_toggle = 1


    # func returns a tuple
    # (dx, dy) which Enemy moves based on
    def update_pos(self, func):
        func(self)
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        # print(str(self.y_vel))

    # this is the chasing enemy for Level 4
    def L4_Enemy_chase(self, player):
        if(self.toggle == True):
            # x coordinate move
            if(self.rect.x < player.rect.x):
                self.rect.x += 1
            elif(self.rect.x > player.rect.x):
                self.rect.x -= 1

            # y coordinate move
            if(self.rect.y < player.rect.y):
                self.rect.y += 1
            elif(self.rect.y > player.rect.y):
                self.rect.y -= 1

            self.toggle = False
        else:
            self.toggle = True


    # this is the chasing enemy for Level 7
    def L7_Enemy_chase(self, player):
        if(self.slow_toggle % 5 == 0):
            # x coordinate move
            if(self.rect.x < player.rect.x):
                self.rect.x += 1
            elif(self.rect.x > player.rect.x):
                self.rect.x -= 1

            # y coordinate move
            if(self.rect.y < player.rect.y):
                self.rect.y += 1
            elif(self.rect.y > player.rect.y):
                self.rect.y -= 1

            self.slow_toggle = 1
        else:
            self.slow_toggle += 1
    



        
        







###################################


# Text class, used for displaying text
class Text():
    def __init__(self, text, x, y, screen):
        self.text = text
        self.x = x
        self.y = y

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text_render = font.render(self.text, True, WHITE, BLACK)
        self.text_rect = self.text_render.get_rect()
        self.text_rect.center = (x,y)
        # screen.blit(text_render, text_rect)
    
###################################

        


# Setting up the window

pygame.init()
screen_size = (700,700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("The word's hardestn't game")
all_sprites_list = pygame.sprite.Group()
enemy_sprites_list = pygame.sprite.Group()
font = pygame.font.Font('freesansbold.ttf', 32)



# object initialization
player = Player(RED, 20, 30)
all_sprites_list.add(player)

# setting up the enemy
enemy1 = Enemy(200,700)


enemy2 = Enemy(200 + ENEMY_SPACE,0)


enemy3 = Enemy(200 + 2*ENEMY_SPACE,700)


enemy4 = Enemy(200 + 3*ENEMY_SPACE, 0)


enemy5 = Enemy(375, 0)
# enemy_sprites_list.add(enemy5)

goal = Goal()
all_sprites_list.add(goal)

# inner layer
enemy6 = Enemy(0,0)
enemy7 = Enemy(0,0)
enemy8 = Enemy(0,0)
enemy9 = Enemy(0,0)

# outer layer
enemyA = Enemy(0,0)
enemyB = Enemy(0,0)
enemyC = Enemy(0,0)
enemyD = Enemy(0,0)

enemy14 = Enemy(600, 100)

# spinny
enemy15 = Enemy(0,0)
enemy16 = Enemy(0,0)


# for level 5
enemy17 = Enemy(380, 100)
enemy18 = Enemy(500, 100)
enemy19 = Enemy(620, 100)

# for level 6
enemy20 = Enemy(600, 100)
enemy21 = Enemy(230, 650)
enemy22 = Enemy(370, 650)

# for level 7
enemy23 = Enemy(260, 100)
enemy24 = Enemy(380, 100)
enemy25 = Enemy(500, 100)

# spinny
enemy26 = Enemy(0,0)
enemy27 = Enemy(0,0)

# slow chase
# enemy28 = Enemy(650, 30)


###################################

def reset_all():
    global player
    global enemy1
    global enemy2
    global enemy3
    global enemy4
    global enemy5
    global enemy6
    global enemy7
    global enemy8
    global enemy9
    global enemyA
    global enemyB
    global enemyC
    global enemyD
    global enemy14
    global enemy15
    global enemy16
    global enemy17
    global enemy18
    global enemy19
    global enemy20
    global enemy21
    global enemy22
    global enemy23
    global enemy24
    global enemy25
    global enemy26
    global enemy27
    global keys_down
    global goal


    player = Player(RED, 20, 30)


    # setting up the enemy
    enemy1 = Enemy(200,700)


    enemy2 = Enemy(200 + ENEMY_SPACE,0)


    enemy3 = Enemy(200 + 2*ENEMY_SPACE,700)


    enemy4 = Enemy(200 + 3*ENEMY_SPACE, 0)


    enemy5 = Enemy(375, 0)
    # enemy_sprites_list.add(enemy5)

    goal = Goal()
    all_sprites_list.add(goal)

    # inner layer
    enemy6 = Enemy(0,0)
    enemy7 = Enemy(0,0)
    enemy8 = Enemy(0,0)
    enemy9 = Enemy(0,0)

    # outer layer
    enemyA = Enemy(0,0)
    enemyB = Enemy(0,0)
    enemyC = Enemy(0,0)
    enemyD = Enemy(0,0)

    enemy14 = Enemy(600, 100)

    # spinny
    enemy15 = Enemy(0,0)
    enemy16 = Enemy(0,0)


    # for level 5
    enemy17 = Enemy(380, 100)
    enemy18 = Enemy(500, 100)
    enemy19 = Enemy(620, 100)

    # for level 6
    enemy20 = Enemy(600, 100)
    enemy21 = Enemy(230, 650)
    enemy22 = Enemy(370, 650)

    # for level 7
    enemy23 = Enemy(260, 100)
    enemy24 = Enemy(380, 100)
    enemy25 = Enemy(500, 100)

    # spinny
    enemy26 = Enemy(0,0)
    enemy27 = Enemy(0,0)

    keys_down = [False, False, False, False]

    goal.x_vel = -3

    



###################################


def L1_Enemy_move(enemy):
    max_y = 670
    min_y = 20
    
    if(enemy.rect.y >= max_y):
        enemy.y_vel = -3
    elif(enemy.rect.y <= min_y):
        enemy.y_vel = 3
    





###################################

def L2_Enemy_move(enemy):
    max_y = 400
    min_y = 20
    
    if(enemy.rect.y >= max_y):
        enemy.y_vel = -3
    elif(enemy.rect.y <= min_y):
        enemy.y_vel = 3






####################################

def L3_Enemy_move(enemy):
    # ensures velocity is 0
    enemy.x_vel = 0
    enemy.y_vel =  0

    r = enemy.radius

    

    # for readibility
    x = enemy.rect.x
    y = enemy.rect.y
    a = enemy.angle

    x = 310 + math.cos(a)*r
    y = 310 + math.sin(a)*r

    enemy.rect.x = x
    enemy.rect.y = y

    enemy.angle += 0.01
    
    



####################################

# this is for the spinning motion
def L4_Enemy_move(enemy):
    #ensures velocity is 0
    enemy.x_vel = 0
    enemy.y_vel =  0

    r = 100

    

    # for readibility
    x = enemy.rect.x
    y = enemy.rect.y
    a = enemy.angle

    x = 550 + math.cos(a)*r
    y = 550 + math.sin(a)*r

    enemy.rect.x = x
    enemy.rect.y = y

    enemy.angle += 0.01


####################################

def L6_Enemy_move(enemy):
    enemy.y_vel =  0
    
    if(enemy.rect.x >= enemy.max_x):
        enemy.x_vel = -2
    elif(enemy.rect.x <= enemy.min_x):
        enemy.x_vel = 2




####################################

def L7_Enemy_move(enemy):
    #ensures velocity is 0
    enemy.x_vel = 0
    enemy.y_vel =  0

    goal_x = 660
    goal_y = 530

    r = 100

    

    # for readibility
    x = enemy.rect.x
    y = enemy.rect.y
    a = enemy.angle

    x = 660 + math.cos(a)*r
    y = 530 + math.sin(a)*r

    enemy.rect.x = x
    enemy.rect.y = y

    enemy.angle += 0.01


####################################




def game_over():
    screen.fill(BACKROUND_COLOR)

    
    title = Text("Game over :(", 340, 266, screen)

    i = 720
    
    while i >= 0:
        screen.blit(title.text_render, title.text_rect)

        pygame.display.update()

        clock.tick(240)


        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.display.quit()
                pygame.quit()


        
        i -= 1
        
    
    # pygame.time.wait(3000)

    global STATE
    STATE = TITLESCREEN


    






###################################

# Titlescreen function
def titlescreen():
    screen.fill(BACKROUND_COLOR)

    # Blits text onto the screen
    test = Text("The World's Hardestn't Game", 360, 66, screen)
    screen.blit(test.text_render, test.text_rect)


    # "Play Game" button
    play_game_button = pygame.Surface(BUTTON_SIZE)
    play_game_text = font.render("Play game", True, WHITE)
    play_game_text_rect = play_game_text.get_rect(center=(play_game_button.get_width()/2, play_game_button.get_height()/2))
    play_game_button_rect = pygame.Rect(260, 264, BUTTON_SIZE[0], BUTTON_SIZE[1])
    play_game_button.blit(play_game_text, play_game_text_rect)
    screen.blit(play_game_button, (play_game_button_rect.x, play_game_button_rect.y))


    # "How to Play" button
    htp_button = pygame.Surface(BUTTON_SIZE)
    htp_text = font.render("How to Play", True, WHITE)
    htp_text_rect = htp_text.get_rect(center=(htp_button.get_width()/2, htp_button.get_height()/2))
    htp_button_rect = pygame.Rect(260, 338, BUTTON_SIZE[0], BUTTON_SIZE[1])
    htp_button.blit(htp_text, htp_text_rect)
    screen.blit(htp_button, (htp_button_rect.x, htp_button_rect.y))
    
    pygame.display.update()
    
    

    # purely for debugging purposes (learn where the cursor is)
    if(DEBUG_MODE):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                print(pygame.mouse.get_pos())


            

    # Handles button clicks
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            global STATE
            if play_game_button_rect.collidepoint(event.pos):
                STATE = L1_INFO
            if htp_button_rect.collidepoint(event.pos):
                STATE = HOW_TO_PLAY

    # if red x pressed then quit
        if event.type == pygame.QUIT: 
            pygame.display.quit()
            pygame.quit()
        
    
        
        

###################################

# How_to_play() function

def how_to_play():
    screen.fill(BACKROUND_COLOR)

    # defining text
    space_size =  60
    title = Text("How to Play", 360, 66, screen)
    rules_1 = Text("You play as a red square and your", 360, 166 + space_size, screen)
    rules_2 = Text("objective is to reach the goal", 360, 166 + 2*space_size, screen)
    rules_3 = Text("while avoiding the enemies. There are", 360, 166 + 3*space_size, screen)
    rules_4 = Text("also coins you can collect.", 360, 166 + 4*space_size, screen)
    rules_5 = Text("Good luck!", 360, 166 + 5*space_size, screen)



    i = 1200


    while i >= 0:
        
        # all blits and update
        screen.blit(title.text_render, title.text_rect)
        screen.blit(rules_1.text_render, rules_1.text_rect)
        screen.blit(rules_2.text_render, rules_2.text_rect)
        screen.blit(rules_3.text_render, rules_3.text_rect)
        screen.blit(rules_4.text_render, rules_4.text_rect)
        screen.blit(rules_5.text_render, rules_5.text_rect)
        pygame.display.update()

        i -= 1
        clock.tick(240)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.display.quit()
                pygame.quit()

        



    # pygame.time.wait(5000)

    global STATE
    STATE = TITLESCREEN



##################################

def Level_setup(level):
    # pass this function the ACTUAL level, not STATE

    global keys_down
    keys_down = [False, False, False, False]
    player.x_vel = 0
    player.y_vel = 0


    
    if level == 1:
        all_sprites_list.empty()
        enemy_sprites_list.empty()

        all_sprites_list.add(player)
        all_sprites_list.add(goal)
        all_sprites_list.add(enemy1)
        all_sprites_list.add(enemy2)
        all_sprites_list.add(enemy3)
        all_sprites_list.add(enemy4)

        
        
        # setting up goal for level 1
        goal.rect.x = 600
        goal.rect.y = 300

        # setting up player for level 1
        player.rect.x = 100
        player.rect.y = 300
        player.x_vel = 0
        player.y_vel = 0

        keys_down = [False, False, False, False]

    elif level == 2:
        all_sprites_list.remove(enemy1)
        all_sprites_list.remove(enemy2)
        all_sprites_list.remove(enemy3)
        all_sprites_list.remove(enemy4)

        goal.rect.x = 600
        goal.rect.y = 230

        player.rect.x = 58
        player.rect.y = 240

        # makes 15 enemies (for level 2)
        enemy_coors = [(120, 280),
                        (170, 270),
                        (220, 255),
                        (270, 240),
                        (325, 245),
                        (375, 255),
                        (430, 245),
                        (475, 255),
                        (525, 270),

                        (120, 180),
                        (170, 170),
                        (220, 155),
                        (270, 140),
                        (325, 145),
                        (375, 155),
                        (430, 145),
                        (475, 155),
                        (525, 180)]

        limit = 0
        while(limit <= 700):
            enemy_coors.append((limit,330))
            enemy_coors.append((limit,80))
            limit+= 69

        # global enemy_sprites_list
        for i in enemy_coors:
            enemy = Enemy(i[0], i[1])
            all_sprites_list.add(enemy)
            enemy_sprites_list.add(enemy)

        global enemy5
        all_sprites_list.add(enemy5)

        
    elif level == 3:

        all_sprites_list.empty()
        all_sprites_list.add(player)
        all_sprites_list.add(goal)
        all_sprites_list.add(enemy6)
        all_sprites_list.add(enemy7)
        all_sprites_list.add(enemy8)
        all_sprites_list.add(enemy9)

        all_sprites_list.add(enemyA)
        all_sprites_list.add(enemyB)
        all_sprites_list.add(enemyC)
        all_sprites_list.add(enemyD)

        enemy_sprites_list.empty()

        enemy_sprites_list.add(enemy6)
        enemy_sprites_list.add(enemy7)
        enemy_sprites_list.add(enemy8)
        enemy_sprites_list.add(enemy9)

        enemy_sprites_list.add(enemyA)
        enemy_sprites_list.add(enemyB)
        enemy_sprites_list.add(enemyC)
        enemy_sprites_list.add(enemyD)

        enemy6.angle = 0
        enemy7.angle = 3.1415 / 2
        enemy8.angle = 3.1415
        enemy9.angle = 3* (3.1415 / 2)

        offset = 3.1415 / 4

        enemyA.angle = offset
        enemyB.angle = (3.1415 / 2) + offset
        enemyC.angle = 3.1415 + offset
        enemyD.angle = (3* (3.1415 / 2)) + offset

        radius = 250

        enemyA.radius = radius
        enemyB.radius = radius
        enemyC.radius = radius
        enemyD.radius = radius

        # setting player and goal coordinates
        goal.rect.x = 310
        goal.rect.y = 310

        player.rect.x = 30
        player.rect.y = 30

        
        # enemy6.rect.x = 100
        # enemy6.rect.y = 100

    elif level == 4:

        # setup for level 4
        all_sprites_list.empty()
        enemy_sprites_list.empty()

        all_sprites_list.add(player)
        all_sprites_list.add(goal)
        all_sprites_list.add(enemy14)
        enemy_sprites_list.add(enemy14)
        
        all_sprites_list.add(enemy15)
        all_sprites_list.add(enemy16)

        enemy_sprites_list.add(enemy15)
        enemy_sprites_list.add(enemy16)

        enemy15.angle = 0
        enemy16.angle = 3.1415
        


        # setting coordinates
        goal.rect.x = 550
        goal.rect.y = 550

        player.rect.x = 58
        player.rect.y = 240

    elif level == 5:
        # setup for level 5
        all_sprites_list.empty()
        enemy_sprites_list.empty()

        all_sprites_list.add(player)
        all_sprites_list.add(goal)

        all_sprites_list.add(enemy17)
        all_sprites_list.add(enemy18)
        all_sprites_list.add(enemy19)

        enemy_sprites_list.add(enemy17)
        enemy_sprites_list.add(enemy18)
        enemy_sprites_list.add(enemy19)

        

        goal.rect.x = 660
        goal.rect.y = 530

        player.rect.x = 58
        player.rect.y = 240

        # r stands for reference
        # this is the coordinate we'll base
        # everything on
        rx = 220
        ry = 100

        space = 160


        
        enemy_loc = [   (rx, ry),
                        (rx + 40, ry - 40),
                        (rx + 80, ry),
                        (rx + 120, ry + 40),
                        (rx + 160, ry + 80),
                        (rx + 200, ry + 120),
                        (rx + 240, ry + 160),

                        (rx + 280, ry + 200),
                        (rx + 320, ry + 240),
                        (rx + 360, ry + 280),
                        (rx + 400, ry + 320),
                        (rx + 440, ry + 360),
                        
                        
                      

                        (rx, ry  + space),
                        (rx + 40, ry - 40 + space),
                        (rx + 80, ry  + space),
                        (rx + 120, ry + 40  + space),
                        (rx + 160, ry + 80  + space),
                        (rx + 200, ry + 120  + space),
                        (rx + 240, ry + 160  + space),


                        (rx + 280, ry + 200 + space),
                        (rx + 320, ry + 240 + space),
                        (rx + 360, ry + 280 + space),
                        (rx + 400, ry + 320 + space),
                        (rx + 440, ry + 360 + space)]

        
        
        for i in enemy_loc:
            enemy = Enemy(i[0], i[1])
            all_sprites_list.add(enemy)
            enemy_sprites_list.add(enemy)

    elif level == 6:

        # getting sprite lists setup
        all_sprites_list.empty()
        enemy_sprites_list.empty()

        all_sprites_list.add(player)
        all_sprites_list.add(goal)

        all_sprites_list.add(enemy20)
        all_sprites_list.add(enemy21)
        all_sprites_list.add(enemy22)

        enemy_sprites_list.add(enemy20)
        enemy_sprites_list.add(enemy21)
        enemy_sprites_list.add(enemy22)

        # setting up coordinates
        goal.rect.x = 300
        goal.rect.y = 650

        player.rect.x = 58
        player.rect.y = 240


        enemy21.min_x = 20
        enemy22.min_x = 160


        enemy21.max_x = 540
        enemy22.max_x = 680

        enemy21.x_vel = -3
        enemy22.x_vel = -3


    elif level == 7:
        
        all_sprites_list.empty()
        enemy_sprites_list.empty()

        all_sprites_list.add(player)
        all_sprites_list.add(goal)

        all_sprites_list.add(enemy23)
        all_sprites_list.add(enemy24)
        all_sprites_list.add(enemy25)
        all_sprites_list.add(enemy26)
        all_sprites_list.add(enemy27)
        # all_sprites_list.add(enemy28)
        

        enemy_sprites_list.add(enemy23)
        enemy_sprites_list.add(enemy24)
        enemy_sprites_list.add(enemy25)
        enemy_sprites_list.add(enemy26)
        enemy_sprites_list.add(enemy27)
        # enemy_sprites_list.add(enemy28)




        enemy26.angle = 0
        enemy27.angle = 3.1415

        

        goal.rect.x = 660
        goal.rect.y = 530

        player.rect.x = 58
        player.rect.y = 240

        # r stands for reference
        # this is the coordinate we'll base
        # everything on
        rx = 220
        ry = 100

        space = 160


        
        enemy_loc = [   (rx, ry),
                        (rx + 40, ry - 40),
                        (rx + 80, ry),
                        (rx + 120, ry + 40),
                        (rx + 160, ry + 80),
                        (rx + 200, ry + 120),
                        (rx + 240, ry + 160),

                        (rx + 280, ry + 200),
                        (rx + 320, ry + 240),
                        (rx + 360, ry + 280),
                        (rx + 400, ry + 320),
                        (rx + 440, ry + 360),
                        
                        
                      

                        (rx, ry  + space),
                        (rx + 40, ry - 40 + space),
                        (rx + 80, ry  + space),
                        (rx + 120, ry + 40  + space),
                        (rx + 160, ry + 80  + space),
                        (rx + 200, ry + 120  + space),
                        (rx + 240, ry + 160  + space),


                        (rx + 280, ry + 200 + space),
                        (rx + 320, ry + 240 + space),
                        (rx + 360, ry + 280 + space),
                        (rx + 400, ry + 320 + space),
                        (rx + 440, ry + 360 + space)]

        
        
        for i in enemy_loc:
            enemy = Enemy(i[0], i[1])
            all_sprites_list.add(enemy)
            enemy_sprites_list.add(enemy)
        
        
        
        
        
    



##################################

# L1_info function
# is a pure void function

def L_info(level):
    screen.fill(BACKROUND_COLOR)

    string = ''
    if(level == 2): # level 1
        string = "Get ready..."


        

        
    elif(level == 5): # level 2

        # setup for level 2
        string = "Good luck getting through"
        

    elif level == 7: # level 3
        string = "Careful with this roundabout"
        
        
    elif level == 9: # level 4
        string = "Don't stay still..."

        

        
    elif level == 11: # level 5
        string = "Be careful!"

        

    elif level == 13: # level 6
        string = "Get ready to chase the goal"


        

    elif level == 15: # level 7
        string = "The final level. Good luck!"



    elif level == 17: #YOU_WIN state
        string = "YOU WIN!!!!!"
        

        
        
        
        

    i = 360   
    
    while i >= 0:
        title = Text(string, 340, 266, screen)
        screen.blit(title.text_render, title.text_rect)

        pygame.display.update()


        
        clock.tick(240)
        i -= 1

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.display.quit()
                pygame.quit()

        

        

        #pygame.time.wait(1500)
    





##################################

def Level(state):
    global STATE


    LEVEL_1 = 3
    LEVEL_2 = 6
    LEVEL_3 = 8
    LEVEL_4 = 10
    LEVEL_5 = 12
    LEVEL_6 = 14
    LEVEL_7 = 16 # i think
    

    pygame.key.set_repeat(1)

    player_move = True

    

    screen.fill(BACKROUND_COLOR)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.display.quit()
            pygame.quit()

        # player movement
        global keys_down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                keys_down[RIGHT_KEY] = True
                player.x_vel = 1
            if event.key == pygame.K_LEFT:
                keys_down[LEFT_KEY] = True
                player.x_vel = -1
            if event.key == pygame.K_UP:
                keys_down[UP_KEY] = True
                player.y_vel = -1
            if event.key == pygame.K_DOWN:
                keys_down[DOWN_KEY] = True
                player.y_vel = 1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                keys_down[RIGHT_KEY] = False
                player.x_vel = 0
            if event.key == pygame.K_LEFT:
                keys_down[LEFT_KEY] = False
                player.x_vel = 0
            if event.key == pygame.K_UP:
                keys_down[UP_KEY] = False
                player.y_vel = 0
            if event.key == pygame.K_DOWN:
                keys_down[DOWN_KEY] = False
                player.y_vel = 0

        # bounds check
        if(player.rect.x <= 0):
            player.rect.x = 0
        if(player.rect.x >= 670):
            player.rect.x = 670
        if(player.rect.y <= 0):
            player.rect.y = 0
        if(player.rect.y >= 680):
            player.rect.y = 680

    
    
    
    # draw everything
    player.update_pos(keys_down)
    # print(keys_down)
    # player.update_pos(keys_down)
    all_sprites_list.update()
    all_sprites_list.draw(screen) 
    pygame.display.update()
    # print(all_sprites_list)



    
    


    if(state == LEVEL_1):
    
        # goal pos
        
        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):

            # Since the player reached the goal, we need to
            # set up for level 2
            STATE = L2_INFO

        # setting up enemies
        enemy1.update_pos(L1_Enemy_move)
        enemy2.update_pos(L1_Enemy_move)
        enemy3.update_pos(L1_Enemy_move)
        enemy4.update_pos(L1_Enemy_move)
        enemy1_col = pygame.sprite.collide_rect(player, enemy1)
        enemy2_col = pygame.sprite.collide_rect(player, enemy2)
        enemy3_col = pygame.sprite.collide_rect(player, enemy3)
        enemy4_col = pygame.sprite.collide_rect(player, enemy4)
        if(enemy1_col or enemy2_col or enemy3_col or enemy4_col):
            STATE = GAME_OVER

    elif state == LEVEL_2:
        

        enemy5.update_pos(L2_Enemy_move)

        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):
            STATE = L3_INFO

        enemy_col  = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
        if(enemy_col != []):
            STATE = GAME_OVER
            # enemy_sprites_list = []

    elif state == LEVEL_3:

        # update all enemy positions
        enemy6.update_pos(L3_Enemy_move)
        enemy7.update_pos(L3_Enemy_move)
        enemy8.update_pos(L3_Enemy_move)
        enemy9.update_pos(L3_Enemy_move)

        enemyA.update_pos(L3_Enemy_move)
        enemyB.update_pos(L3_Enemy_move)
        enemyC.update_pos(L3_Enemy_move)
        enemyD.update_pos(L3_Enemy_move)

        # see if player touched enemy
        enemy_col  = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
        if(enemy_col != []):
            STATE = GAME_OVER

        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):
            STATE = L4_INFO

    elif state == LEVEL_4:
        enemy14.L4_Enemy_chase(player)

        enemy15.update_pos(L4_Enemy_move)
        enemy16.update_pos(L4_Enemy_move)

        
        
        # see if player touched enemy
        enemy_col  = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
        if(enemy_col != []):
            STATE = GAME_OVER

        # check if player touched goal
        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):
            STATE = L5_INFO

            
    elif state == LEVEL_5:
        enemy17.update_pos(L1_Enemy_move)
        enemy18.update_pos(L1_Enemy_move)
        enemy19.update_pos(L1_Enemy_move)

        # see if player touched enemy
        enemy_col  = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
        if(enemy_col != []):
            STATE = GAME_OVER

        # check if player touched goal
        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):
            STATE = L6_INFO

    elif state == LEVEL_6:
        enemy20.L4_Enemy_chase(player)
        enemy21.update_pos(L6_Enemy_move)
        enemy22.update_pos(L6_Enemy_move)

        goal.update_pos()

        # see if player touched enemy
        enemy_col  = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
        if(enemy_col != []):
            STATE = GAME_OVER

        # check if player touched goal
        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):
            STATE = L7_INFO

            
    elif state == LEVEL_7:
        enemy23.update_pos(L1_Enemy_move)
        enemy24.update_pos(L1_Enemy_move)
        enemy25.update_pos(L1_Enemy_move)

        enemy26.update_pos(L7_Enemy_move)
        enemy27.update_pos(L7_Enemy_move)
        # enemy28.L7_Enemy_chase(player)


        # see if player touched enemy
        enemy_col  = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
        if(enemy_col != []):
            STATE = GAME_OVER

        # check if player touched goal
        goal_col = pygame.sprite.collide_rect(player, goal)
        if(goal_col == True):
            STATE = YOU_WIN
        
        

        

    
    



##################################

# dispatch function
def dispatch(state):
    if state == TITLESCREEN:
        reset_all()
        titlescreen()
    elif state == HOW_TO_PLAY:
        how_to_play()
    elif state == L1_INFO:
        L_info(L1_INFO)
        global STATE
        STATE += 1 # need this to progress to next state
        Level_setup(1)
    elif state == LEVEL_1:
        Level(state)
    elif state == GAME_OVER:
        game_over()
    elif state == L2_INFO:
        L_info(L2_INFO)
        Level_setup(2)
        STATE += 1
    elif state == LEVEL_2:
        Level(state)
    elif state == L3_INFO:
        L_info(L3_INFO)
        Level_setup(3)
        STATE += 1
    elif state == LEVEL_3:
        Level(state)
    elif state == L4_INFO:
        L_info(L4_INFO)
        Level_setup(4)
        STATE += 1
    elif state == LEVEL_4:
        Level(state)
    elif state == L5_INFO:
        L_info(L5_INFO)
        Level_setup(5)
        STATE += 1
    elif state == LEVEL_5:
        Level(state)
    elif state == L6_INFO:
        L_info(L6_INFO)
        Level_setup(6)
        STATE += 1
    elif state == LEVEL_6:
        Level(state)
    elif state == L7_INFO:
        L_info(L7_INFO)
        Level_setup(7)
        STATE += 1
    elif state == LEVEL_7:
        Level(state)
    elif state == YOU_WIN:
        L_info(YOU_WIN)
        STATE = TITLESCREEN
    else:
        print("Error: invalid state")
        pygame.display.quit()
        pygame.quit()
        quit()

###################################


while True:
    dispatch(STATE)
    clock.tick(240)
    


