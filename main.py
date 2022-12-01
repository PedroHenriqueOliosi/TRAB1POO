import pygame as pg
from sprites import *
from config import *
import sys
from time import time

class Cronometro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tempo_referencia = time()

    def tempo_passado(self):
        tempo_atual = time()
        return tempo_atual - self.tempo_referencia

class Game:
    def __init__ (self):
        pg.init()
        self.screen = pg.display.set_mode((LARGURA, ALTURA))
        self.clock = pg.time.Clock()
        self.running = True
        self.intro = True
        self.lore = True
        self.font = pg.font.Font("ibagens\Fonte_jogo.TTF", 34)
        self.little_font = pg.font.Font("ibagens\Fontinha_jogo.TTF", 14)

        self.character_spritesheet = Spritesheet('ibagens\character.png')
        self.terrain_spritesheet = Spritesheet('ibagens\Terrain.png')
        self.enemy_spritesheet = Spritesheet('ibagens\enemy.png')
        self.attack_spritesheet = Spritesheet('ibagens\Attack.png')
        self.intro_background = pg.image.load('ibagens\introbackground.png')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == '2':
                    self.player2 = Player2(self, j, i)

    def new(self):

            self.playing = True

            self.all_sprites = pg.sprite.LayeredUpdates()
            self.blocks = pg.sprite.LayeredUpdates()
            self.enemies = pg.sprite.LayeredUpdates()
            self.attacks = pg.sprite.LayeredUpdates()
            self.fireballs = pg.sprite.LayeredUpdates()
        
            self.createTilemap()
            
    def events(self):
        #game loop events
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.playing = False
                self.running = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE, self.player)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE, self.player)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y, self.player)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y, self.player)
                
                if event.key == pg.K_SPACE:
                    if self.player2.facing == 'up':
                        Attack(self, self.player2.rect.x, self.player2.rect.y - TILESIZE, self.player2)
                    if self.player2.facing == 'down':
                        Attack(self, self.player2.rect.x, self.player2.rect.y + TILESIZE, self.player2)
                    if self.player2.facing == 'left':
                        Attack(self, self.player2.rect.x - TILESIZE, self.player2.rect.y, self.player2)
                    if self.player2.facing == 'right':
                        Attack(self, self.player2.rect.x + TILESIZE, self.player2.rect.y, self.player2)
    
    def update (self):
        self.all_sprites.update()
        #o vscode deu problema quando botei "self.all_sprites.update()", achei muito esquisito

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pg.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):

        title = self.font.render('Joguissimo', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 76, 100, 50, WHITE, BLACK, 'Play', 18)
        lore_button = Button(10, 140, 100, 50, WHITE, BLACK, 'Lore', 18)

        while self.intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.intro = False
                    self.running = False
            
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro = False
                self.lore = False
            if lore_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro = False


            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(lore_button.image, lore_button.rect)

            self.clock.tick(FPS)
            pg.display.update()

    def lore_screen (self):

        title = self.font.render('Lore', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        intro_button = Button(10, 76, 100, 50, WHITE, BLACK, 'Back', 18)

        while self.lore:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if intro_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro_screen()
                self.lore = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(intro_button.image, intro_button.rect)

            self.clock.tick(FPS)
            pg.display.update()

g = Game()
g.intro_screen()
if g.lore:
    g.lore_screen()

g.new()
while g.running:
    g.main()
    g.game_over()

pg.quit()
sys.exit() 