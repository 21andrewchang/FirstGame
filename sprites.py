import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite): # pygame.sprite.Sprite makes it easier to make sprites
    def __init__(self, game, x, y): # pass in game to access variables defined there
        self.game = game
        self._layer = PLAYER_LAYER # tells pygame what layer we want this sprite to be in
        self.groups = self.game.all_sprites, self.game.player # adds player to all_sprites group 
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
        image_to_load = pygame.image.load("./assets/bondosan.png")
        image_to_load = pygame.transform.scale(image_to_load, (64,64))
        self.image = pygame.Surface([self.width, self.height]) # creates 32x32 rectangle 
        self.image.blit(image_to_load, (0,0))

        # hitbox
        self.rect  = self.image.get_rect() # sets hitbox same size as image
        self.rect.x = self.x
        self.rect.y = self.y

        # x_diff = self.rect.center[0] - self.game.screen.get_rect().center[0]
        # y_diff = self.rect.center[1] - self.game.screen.get_rect().center[1]


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



        # self.changeColors()

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
        # player_center = self.rect.center

        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
                print(sprite.rect.x)
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, facing):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.facing = facing
        self.x_change = 0

        image_to_load = pygame.image.load("./assets/penginsan.jpg")
        image_to_load = pygame.transform.scale(image_to_load, (32, 32))
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(WHITE)
        self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement(self.facing)
        self.rect.x += self.x_change
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            if self.x_change > 0:
                self.rect.x = hits[0].rect.left - self.rect.width
                self.facing = 'left'
            if self.x_change < 0:
                self.rect.x = hits[0].rect.right
                self.facing = 'right'

    def movement(self, facing):
        if facing == 'left':
            self.x_change = -ENEMY_SPEED
        if facing == 'right':
            self.x_change = ENEMY_SPEED




        
class House(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE * 5
        self.height = TILE_SIZE * 5

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width =TILE_SIZE
        self.height =TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

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

