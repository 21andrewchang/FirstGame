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

        '''
        Set player graphics
            - in pygame, each sprite has an image and a rect
            - image: what it looks like
            - rect: hitbox
        '''
        self.image = pygame.Surface([self.width, self.height]) # creates 32x32 rectangle 
        self.image.fill(WHITE)
        self.rect  = self.image.get_rect() # sets hitbox same size as image
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass
