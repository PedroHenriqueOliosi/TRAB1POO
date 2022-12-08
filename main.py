import pygame as pg
from sprites import *
from config import *
import sys
from cronometro import *


class Game:
    def __init__ (self):
        pg.init()
        self.screen = pg.display.set_mode((LARGURA, ALTURA))
        self.clock = pg.time.Clock()
        self.cronometro = Cronometro()
        self.running = True
        self.intro = True
        self.lore = True
        self.font = pg.font.Font("ibagens\Fonte_jogo.TTF", 34)
        self.little_font = pg.font.Font("ibagens\Fontinha_jogo.TTF", 14)

        self.character_spritesheet = Spritesheet('ibagens\character.png')
        self.terrain_spritesheet = Spritesheet('ibagens\Terrain.png')
        self.enemy_spritesheet = Spritesheet('ibagens\enemy.png')
        self.attack_spritesheet = Spritesheet('ibagens\Attack.png')
        self.explosion_spritesheet = Spritesheet('ibagens\explosion.png')
        self.intro_background = pg.image.load('ibagens\introbackground.png')
        self.papiro = pg.image.load('ibagens\papiro.png')
        self.papiro = pg.transform.scale(self.papiro, (580, 451))

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "O":
                    Obstacle(self, j, i)
                if column == "W":
                    Water(self, j, i)       
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
            self.explosion = pg.sprite.LayeredUpdates()
            self.obstacle = pg.sprite.LayeredUpdates()
            self.water = pg.sprite.LayeredUpdates()
            
        
            self.createTilemap()
            
    def events(self):
        #game loop events
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.playing = False
                self.running = False
                sys.exit(0)
                
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

                if event.key == pg.K_e:
                    Explosion(self, self.player2.rect.x, self.player2.rect.y, self.player)
    
                if event.key == pg.K_u:
                    Explosion(self, self.player.rect.x, self.player.rect.y, self.player2)
    
    def update (self):
        self.all_sprites.update()

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
                    sys.exit(0)

            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro = False
                self.lore = False
                self.new()
            if lore_button.is_pressed(mouse_pos, mouse_pressed):
                self.lore = True
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

        intro_button = Button(LARGURA*0.8, ALTURA*0.9, 100, 50, WHITE, BLACK, 'Back', 18)
        frase_1 = Phrase(0, 0, 700, 220, BLACK, 'O MAR MEDITERRANEO,', 10)
        frase_2 = Phrase(0, 0, 700, 260, BLACK, 'CRIPTA DE NAUFRAGOS,', 10)
        frase_3 = Phrase(0, 0, 700, 300, BLACK, 'PRESENCIOU A ASCENCAO E A QUEDA', 10)
        frase_4 = Phrase(0, 0, 700, 340, BLACK, 'DE DIVERSOS IMPERIOS.', 10)
        frase_5 = Phrase(0, 0, 700, 380, BLACK, 'MAS NO SECULO VIII, O MAR', 10)
        frase_6 = Phrase(0, 0, 700, 420, BLACK, 'FOI ESPECIALMENTE MARCADO PELA', 10)
        frase_7 = Phrase(0, 0, 700, 460, BLACK, 'GUERRA QUE ECOLDIU PARA DEFINIR', 10)
        frase_8 = Phrase(0, 0, 700, 500, BLACK, 'O CONTROLE DA PENISULA IBERICA.', 10)
        frase_9 = Phrase(0, 0, 700, 540, BLACK, 'BERBERES E MOUROS,', 10)
        frase_10 = Phrase(0, 0, 700, 580, BLACK, 'VISIGODOS E ANDALUZES', 10)
        frase_11 = Phrase(0, 0, 700, 620, BLACK, 'TRAVARAM SECULOS DE BATALHA', 10)
        frase_12 = Phrase(0, 0, 700, 660, BLACK, 'PELA DISPUTA DO TERRITORIO. AGORA,', 10)
        frase_13 = Phrase(0, 0, 700, 700, BLACK, 'ESCOLHA SEU LADO NESSA BATALHA', 10)
        frase_14 = Phrase(0, 0, 700, 740, BLACK, 'E LUTE PELO DESTINO DA HISTORIA!', 10)

        while self.lore:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.lore = False
                    self.running = False
                    sys.exit(0)
            
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if intro_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro = True
                self.lore = False
                self.intro_screen()

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(self.papiro, (LARGURA*0.08, ALTURA*0.05))
            self.screen.blit(title, title_rect)
            self.screen.blit(intro_button.image, intro_button.rect)
            self.screen.blit(frase_1.image, frase_1.rect)
            self.screen.blit(frase_2.image, frase_2.rect)
            self.screen.blit(frase_3.image, frase_3.rect)
            self.screen.blit(frase_4.image, frase_4.rect)
            self.screen.blit(frase_5.image, frase_5.rect)
            self.screen.blit(frase_6.image, frase_6.rect)
            self.screen.blit(frase_7.image, frase_7.rect)
            self.screen.blit(frase_8.image, frase_8.rect)
            self.screen.blit(frase_9.image, frase_9.rect)
            self.screen.blit(frase_10.image, frase_10.rect)
            self.screen.blit(frase_11.image, frase_11.rect)
            self.screen.blit(frase_12.image, frase_12.rect)
            self.screen.blit(frase_13.image, frase_13.rect)
            self.screen.blit(frase_14.image, frase_14.rect)

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