import pygame as pg
from config import *
import math
import random

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        #temporary variables that will store the mov change every loop
        self.x_change = 0
        self.y_change = 0

        #orientation of the player
        self.facing = 'down'

        self.image = pg.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
             self.x_change -= PLAYER_SPEED
             self.facing = 'left'
             print(self.facing)
        if keys[pg.K_d]:
             self.x_change += PLAYER_SPEED
             self.facing = 'right'
             print(self.facing)
        if keys[pg.K_s]:
             self.y_change += PLAYER_SPEED
             self.facing = 'down'
             print(self.facing)
        if keys[pg.K_w]:
             self.y_change -= PLAYER_SPEED
             self.facing = 'up'
             print(self.facing)

class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pg.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        