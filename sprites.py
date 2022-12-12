import pygame as pg
from config import *
from cronometro import * 
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(WHITE)
        
        return sprite

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, health, damage):

        self.game = game
        self.maximum_health = health
        self.current_health = 0
        self.current_health += self.maximum_health
        self.damage = damage
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.character
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3,2, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def get_damage(self, damage):
        if self.current_health > 0:
            self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            self.game.playing = False

    def get_health(self, damage):
        if self.current_health < self.maximum_health:
            self.current_health += damage
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health

    def collide_attack(self):
        hits = pg.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)
    
    def collide_explosion(self):
        hits = pg.sprite.spritecollide(self, self.game.explosion, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)

    def collide_arrow(self):
        hits = pg.sprite.spritecollide(self, self.game.arrow, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)

    def auto_heal(self):
        hits = pg.sprite.spritecollide(self, self.game.Auto_heal, False)
        if hits:
            self.get_health(self.damage)
            print(self.current_health)



    def update(self):
        self.movement()
        self.animate_player()
        self.collide_attack()
        self.collide_explosion()
        self.collide_arrow()
        self.auto_heal()
        self.collide_enemies()
        self.collide_water()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_obstacle('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_obstacle('y')

        self.x_change = 0
        self.y_change = 0

    def moveup(self):
        self.y_change -= self.speed
        self.facing = 'up'
        print(self.facing)

    def movedown(self):
        self.y_change += self.speed
        self.facing = 'down'
        print(self.facing)

    def moveleft(self):
        self.x_change -= self.speed
        self.facing = 'left'
        print(self.facing)
    
    def moveright(self):
        self.x_change += self.speed
        self.facing = 'right'
        print(self.facing)

    def movement(self):
        self.speed = PLAYER_SPEED
        keys = pg.key.get_pressed()

        self.commands = {
            pg.K_w : self.moveup,
            pg.K_s : self.movedown,
            pg.K_a : self.moveleft,
            pg.K_d : self.moveright
        }

        for k, fn in self.commands.items():
            if keys[k]:
                fn()
                
    def collide_enemies(self):
        hits = pg.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)
       

    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.blocks, False) 
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                

        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom      

    def collide_obstacle(self, direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.obstacle, False) 
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                
        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.obstacle, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom  

    def collide_water(self):
        hits = pg.sprite.spritecollide(self, self.game.water, False)
        if hits:
            self.speed = 1
            self.x_change = self.x_change//3
            self.y_change = self.y_change//3
            print(self.speed)

    def animate_player(self):
        down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3,2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3,34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3,98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3,66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
