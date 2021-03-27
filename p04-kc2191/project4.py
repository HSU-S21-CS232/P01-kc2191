import pygame
import random

#initialize the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((1000, 800))

#background
background = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/background.jpg")

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
enemyimg = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/devil.png")
enemyX = random.randint(0, 1000)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

#bullet
#ready = no bullet on screen
#fire = the bullet is moving
bulletimg = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/gems.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(playerimg, (x, y))

def enemy(x,y):
    screen.blit(enemyimg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16,y+10))

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

    enemyX += enemyX_change

    #enemy movement
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 936:
        enemyX_change = -4
        enemyY += enemyY_change

    #bullet movement
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()   