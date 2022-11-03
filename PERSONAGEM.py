import pygame as pg
from CONFIG_PERSONAGEM import ConfigPersonagem

class Personagem:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0 

    def mover_cima(self, velocidade):
        self.velocidade = -velocidade
        self.atualiza_posy()
        
    def mover_esquerda(self, velocidade):
        self.velocidade = -velocidade
        self.atualiza_posx()

    def mover_baixo(self, velocidade):
        self.velocidade = velocidade
        self.atualiza_posy()

    def mover_direita(self, velocidade):
        self.velocidade = velocidade
        self.atualiza_posx()

    def atualiza_posx(self):
        x,y = self.posicao
        novo_x = x + self.velocidade

        if (novo_x >= ConfigPersonagem.RAIO_PERSONAGEM) and ((novo_x + ConfigPersonagem.RAIO_PERSONAGEM) <= ConfigPersonagem.SCREEN_WIDTH ):
                self.posicao = (novo_x,y)

    def atualiza_posy(self):
        x,y = self.posicao
        novo_y = y + self.velocidade

        if (novo_y >= ConfigPersonagem.RAIO_PERSONAGEM) and ((novo_y + ConfigPersonagem.RAIO_PERSONAGEM) <= ConfigPersonagem.SCREEN_HEIGHT ):
                self.posicao = (x,novo_y)
    
    def parar(self, velocidade):
        self.velocidade = velocidade

    def desenho(self, screen):
        x = self.posicao[0]
        y = self.posicao[1]
        pg.draw.circle(
            screen,
            ConfigPersonagem.COR_PERSONAGEM,
            (x, y),
            ConfigPersonagem.RAIO_PERSONAGEM
        )
    
    def barra_de_vida(self):
        pass

    def tiro(self):
        pass
