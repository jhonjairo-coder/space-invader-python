import pygame
import random

# inicialize de pygame
pygame.init()

# create de screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('back.png')

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 539
playerX_change = 0

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# game loop
running = True
while running:
    # RGB - Red , Green, Blue
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keystroke right of left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,playerY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # movimiento de jugador
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # movimiento del enemigo
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    #bullet movement


    if bullet_state is "fire":
        fire_bullet(playerX,playerY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
