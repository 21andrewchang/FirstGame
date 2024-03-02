import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def createTilemap(self):
        for i, row in enumerate(TILE_MAP):
            for j, col in enumerate(row):
                if col == "B":
                    Block(self, j, i)
                if col == "P":
                    Player(self, j, i)
                if col == "E":
                    Enemy(self, j, i, 'left')
                if col == "H":
                    House(self, j, i)
                if col == ".":
                    Ground(self, j, i)

    def new(self):
        self.playing = True
        # empty groups that we can add our sprites into later
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates() # where walls are stored
        self.enemies = pygame.sprite.LayeredUpdates() # where enemies are stored
        self.attacks = pygame.sprite.LayeredUpdates() # where attack animations are stored
        self.createTilemap()
        self.center()

    # contains keypress events
    def events(self):
        for event in pygame.event.get():
            # press close button
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    # updates game so its not just a static image
    def update(self):
        # calls the update method of every sprite in all_sprites
        self.all_sprites.update()

    def center(self):
        player = self.player.get_sprite(0)
        x_diff = player.rect.center[0] - self.screen.get_rect().center[0]
        y_diff = player.rect.center[1] - self.screen.get_rect().center[1]
        for sprite in self.all_sprites:
            sprite.rect.x -= x_diff
            sprite.rect.y -= y_diff

    # displays sprites onto our screen
    def draw(self):
        self.screen.fill(BLACK)
        # walks through every sprite in all_sprites and draws the rect onto our window
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
    # game loop 
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()

