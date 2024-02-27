import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arial', 32)
        self.running = True

    def new(self):
        self.playing = True

        # empty groups that we can add our sprites into later
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates() # where walls are stored
        self.enemies = pygame.sprite.LayeredUpdates() # where enemies are stored
        self.attacks = pygame.sprite.LayeredUpdates() # where attack animations are stored

        self.player = Player


    def update(self):

    def draw(self):

    def main(self):

    def game_over(self):

    def intro_screen(self):


