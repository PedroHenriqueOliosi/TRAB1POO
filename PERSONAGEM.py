import pygame as pg
import sys  
from CONFIG_PERSONAGEM import ConfigPersonagem

class Personagem(pg.sprite.Sprite):
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0 
        self.keys = pg.key.get_pressed()
        super().__init__()
        self.image = pg.image.load('C:\POO\TRAB_1\patrick.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,300))
        
    def fechar_jogo(self):
        if self.keys[pg.K_ESCAPE]:
            sys.exit(0)

    def mover_cima(self, velocidade):
        self.velocidade = -velocidade
        if self.keys[pg.K_w]:    
            self.atualiza_posy()
        elif self.keys[pg.K_w] and self.keys[pg.K_d]:
            self.velocidade = velocidade / 2
            self.atualiza_posy()
            self.velocidade = velocidade            
            self.atualiza_posx()
        elif self.keys[pg.K_w] and self.keys[pg.K_a]:
            self.velocidade = velocidade / 2
            self.atualiza_posy()
            self.atualiza_posx()
        else:
            self.parar()

    def mover_baixo(self, velocidade):
        self.velocidade = velocidade
        if self.keys[pg.K_s]:    
            self.atualiza_posy()
        elif self.keys[pg.K_s] and self.keys[pg.K_d]:
            self.velocidade = velocidade / 2
            self.atualiza_posy()
            self.atualiza_posx()
        elif self.keys[pg.K_s] and self.keys[pg.K_a]:
            self.velocidade = velocidade / 2
            self.atualiza_posy()
            self.velocidade = -velocidade
            self.atualiza_posx()
        else:
            self.parar()        

    def mover_esquerda(self, velocidade):
        self.velocidade = -velocidade
        self.atualiza_posx()

    def mover_direita(self, velocidade):
        self.velocidade = velocidade
        self.atualiza_posx()

    def atualiza_posx(self):
        x,y = self.posicao
        novo_x = x + self.velocidade

        if (novo_x >= 0) and ((novo_x + ConfigPersonagem.DEFAULT_LARGURA) <= ConfigPersonagem.SCREEN_WIDTH ):
                self.posicao = (novo_x,y)

    def atualiza_posy(self):
        x,y = self.posicao
        novo_y = y + self.velocidade

        if (novo_y >= 0) and ((novo_y + ConfigPersonagem.DEFAULT_ALTURA) <= ConfigPersonagem.SCREEN_HEIGHT ):
                self.posicao = (x,novo_y)
    
    def parar(self):
        self.velocidade = 0

    def update(self):
        self.mover_cima(10)
        self.mover_baixo(10)
        self.mover_esquerda(10)
        self.mover_direita(10)

    def barra_de_vida(self):
        pass

    def tiro(self):
        pass
