# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""
██████╗ ██╗   ██╗████████╗██████╗  ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ██████╔╝██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

-----------------------------------------------------                                                     


    ██╗      █████╗ ████████╗ █████╗ ███╗   ███╗
    ██║     ██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║
    ██║     ███████║   ██║   ███████║██╔████╔██║
    ██║     ██╔══██║   ██║   ██╔══██║██║╚██╔╝██║
    ███████╗██║  ██║   ██║   ██║  ██║██║ ╚═╝ ██║
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝

-----------------------------------------------------

2015/DEC/03 - NOTTINGHAM, UK

"""""""""""""""""""""""""""""""""""""""""""""""""""

import pygame, sys, os
from threading import Timer
from pygame.locals import *

"""
DEFINING CONSTANTS AND VARIABLES
"""
 
# Players by colour of bike
# Yellow
PLAYER1 = (224,185,68)
# Cyan
PLAYER2 = (33,224,225) 

# Screens and borders of the display
WHITE = (0, 0, 0)
BORDER = 20
BORDER2 = 30
SIZE = (600, 600)

# Dimensions of the head and body of the bikes
LENGTH = 10
HEIGHT = 10

# List to store the player who loses when a collition occurs
lose = []
# List containing all the sprites created with the movements of the bikes
list_of_all_sprites = []

flag = True

pygame.init()

# Defining the sound effect that depicts the collitions
crashfx = pygame.mixer.Sound('crash.wav')


"""
SETTING INITIAL VALUES AT THE START OF EACH GAME
"""

def initialValues():
    
    global x1, x2, y1, y2 , lose, flag, list_of_all_sprites
 
    # Initial speed of bike1
    x1 = LENGTH
    y1 = 0
    
    # Initial speed of bike2
    x2 = -LENGTH
    y2 = 0

    flag = True
    lose = []
    list_of_all_sprites = []


"""
DEFINING THE CLASS THAT CREATES THE BIKES
"""

# Class that creates sprites for the bikes
class Bike(pygame.sprite.Sprite):
    
    # Constructor
    def __init__(self, colour, x, y):
        
        # Call to the parent constructor
        pygame.sprite.Sprite.__init__(self)
        self.colour = colour
          
        # Establishing the lenght and height of every initial sprite for the bikes
        self.image = pygame.Surface([LENGTH, HEIGHT])
        self.image.fill(colour)
        
        # Before creating the initial sprite of both bikes and setting their coordinates, checkCollition is called to check if their sprites are not collisioned
        if checkCollition(x,y) :
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        else :
            # Else if there is a collision then the RGB values of the loser are appended to the list 'lose'
            lose.append(colour)
            global flag
            # A thread is created to detect if there is another collision going on simultaneously
            if flag :
                crashfx.play()
                # Calling the thread
                t = Timer(1,checkWinner)
                t.start()
                # Delay to wait whether the other bike has collided
                pygame.time.delay(1000)
                flag = False 

"""
FUNCTION CREATED FOR CHECKING COLLISIONS
"""

#Function that checks if sprites have not yet been created. Else, a collision is detected
def checkCollition(x,y):
    for e in list_of_all_sprites :
        # Checking for collisions between bikes' sprites
        if e.rect.x == x and e.rect.y == y:
            return False
        # Checking for collisions with the borders of the display
        if x < BORDER or x > SIZE[0] - BORDER2 or y < BORDER or y > SIZE[1] - BORDER2 :
            return False
    return True  

"""
FUNCTION FOR CHECKING WHO WINS
"""

def checkWinner():

    # Display an image according to who wins or ties
    p1Img = pygame.image.load('player1.jpg')
    p2Img = pygame.image.load('player2.jpg')
    tieImg = pygame.image.load('tie.jpg')
    
    screen.fill(WHITE)
    # If list 'lose' has 2 elements it means a tie
    if len(lose)>1:
        screen.blit(tieImg, (0, 0))
    # If player 2 is on the list player 1 wins
    elif lose[0] == PLAYER2:
        screen.blit(p1Img, (0, 0))        
    # Otherwise the player 2 wins
    else :
        screen.blit(p2Img, (0, 0))
    pygame.display.update()


"""
FUNCTION FOR CALLING INTRODUCTORY SCREENS
"""  
       
def startScreens():

    end_start = False
    
    # Import images
    bikeImg = pygame.image.load('bike_txt.png')
    instImg = pygame.image.load('instructions.jpg')
    bckImg = pygame.image.load('intro.jpg')
    creImg = pygame.image.load('credits.jpg')
    
    # Setting frames per second
    FPS = 15 
    fpsClock = pygame.time.Clock()

    # Initial positions for the animation of the instroductory screen
    bikex = SIZE[0] + 40
    bikey = (SIZE[1]/2) + 20
    
    # Variable created for defining the movement of the loop
    direction = 'left'

    # Initializing introductory song
    pygame.mixer.init()
    introSound = pygame.mixer.Sound('intro.ogg')
        
    global screen
    screen = pygame.display.set_mode(SIZE)
    introSound.play(-1)

    # Loop created for the animation of the introductory screen
    while not end_start:
        screen.fill(WHITE)
        # If direction variable is left the movement of the bike image is across the screen
        if direction == 'left':
            #speed of the movement
            bikex -= 20
            if bikex == -SIZE[0]-200:
                direction = 'loop'
        # If direction variable is loop the 'bike image' returns to the initial point
        elif direction == 'loop':
            #speed of the movement
            bikex = SIZE[0] + 40
            direction = 'left'

        # Setting the images on the screen
        screen.blit(bckImg, (0, 0))
        screen.blit(bikeImg, (bikex, bikey))
        pygame.display.update()
        fpsClock.tick(FPS)

        # Creating the key events for jump between screens
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                # Key code 'spacebar' ends animation loop displays the instructions screen from instructions loop
                if event.key == pygame.K_SPACE:
                    screen.fill(WHITE)
                    instructions_start = False
                    end_start = True

                # Key code 'c' displays the credits screen for 4 seconds
                if event.key == pygame.K_c:
                    screen.blit(creImg, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(4000)

    # Initializing the instructions loop to show the keycodes for playing the game
    while not instructions_start:   
        screen.blit(instImg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():

            # Key code 'spacebar' ends the animation loop and skips to the game controls screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    introSound.stop()
                    instructions_start = True
                    
  
# Setting the title of the game
pygame.display.set_caption('PyTron')

startScreens()

"""
FUNCTION TO SET AND INITIALIZE MAIN GAMEPLAY SEQUENCE
"""

def game():
    gridImg = pygame.image.load('grid.jpg')
    
    # Initiliazing globals for list of all sprites and coordinates for each bike
    global list_of_all_sprites , x1, x2, y1, y2
    list_of_all_sprites = pygame.sprite.Group()
     
    # In this list are all the sprites of the 1st bike
    list_first_bike= pygame.sprite.Group()

    # Setting the initial point for the 1st bike at the middle of the left side border
    x01=BORDER
    y01=SIZE[1]/2

    # Creating the bike for PLAYER1 and adding values to its respective list
    bike1=Bike(PLAYER1,x01, y01)
    list_first_bike.add(bike1)

    # In this list are all the sprites of the 2nd bike
    list_second_bike= pygame.sprite.Group()

    # Setting the initial point for the 1st bike at the middle of the right side border
    x02=SIZE[0]-BORDER2    
    y02=SIZE[1]/2

    # Creating the bike for PLAYER2 and adding values to its respective list
    bike2=Bike(PLAYER2,x02, y02)
    list_second_bike.add(bike2)

    # Adding the first sprites of both bikes to the list of all sprites
    list_of_all_sprites.add(bike1)
    list_of_all_sprites.add(bike2)
      
    clock = pygame.time.Clock()
    done = False

    #Variables to keep each player from turning back the opposite way
    MOVplay1='r'
    MOVplay2='l'

    #Loop for bike movements
    while not done:
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:             
                pass
            
            if event.type == pygame.KEYDOWN:
                # Controlling the movements of the first bike with the keys: a,d, w and s
                if event.key == pygame.K_a and not (MOVplay1 == 'r'):
                    x1 = (LENGTH) * -1
                    y1 = 0
                    MOVplay1 = 'l'
                if event.key == pygame.K_d and not (MOVplay1 == 'l'):
                    x1 = (LENGTH)
                    y1 = 0
                    MOVplay1 = 'r'
                if event.key == pygame.K_w and not (MOVplay1 == 'd'):
                    x1 = 0
                    y1 = (HEIGHT) * -1
                    MOVplay1 = 'u'
                if event.key == pygame.K_s and not (MOVplay1 == 'u'):
                    x1 = 0
                    y1 = (HEIGHT)
                    MOVplay1 = 'd'

                # Controlling the movements of the second bike with the keys: Left, Right, Up and Down
                if event.key == pygame.K_LEFT and not (MOVplay2 == 'r'):              
                    x2 = (LENGTH) * -1
                    y2 = 0
                    MOVplay2 = 'l'
                if event.key == pygame.K_RIGHT and not (MOVplay2 == 'l'):
                    x2 = (LENGTH)
                    y2 = 0
                    MOVplay2 = 'r'
                if event.key == pygame.K_UP and not (MOVplay2 == 'd'):
                    x2 = 0
                    y2 = (HEIGHT) * -1
                    MOVplay2 = 'u'
                if event.key == pygame.K_DOWN and not (MOVplay2 == 'u'):
                    x2 = 0
                    y2 = (HEIGHT)
                    MOVplay2 = 'd'
                                 
        # Establishing each new position for the 'head' of bike1
        x01 = bike1.rect.x + x1
        y01 = bike1.rect.y + y1
        bike1 = Bike(PLAYER1, x01, y01)

        # Establishing each new position for the 'head' of bike2
        x02 = bike2.rect.x + x2
        y02 = bike2.rect.y + y2
        bike2 = Bike(PLAYER2, x02, y02)
         
        # Inserting each new sprite of bike1 in its respective list
        list_first_bike.add(bike1)
        list_of_all_sprites.add(bike1)

        # Inserting each new sprite of bike2 in its respective list
        list_first_bike.add(bike2)
        list_of_all_sprites.add(bike2)
            
        # Filling the screen with the grid image
        screen.blit(gridImg, (0,0))
        
        # Drawing all the sprites (for the 2 bikes)
        list_of_all_sprites.draw(screen)
                  
        # Updating the screen with the new changes
        pygame.display.flip()
          
        # Defining the game speed
        clock.tick(15)

"""
FUNCTION FOR RESTARTING THE GAME
"""

def playGame():
    try:
        initialValues()
        game()
    #Avoiding the error generated for stopping the rectangle drawing method
    except AttributeError :
        pass

# Initializing music for the game    
gridSound = pygame.mixer.Sound('grid.ogg')
gridSound.play(-1) 
playing = True

playGame()

"""
LOOP CREATED TO WAIT FOR THE INPUT OF THE USER BETWEEN RESTART OR QUIT
"""

while playing:
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Key code ' space bar' to restart the game
            if event.key == pygame.K_SPACE:
                playGame()
            # Key code 'q' to end the game and show the goodbye screen for 2 seconds
            if event.key == pygame.K_q:
                playing = False
                quitImg = pygame.image.load('quit.jpg')
                screen.blit(quitImg, (0, 0))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
