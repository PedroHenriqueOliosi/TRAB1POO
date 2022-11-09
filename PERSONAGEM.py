import pygame as pg
import sys  
from CONFIG_PERSONAGEM import ConfigPersonagem

class Personagem(pg.sprite.Sprite):
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0 
        super().__init__()
        self.image = pg.image.load('C:\POO\TRAB_1\patrick.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (ConfigPersonagem.DEFAULT_LARGURA,ConfigPersonagem.DEFAULT_ALTURA))
        self.rect = self.image.get_rect()
        self.rect.center = posicao
        
    def fechar_jogo(self):
        pg.event.get()
        
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

    def mover_cima(self, velocidade):
        self.velocidade = -velocidade
        self.keys = pg.key.get_pressed()

        if self.keys[pg.K_w]:    
            self.atualiza_posy()
        elif self.keys[pg.K_w] and pg.key.get_pressed()[pg.K_d]:
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
        self.keys = pg.key.get_pressed()
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
        self.keys = pg.key.get_pressed()
        self.velocidade = -velocidade
            
        if self.keys[pg.K_a]:    
            self.atualiza_posx()
        else:
            self.parar()

    def mover_direita(self, velocidade):
        self.keys = pg.key.get_pressed()
        self.velocidade = velocidade
        
        if self.keys[pg.K_d]:
            self.atualiza_posx()
        else:
            self.parar()

    def atualiza_posx(self):
        self.rect.x,y = self.posicao
        novo_x = self.rect.x + self.velocidade

        if (novo_x >= 0) and ((novo_x + ConfigPersonagem.DEFAULT_LARGURA) <= ConfigPersonagem.SCREEN_WIDTH ):
                self.posicao = (novo_x,y)

    def atualiza_posy(self):
        x,self.rect.y = self.posicao
        novo_y = self.rect.y + self.velocidade

        if (novo_y >= 0) and ((novo_y + ConfigPersonagem.DEFAULT_ALTURA) <= ConfigPersonagem.SCREEN_HEIGHT ):
                self.posicao = (x,novo_y)
    
    def parar(self):
        self.velocidade = 0

    def update(self):
        self.fechar_jogo()
        self.mover_cima(10)
        self.mover_baixo(10)
        self.mover_esquerda(10)
        self.mover_direita(10)

    def barra_de_vida(self):
        pass

    def tiro(self):
        pass
