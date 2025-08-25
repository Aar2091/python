import math
import random
import pygame

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y = 50
ENEMY_START_Y = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 10
BULLET_SPEED_Y = 20
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN HIEGHT))

baground = pygame.image.load('baground.png')

pygame.display.set_captiom("Space Invader")
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('olayer.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerx_change = 0

