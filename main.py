import pygame as pg
from time import time
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

        #personagens
        self.character_spritesheet = Spritesheet('ibagens\character.png')
        self.character_2_spritesheet = Spritesheet('ibagens\character.png')
        self.enemy_spritesheet = Spritesheet('ibagens\enemy.png')
        self.mouro_spritesheet = Spritesheet('ibagens\Mouro.png')
        self.berbere_spritesheet = Spritesheet('ibagens\Berbero.png')
        self.andaluz_spritesheet = Spritesheet('ibagens\Andaluz.png')
        self.visigodo_spritesheet = Spritesheet('ibagens\Visigodo.png')
        
        #terrenos
        self.terrain_spritesheet = Spritesheet('ibagens\Terrain.png')
        
        #ataques
        self.attack_spritesheet = Spritesheet('ibagens\Attack.png')
        self.explosion_spritesheet = Spritesheet('ibagens\explosion.png')
        
        #cenas
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
                    self.player = Player(self, j, i, 100, 0.2)
                if column == '2':
                    self.player2 = Player2(self, j, i, 100, 0.2)
                if column == 'p':
                    Placar(self, j, i, self.player, self.player.maximum_health)
                if column == 'l':
                    Placar2(self, j, i, self.player2, self.player2.maximum_health)
    
    def new(self):

            self.playing = True

            self.all_sprites = pg.sprite.LayeredUpdates()
            self.character = pg.sprite.LayeredUpdates()
            self.character2 = pg.sprite.LayeredUpdates()
            self.blocks = pg.sprite.LayeredUpdates()
            self.enemies = pg.sprite.LayeredUpdates()
            self.attacks = pg.sprite.LayeredUpdates()
            self.healthbar = pg.sprite.LayeredUpdates()
            self.explosion = pg.sprite.LayeredUpdates()
            self.obstacle = pg.sprite.LayeredUpdates()
            self.water = pg.sprite.LayeredUpdates()
            self.arrow = pg.sprite.LayeredUpdates()
            self.Auto_heal = pg.sprite.LayeredUpdates()
            
        
            self.createTilemap()
            
    def events(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.playing = False
                self.running = False
                sys.exit(0)
                
            if event.type == pg.KEYDOWN:
                if self.visigodo_1 == True:
                    if event.key == pg.K_q:
                        if self.player.facing == 'up':
                            Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE, self.player)
                        if self.player.facing == 'down':
                            Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE, self.player)
                        if self.player.facing == 'left':
                            Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y, self.player)
                        if self.player.facing == 'right':
                            Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y, self.player)

                    if event.key == pg.K_e:
                        if self.player.facing == 'up':
                            Auto_heal(self, self.player.rect.x, self.player.rect.y, self.player, 'up')
                        if self.player.facing == 'down':
                            Auto_heal(self, self.player.rect.x, self.player.rect.y, self.player, 'down')
                        if self.player.facing == 'left':
                            Auto_heal(self, self.player.rect.x, self.player.rect.y, self.player, 'left')
                        if self.player.facing == 'right':
                            Auto_heal(self, self.player.rect.x, self.player.rect.y, self.player, 'right')

                if self.berbere_1 == True:
                    if event.key == pg.K_q:
                        if self.player.facing == 'up':
                            Arrow(self, self.player.rect.x, self.player.rect.y - TILESIZE, self.player, 'up')
                        if self.player.facing == 'down':
                            Arrow(self, self.player.rect.x, self.player.rect.y + TILESIZE, self.player, 'down')
                        if self.player.facing == 'left':
                            Arrow(self, self.player.rect.x - TILESIZE, self.player.rect.y, self.player, 'left')
                        if self.player.facing == 'right':
                            Arrow(self, self.player.rect.x + TILESIZE, self.player.rect.y, self.player, 'right')
                    
                    if event.key == pg.K_e:
                        Explosion(self, self.player2.rect.x, self.player2.rect.y, self.player)
                
                if self.andaluz_1 == True:
                    if event.key == pg.K_q:
                        if self.player.facing == 'up':
                            Arrow(self, self.player.rect.x, self.player.rect.y - TILESIZE, self.player, 'up')
                        if self.player.facing == 'down':
                            Arrow(self, self.player.rect.x, self.player.rect.y + TILESIZE, self.player, 'down')
                        if self.player.facing == 'left':
                            Arrow(self, self.player.rect.x - TILESIZE, self.player.rect.y, self.player, 'left')
                        if self.player.facing == 'right':
                            Arrow(self, self.player.rect.x + TILESIZE, self.player.rect.y, self.player, 'right')
                    
                    if event.key == pg.K_e:
                        Explosion(self, self.player2.rect.x, self.player2.rect.y, self.player)
                
                if self.mouro_1 == True:
                    if event.key == pg.K_q:
                        if self.player.facing == 'up':
                            Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE, self.player)
                        if self.player.facing == 'down':
                            Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE, self.player)
                        if self.player.facing == 'left':
                            Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y, self.player)
                        if self.player.facing == 'right':
                            Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y, self.player)
                    
                    if event.key == pg.K_e:
                        Explosion(self, self.player2.rect.x, self.player2.rect.y, self.player)

                if self.visigodo_2 == True:
                    if event.key == pg.K_u:
                        if self.player2.facing == 'up':
                            Attack(self, self.player2.rect.x, self.player2.rect.y - TILESIZE, self.player2)
                        if self.player2.facing == 'down':
                            Attack(self, self.player2.rect.x, self.player2.rect.y + TILESIZE, self.player2)
                        if self.player2.facing == 'left':
                            Attack(self, self.player2.rect.x - TILESIZE, self.player2.rect.y, self.player2)
                        if self.player2.facing == 'right':
                            Attack(self, self.player2.rect.x + TILESIZE, self.player2.rect.y, self.player2)

                    if event.key == pg.K_o:
                        if self.player2.facing == 'up':
                            Auto_heal(self, self.player2.rect.x, self.player2.rect.y, self.player2, 'up')
                        if self.player2.facing == 'down':
                            Auto_heal(self, self.player2.rect.x, self.player2.rect.y, self.player2, 'down')
                        if self.player2.facing == 'left':
                            Auto_heal(self, self.player2.rect.x, self.player2.rect.y, self.player2, 'left')
                        if self.player2.facing == 'right':
                            Auto_heal(self, self.player2.rect.x, self.player2.rect.y, self.player2, 'right')

                if self.berbere_2 == True:
                    if event.key == pg.K_u:
                        if self.player2.facing == 'up':
                            Arrow(self, self.player2.rect.x, self.player2.rect.y - TILESIZE, self.player2, 'up')
                        if self.player2.facing == 'down':
                            Arrow(self, self.player2.rect.x, self.player2.rect.y + TILESIZE, self.player2, 'down')
                        if self.player2.facing == 'left':
                            Arrow(self, self.player2.rect.x - TILESIZE, self.player2.rect.y, self.player2, 'left')
                        if self.player2.facing == 'right':
                            Arrow(self, self.player2.rect.x + TILESIZE, self.player2.rect.y, self.player2, 'right')
                    
                    if event.key == pg.K_o:
                        Explosion(self, self.player.rect.x, self.player.rect.y, self.player2)
                
                if self.andaluz_2 == True:
                    if event.key == pg.K_u:
                        if self.player2.facing == 'up':
                            Arrow(self, self.player2.rect.x, self.player2.rect.y - TILESIZE, self.player2, 'up')
                        if self.player2.facing == 'down':
                            Arrow(self, self.player2.rect.x, self.player2.rect.y + TILESIZE, self.player2, 'down')
                        if self.player2.facing == 'left':
                            Arrow(self, self.player2.rect.x - TILESIZE, self.player2.rect.y, self.player2, 'left')
                        if self.player2.facing == 'right':
                            Arrow(self, self.player2.rect.x + TILESIZE, self.player2.rect.y, self.player2, 'right')
                    
                    if event.key == pg.K_o:
                        Explosion(self, self.player.rect.x, self.player.rect.y, self.player2)
                
                if self.mouro_2 == True:
                    if event.key == pg.K_u:
                        if self.player2.facing == 'up':
                            Attack(self, self.player2.rect.x, self.player2.rect.y - TILESIZE, self.player2)
                        if self.player2.facing == 'down':
                            Attack(self, self.player2.rect.x, self.player2.rect.y + TILESIZE, self.player2)
                        if self.player2.facing == 'left':
                            Attack(self, self.player2.rect.x - TILESIZE, self.player2.rect.y, self.player2)
                        if self.player2.facing == 'right':
                            Attack(self, self.player2.rect.x + TILESIZE, self.player2.rect.y, self.player2)
                    
                    if event.key == pg.K_o:
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
                self.selection_screen_1()

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

    def selection_screen_1 (self):
        
        self.animation_loop = 1
        self.selection_1 = True
        self.selection_2 = False

        self.visigodo_1 = False
        self.andaluz_1 = False
        self.berbere_1 = False
        self.mouro_1 = False

        title = self.font.render('1- Escolha seu char', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        for i in range (300):
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

        visigodo_button = Button(LARGURA*0.15, ALTURA*0.6, 200, 50, WHITE, BLACK, 'Visigodo', 18)
        visigodo_select_animation = [self.visigodo_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.visigodo_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.visigodo_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.visigodo_animation = visigodo_select_animation[math.floor(self.animation_loop)]

        andaluz_button = Button(LARGURA*0.15, ALTURA*0.3, 200, 50, WHITE, BLACK, 'Andaluz', 18)
        andaluz_select_animation = [self.andaluz_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.andaluz_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.andaluz_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.andaluz_animation = andaluz_select_animation[math.floor(self.animation_loop)]

        berbere_button = Button(LARGURA*0.5, ALTURA*0.6, 200, 50, WHITE, BLACK, 'Berbere', 18)
        berbere_select_animation = [self.berbere_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.berbere_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.berbere_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.berbere_animation = berbere_select_animation[math.floor(self.animation_loop)]

        mouro_button = Button(LARGURA*0.5, ALTURA*0.3, 200, 50, WHITE, BLACK, 'Mouro', 18)
        mouro_select_animation = [self.mouro_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.mouro_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.mouro_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.mouro_animation = mouro_select_animation[math.floor(self.animation_loop)]


        while self.selection_1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.selection_screen_1 = False
                    self.running = False
                    sys.exit(0)
            
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()
            pg.time.delay(100)

            if visigodo_button.is_pressed(mouse_pos, mouse_pressed):
                print("iu")
                self.character_spritesheet = Spritesheet('ibagens\Visigodo.png')
                self.visigodo_1 = True
                self.selection_2 = True
                self.selection_1 = False
                self.selection_screen_2()
            
            if andaluz_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_spritesheet = Spritesheet('ibagens\Andaluz.png')
                self.andaluz_1 = True
                self.selection_2 = True
                self.selection_1 = False
                self.selection_screen_2()
            
            if berbere_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_spritesheet = Spritesheet('ibagens\Berbero.png')
                self.berbere_1 = True
                self.selection_2 = True
                self.selection_1 = False
                self.selection_screen_2()
            
            if mouro_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_spritesheet = Spritesheet('ibagens\Mouro.png')
                self.mouro_1 = True
                self.selection_2 = True
                self.selection_1 = False
                self.selection_screen_2()

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(visigodo_button.image, visigodo_button.rect)
            self.screen.blit(andaluz_button.image, andaluz_button.rect)
            self.screen.blit(berbere_button.image, berbere_button.rect)
            self.screen.blit(mouro_button.image, mouro_button.rect)
            self.screen.blit(self.visigodo_animation, (LARGURA*0.28, ALTURA*0.72))
            self.screen.blit(self.andaluz_animation, (LARGURA*0.28, ALTURA*0.42))
            self.screen.blit(self.berbere_animation, (LARGURA*0.61, ALTURA*0.72))
            self.screen.blit(self.mouro_animation, (LARGURA*0.61, ALTURA*0.42))

            self.clock.tick(FPS)
            pg.display.update()


    def selection_screen_2 (self):
        
        self.animation_loop = 1

        self.visigodo_2 = False
        self.andaluz_2 = False
        self.berbere_2 = False
        self.mouro_2 = False

        title = self.font.render('2- Escolha seu char', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        for i in range (300):
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

        visigodo_button = Button(LARGURA*0.15, ALTURA*0.6, 200, 50, WHITE, BLACK, 'Visigodo', 18)
        visigodo_select_animation = [self.visigodo_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.visigodo_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.visigodo_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.visigodo_animation = visigodo_select_animation[math.floor(self.animation_loop)]

        andaluz_button = Button(LARGURA*0.15, ALTURA*0.3, 200, 50, WHITE, BLACK, 'Andaluz', 18)
        andaluz_select_animation = [self.andaluz_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.andaluz_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.andaluz_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.andaluz_animation = andaluz_select_animation[math.floor(self.animation_loop)]

        berbere_button = Button(LARGURA*0.5, ALTURA*0.6, 200, 50, WHITE, BLACK, 'Berbere', 18)
        berbere_select_animation = [self.berbere_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.berbere_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.berbere_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.berbere_animation = berbere_select_animation[math.floor(self.animation_loop)]

        mouro_button = Button(LARGURA*0.5, ALTURA*0.3, 200, 50, WHITE, BLACK, 'Mouro', 18)
        mouro_select_animation = [self.mouro_spritesheet.get_sprite(3, 2, TILESIZE, TILESIZE),
                           self.mouro_spritesheet.get_sprite(35, 2, TILESIZE, TILESIZE),
                           self.mouro_spritesheet.get_sprite(68, 2, TILESIZE, TILESIZE)]
        self.mouro_animation = mouro_select_animation[math.floor(self.animation_loop)]


        while self.selection_2:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.selection_screen_2 = False
                    self.running = False
                    sys.exit(0)
            
            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if visigodo_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_2_spritesheet = Spritesheet('ibagens\Visigodo.png')
                self.visigodo_2 = True
                self.selection_2 = False
                self.selection_1 = False
                self.new()
            
            if andaluz_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_2_spritesheet = Spritesheet('ibagens\Andaluz.png')
                self.andaluz_2 = True
                self.selection_2 = False
                self.selection_1 = False
                self.new()
            
            if berbere_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_2_spritesheet = Spritesheet('ibagens\Berbero.png')
                self.berbere_2 = True
                self.selection_2 = False
                self.selection_1 = False
                self.new()
            
            if mouro_button.is_pressed(mouse_pos, mouse_pressed):
                self.character_2_spritesheet = Spritesheet('ibagens\Mouro.png')
                self.mouro_2 = True
                self.selection_2 = False
                self.selection_1 = False
                self.new()

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(visigodo_button.image, visigodo_button.rect)
            self.screen.blit(andaluz_button.image, andaluz_button.rect)
            self.screen.blit(berbere_button.image, berbere_button.rect)
            self.screen.blit(mouro_button.image, mouro_button.rect)
            self.screen.blit(self.visigodo_animation, (LARGURA*0.28, ALTURA*0.72))
            self.screen.blit(self.andaluz_animation, (LARGURA*0.28, ALTURA*0.42))
            self.screen.blit(self.berbere_animation, (LARGURA*0.61, ALTURA*0.72))
            self.screen.blit(self.mouro_animation, (LARGURA*0.61, ALTURA*0.42))

            self.clock.tick(FPS)
            pg.display.update()

g = Game()
g.intro_screen()
if g.lore:
    g.lore_screen()
if g.selection_1:
    g.selection_screen_1()

g.new()
while g.running:
    g.main()
    g.game_over()

pg.quit()
sys.exit() 