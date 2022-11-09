import pygame as pg
from CONFIG_PERSONAGEM import * 
#futuramente sera a classe de habilidades
class Tiro(pg.sprite.Sprite):
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0
        super().__init__()
        self.image = pg.image.load('C:\POO\TRAB_1\Tiro.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (ConfigPersonagem.TAMANHO_TIRO[0],ConfigPersonagem.TAMANHO_TIRO[1]))
        self.rect = self.image.get_rect()
        self.rect.midleft = posicao

    def atualizar_pos(self):
        self.rect.x,y = self.posicao
        novo_x = self.rect.x + self.velocidade

        if (novo_x >= 0) and ((novo_x + ConfigPersonagem.TAMANHO_TIRO[0]) <= ConfigPersonagem.SCREEN_WIDTH):
            self.posicao = (novo_x,y)

    def mover(self, velocidade):
        self.velocidade = velocidade
    
    def update(self):
        self.mover(50)
        self.atualizar_pos()
