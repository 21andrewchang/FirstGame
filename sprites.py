import pygame
from config import *
import math
import random


class Player(pygame.sprite.Sprite): # pygame.sprite.Sprite makes it easier to make sprites
    def __init__(self, game, x, y): # pass in game to access variables defined there
        self.game = game
        self._layer = PLAYER_LAYER # tells pygame what layer we want this sprite to be in
        self.groups = self.game.all_sprites # adds player to all_sprites group 
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        # movement
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'

        # color_changing
        self.next_change = 0

        '''
        Set player graphics
            - in pygame, each sprite has an image and a rect
            - image: what it looks like
            - rect: hitbox
        '''
        # image_to_load = pygame.image.load("assets")
        self.image = pygame.Surface([self.width, self.height]) # creates 32x32 rectangle 
        self.image.fill(WHITE)
        self.rect  = self.image.get_rect() # sets hitbox same size as image
        self.rect.x = self.x
        self.rect.y = self.y

    def changeColors(self):
        changes = random.random()
        current_time = pygame.time.get_ticks()
        if self.next_change == 0:
            self.next_change = current_time
        if current_time - self.next_change >= 0:
            if changes < 0.5:
                self.image.fill(RED)
            else:
                self.image.fill(WHITE)
            self.next_change = current_time + 1000 # 1 second

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide('x')
        self.rect.y += self.y_change
        self.collide('y')
        self.x_change = 0
        self.y_change = 0
        self.changeColors()

    def collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def movement(self):
        keys = pygame.key.get_pressed() # stored list of every key pressed on your keyboard
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width =TILE_SIZE
        self.height =TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WALL)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

