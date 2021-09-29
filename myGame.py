import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy and prize image). 

player = pygame.image.load("player.jpg")
monster = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
#We get this for the player, enemy and prize characters
player_height = player.get_height()
player_width = player.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()
monster_height = monster.get_height()
monster_width = monster.get_width()

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy and prize characters start off screen and at a random y position.

monsterXPosition =  screen_width
monsterYPosition =  random.randint(0, screen_height - monster_height)

monster2XPosition =  screen_width
monster2YPosition =  random.randint(0, screen_height - monster_height)

monster3XPosition =  screen_width
monster3YPosition =  random.randint(0, screen_height - monster_height)

prizeXPosition =  screen_width
prizeYPosition =  random.randint(0, screen_height - prize_height)

# This checks if the up, down, left, right keys are pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

   
    screen.fill(0) # Clears the screen.
    
    screen.blit(player, (playerXPosition, playerYPosition)) # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(monster, (monsterXPosition, monsterYPosition))  #Similarly, this draws the first enemy image to the screen at the postion specfied. 
    monsterXPosition -= 0.15 #This moves the first enemy character across the screen

    if monsterXPosition < 0 - monster_width: #If the first enemy successfully moves across the screen, we trigger the second enemy to be drawn
        screen.blit(monster, (monster2XPosition, monster2YPosition)) #This draws the second enemy image to the screen at the postion specfied. 
        monster2XPosition -= 0.3 #This moves the second enemy character across the screen

    if monster2XPosition < 0 - monster_width: #If the second enemy successfully moves across the screen, we trigger the third enemy to be drawn
        screen.blit(monster, (monster3XPosition, monster3YPosition)) #This draws the third enemy image to the screen at the postion specfied.
        monster3XPosition -= 0.45 #This moves the third enemy character across the screen

    if monster3XPosition < 0 - monster_width:  #If the third enemy successfully moves across the screen, we trigger the prize character to be drawn
        screen.blit(prize, (prizeXPosition, prizeYPosition)) #This draws the prize image to the screen at the postion specfied.
        prizeXPosition -= 0.6 #This moves the prize character across the screen


    pygame.display.flip() # This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        
        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyRight == True:
        if playerXPosition < screen_width - player_width : # This makes sure that the user does not move the player too far right of the window.
            playerXPosition += 1
    if keyLeft == True:
        #if playerXPosition < screen_width - player_width:# This makes sure that the user does not move the player too far left of the window.
        if playerXPosition > 0:    
            playerXPosition -= 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    monster2Box = pygame.Rect(monster.get_rect())
    monster2Box.top = monster2YPosition
    monster2Box.left = monster2XPosition

    monster3Box = pygame.Rect(monster.get_rect())
    monster3Box.top = monster3YPosition
    monster3Box.left = monster3XPosition

    # Bounding box for the enemy:

    prizeBox = pygame.Rect(monster.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(monsterBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(monster2Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


    if playerBox.colliderect(monster3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


    if playerBox.colliderect(prizeBox): #If the user collides with the prize, they win
    
        # Display Winning status to the user: 
        
        print("You Win!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
             
    # ================The game loop logic ends here. =============
  