class Player2(Player):
    def __init__(self, game, x, y, health, damage):
        super().__init__(game, x, y, health, damage)
        self.groups = self.game.all_sprites, self.game.character2

        self.image = self.game.character_2_spritesheet.get_sprite(3,2, self.width, self.height)

        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def collide_enemies(self):
        hits = pg.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)

    def collide_attack(self):
        hits = pg.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)

    def collide_explosion(self):
        hits = pg.sprite.spritecollide(self, self.game.explosion, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)

    def collide_arrow(self):
        hits = pg.sprite.spritecollide(self, self.game.arrow, False)
        if hits:
            self.get_damage(self.damage)
            print(self.current_health)

    def auto_heal(self):
        hits = pg.sprite.spritecollide(self, self.game.Auto_heal, False)
        if hits:
            self.get_health(self.damage)
            print(self.current_health)

    def update(self):
        self.movement()
        self.animate_player()
        self.collide_attack()
        self.collide_enemies()
        self.collide_explosion()
        self.collide_arrow()
        self.auto_heal()
        self.collide_enemies()
        self.collide_water()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_obstacle('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_obstacle('y')

        self.x_change = self.y_change = 0

    def movement(self):
        self.speed = PLAYER_SPEED
        keys = pg.key.get_pressed()

        self.commands = {
            pg.K_i : self.moveup,
            pg.K_k : self.movedown,
            pg.K_j : self.moveleft,
            pg.K_l : self.moveright
        }

        for k, fn in self.commands.items():
            if keys[k]:
                fn()
    
    def animate_player(self):
        down_animations = [self.game.character_2_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_2_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_2_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_2_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_2_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_2_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_2_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_2_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_2_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_2_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_2_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_2_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_2_spritesheet.get_sprite(3,2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_2_spritesheet.get_sprite(3,34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_2_spritesheet.get_sprite(3,98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_2_spritesheet.get_sprite(3,66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.collide_down = False
        self.collide_up = False
        self.collide_right = False
        self.collide_left = False

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right', 'up', 'down'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(3, 7)

        self.image = self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.collide_water()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_obstacle('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_obstacle('y')

        self.x_change = 0
        self.y_change = 0
    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.blocks, False) 
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.collide_right = True
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.collide_left = True
                

        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                    self.collide_down = True
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom 
                    self.collide_up = True

    def collide_obstacle(self, direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.obstacle, False) 
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    self.collide_right = True
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    self.collide_left = True
                
        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.obstacle, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                    self.collide_down = True
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    self.collide_up = True

    def collide_water(self):
        hits = pg.sprite.spritecollide(self, self.game.water, False)
        if hits:
            self.speed = 1
            self.x_change = self.x_change//3
            self.y_change = self.y_change//3
            print(self.speed)
            
    def choose_direction(self):
        if self.collide_left:
            self.facing = random.choice(['right', 'up', 'down'])
            self.collide_left = False

        if self.collide_right:
            self.facing = random.choice(['left', 'up', 'down'])
            self.collide_right = False
            
        if self.collide_up:
            self.facing = random.choice(['left', 'right', 'down'])
            self.collide_up = False

        if self.collide_down:
            self.facing = random.choice(['left', 'right', 'up'])
            self.collide_down = False

        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(15, 30)


    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.choose_direction()

        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.choose_direction()

        if self.facing == 'up':
            self.y_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.choose_direction()

        if self.facing == 'down':
            self.y_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop <= self.max_travel:
                self.choose_direction()

    def animate(self):
        down_animations = [self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.enemy_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(68, 34, self.width, self.height)]
        
        left_animations = [self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)]


        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3,2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3,34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3,98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3,66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

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

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pg.font.Font("ibagens\Fontinha_jogo.TTF", fontsize)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.content = content

        self.fg = fg
        self.bg = bg

        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Phrase:
    
    def __init__(self, game, x, y, width, height, content_color, content, fontsize):
        self.font = pg.font.Font("ibagens\Fontinha_jogo.TTF", fontsize)

        self.game = game
        self._layer = PLAYER_LAYER
        self.x = x
        self.y = y
        self._layer = PLAYER_LAYER
        self.width = width
        self.height = height
        self.content = content
        self.fg = content_color

        self.image = pg.Surface((self.width, self.height))
        self.image.fill(WHITE)
        pg.Surface.set_colorkey(self.image, WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

class Attack(pg.sprite.Sprite):
    def __init__(self, game, x, y, player):
    
        self.game = game
        self._layer = PLAYER_LAYER
        self.player = player
        self.groups = self.game.all_sprites, self.game.attacks
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE 
        self.height = TILESIZE

        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide_enemies()
        self.collide_obstacles()

    def collide_enemies(self):
        hits_enemies = pg.sprite.spritecollide(self, self.game.enemies, True)
    
    def collide_obstacles(self):
        hits_obstacle = pg.sprite.spritecollide(self, self.game.obstacle, True)

    def animate(self):
        direction = self.game.player.facing
        direction2 = self.game.player2.facing

        right_animations = [self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

        down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

        left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

        up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]
        
        if self.player == self.game.player:
            if direction == 'up':
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()
            
            if direction == 'down':
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()

            if direction == 'left':
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()

            if direction == 'right':
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()
        
        if self.player == self.game.player2:
            if direction2 == 'up':
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()
            
            if direction2 == 'down':
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()

            if direction2 == 'left':
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()

            if direction2 == 'right':
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.5
                if self.animation_loop >= 5:
                    self.kill()
        
class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.obstacle
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(930, 480, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Water(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WATER_LAYER
        self.groups = self.game.all_sprites, self.game.water
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(865, 160, self.width, self.height)
        self.animation_loop = 0

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
    
    def animate(self):

        animations = [self.game.terrain_spritesheet.get_sprite(865, 160, self.width, self.height),
                      self.game.terrain_spritesheet.get_sprite(895, 160, self.width, self.height),
                      self.game.terrain_spritesheet.get_sprite(925, 160, self.width, self.height)]

        self.image = animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.01
        if self.animation_loop >= 3:
            self.animation_loop = 0

class Explosion(pg.sprite.Sprite):
    def __init__(self, game, x, y, player):
        self.game = game
        self._layer = PLAYER_LAYER
        self.player = player
        self.cronometro = Cronometro()
        self.groups = self.game.all_sprites, self.game.explosion
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE 
        self.height = TILESIZE 

        self.animation_loop = 0
        self.image = self.game.explosion_spritesheet.get_sprite(65,5, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if self.cronometro.tempo_passado() > 2:
            self.animate()

    def animate(self):
        animations = [self.game.explosion_spritesheet.get_sprite(19,8, self.width, self.height),
                      self.game.explosion_spritesheet.get_sprite(19,41, self.width, self.height),
                      self.game.explosion_spritesheet.get_sprite(19,82, self.width, self.height),
                      self.game.explosion_spritesheet.get_sprite(19,126, self.width, self.height),
                      self.game.explosion_spritesheet.get_sprite(19,172, self.width, self.height),
                      self.game.explosion_spritesheet.get_sprite(19,218, self.width, self.height)]

        
        self.image = animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.2
        if self.animation_loop >= 6:
            self.kill()

class Arrow(pg.sprite.Sprite):
    def __init__(self, game, x, y, player, direction):
        self.direction = direction

        self.game = game
        self._layer = PLAYER_LAYER
        self.player = player
        self.groups = self.game.all_sprites, self.game.arrow
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE 
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.speed = 7

        self.animation_loop = 0

        self.image = self.game.andaluz_spritesheet.get_sprite(20, 130, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.animate()
        self.collide_enemies()
        self.collide_obstacles()
        self.collide_blocks()
        self.animate()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change *= 0.8
        self.y_change *= 0.8
        self.speed *= 0.8
    
    def collide_enemies(self):
        hits = pg.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            self.x_change = 0
            self.y_change = 0
            self.speed = 0
    
    def collide_obstacles(self):
        hits = pg.sprite.spritecollide(self, self.game.obstacle, True)
        if hits:
            self.x_change = 0
            self.y_change = 0
            self.speed = 0
                    
    def collide_blocks(self):
        hits = pg.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            self.x_change = 0
            self.y_change = 0
            self.speed = 0
                    
    def animate(self):
        direction = self.game.player.facing
        direction2 = self.game.player2.facing

        right_animations = [self.game.andaluz_spritesheet.get_sprite(20, 130, self.width, self.height)]

        down_animations = [self.game.andaluz_spritesheet.get_sprite(82, 138, self.width, self.height)]

        left_animations = [self.game.andaluz_spritesheet.get_sprite(20, 156, self.width, self.height)]

        up_animations = [self.game.andaluz_spritesheet.get_sprite(63, 138, self.width, self.height)]
        
        if self.player == self.game.player:
            if self.direction == 'up':
                self.y_change -= self.speed
                self.image = up_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()
            
            if self.direction == 'down':
                self.y_change += self.speed
                self.image = down_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()

            if self.direction == 'left':
                self.x_change -= self.speed
                self.image = left_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()

            if self.direction == 'right':
                self.x_change += self.speed
                self.image = right_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()
        
        if self.player == self.game.player2:
            if direction2 == 'up':
                self.y_change -= self.speed
                self.image = up_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()
            
            if direction2 == 'down':
                self.y_change += self.speed
                self.image = down_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()

            if direction2 == 'left':
                self.x_change -= self.speed
                self.image = left_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()

            if direction2 == 'right':
                self.x_change += self.speed
                self.image = right_animations[0]
                self.animation_loop += 1
                if self.animation_loop >= 45:
                    self.kill()

    def movement(self):
        if self.direction == 'up':
            pass

class Auto_heal(pg.sprite.Sprite):
    def __init__(self, game, x, y, player, direction):
        self.direction = direction

        self.game = game
        self._layer = PLAYER_LAYER
        self.player = player
        self.groups = self.game.all_sprites, self.game.Auto_heal
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE 
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.speed = 0

        self.animation_loop = 0

        self.image = self.game.visigodo_spritesheet.get_sprite(280, 90, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide_enemies()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
    
    def collide_enemies(self):
        hits = pg.sprite.spritecollide(self, self.game.enemies, True)
    
    def animate(self):

        right_animations = [self.game.visigodo_spritesheet.get_sprite(223,8, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(263,8, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(303,8, self.width, self.height)]

        down_animations = [self.game.visigodo_spritesheet.get_sprite(222,47, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(258,47, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(296,47, self.width, self.height)]

        left_animations = [self.game.visigodo_spritesheet.get_sprite(222,82, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(257,82, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(295,82, self.width, self.height)]

        up_animations = [self.game.visigodo_spritesheet.get_sprite(222,124, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(258,124, self.width, self.height),
                      self.game.visigodo_spritesheet.get_sprite(295,124, self.width, self.height)]
        
        
        if self.player == self.game.player:
            if self.direction == 'up':
                self.y_change = 0
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()
        
            if self.direction == 'down':
                self.y_change = 0
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()

            if self.direction == 'left':
                self.x_change = 0
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()

            if self.direction == 'right':
                self.x_change = 0
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()
        
        if self.player == self.game.player2:
            if self.direction == 'up':
                self.y_change = 0
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()
        
            if self.direction == 'down':
                self.y_change = 0
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()

            if self.direction == 'left':
                self.x_change = 0
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()

            if self.direction == 'right':
                self.x_change = 0
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.kill()

class Placar(pg.sprite.Sprite):
    def __init__(self, game, x, y, player, max_health):
        self.game = game
        self.player = player
        self.max_health = max_health
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 100
        self.height = TILESIZE

        self.animation_loop = 0
        self.image = self.game.character_spritesheet.get_sprite(111, 2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.animate()
    
    def animate(self):
        health = self.game.player.current_health
        
        animations = [self.game.character_spritesheet.get_sprite(111, 2, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(111, 34, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(111, 66, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(111, 98, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(111, 130, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(111, 162, self.width, self.height)]
        
        
        
        if self.player == self.game.player:
            if health == self.max_health:
                self.image = animations[0]
            if health <= 0.83 * self.max_health:
                self.image = animations[1]
            if health <= 0.66 * self.max_health:
                self.image = animations[2]
            if health <= 0.5 * self.max_health:
                self.image = animations[3]
            if health <= 0.33 * self.max_health:
                self.image = animations[4]
            if health <= 0.17 * self.max_health:
                self.image = animations[5]
       

class Placar2(Placar):
    def __init__(self, game, x, y, player,max_health):
        super().__init__(game, x, y, player,max_health)

        self.image = self.game.character_2_spritesheet.get_sprite(111, 2, self.width, self.height)

    def animate(self):
        health = self.game.player2.current_health
        
        animations = [self.game.character_2_spritesheet.get_sprite(111, 2, self.width, self.height),
                        self.game.character_2_spritesheet.get_sprite(111, 33, self.width, self.height),
                        self.game.character_2_spritesheet.get_sprite(111, 66, self.width, self.height),
                        self.game.character_2_spritesheet.get_sprite(111, 99, self.width, self.height),
                        self.game.character_2_spritesheet.get_sprite(111, 133, self.width, self.height),
                        self.game.character_2_spritesheet.get_sprite(111, 165, self.width, self.height)]

        if self.player == self.game.player2:
            if health == self.max_health:
                self.image = animations[0]
            if health <= 0.83 * self.max_health:
                self.image = animations[1]
            if health <= 0.66 * self.max_health:
                self.image = animations[2]
            if health <= 0.5 * self.max_health:
                self.image = animations[3]
            if health <= 0.33 * self.max_health:
                self.image = animations[4]
            if health <= 0.17 * self.max_health:
                self.image = animations[5]

    def update(self):
        self.animate()