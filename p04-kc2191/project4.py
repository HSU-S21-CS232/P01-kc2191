import pygame
from pygame import mixer

import random
import math

#initialize the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((1000, 800))

#background
background = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/background.jpg")


#background sound
mixer.music.load("/Users/kevinchung/KC2191/p04-kc2191/spaceoddity.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders!")
icon = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/planetsmall.png")
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/space-invaders.png")
playerX = 370
playerY = 650
playerX_change = 0

#enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyimg.append(pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/devil.png"))
    enemyX.append(random.randint(0, 937))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
#ready = no bullet on screen
#fire = the bullet is moving
bulletimg = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/gems.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x,y):
    score = font.render("Annihalations : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("TO THE NEXT DIMENSION : ", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16,y+10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop: if you want to move objects in the game, manipulate this loop
running = True
while running:

    #RGBB: red, green, blue (cannot be more than 255)
    screen.fill((0, 0, 128))

    #background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    #bullet_Sound = mixer.Sound(file)
                    #bullet_Sound.play()
                    #this gets the current x-coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    #movement, baby
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936


    #enemy movement
    for i in range(num_of_enemies):

        #game over
        if enemyY[i] > 600:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 936:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        #collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
           #collision_Sound = mixer.Sound(file)
            #collision_Sound.play() 
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 1000)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)



    #bullet movement
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()   


    #i want the enemies to be more spread out
    #after getting 10 kills, i want to be teleported to a different location
    #i then want different enemies