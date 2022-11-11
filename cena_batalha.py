import sys
import pygame as pg

from CONFIG_PERSONAGEM import ConfigPersonagem
from personagem import Personagem

class Jogo:
    def __init__(self, tela):
        pg.init()
        self.tela = tela

        px = ConfigPersonagem.POSX_PERSONAGEM
        py = ConfigPersonagem.POSY_PERSONAGEM
        
        self.player = Personagem(posicao=(px,py))
        self.clock = pg.time.Clock()

    def rodar (self):
        while not self.fim:
            self.desenha()
            self.tratamento_eventos()
    
    def tratamento_eventos(self):
        pg.event.get()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            sys.exit(0)

        if keys[pg.K_w]:
            self.player.mover_negativo()
            self.player.atualizar_posy()
        elif keys[pg.K_d]:
            self.player.mover_positivo()
            self.player.atualizar_posx()
        elif keys[pg.K_s]:
            self.player.mover_positivo()
            self.player.atualizar_posy()
        elif keys[pg.K_a]:
            self.player.mover_negativo()
            self.player.atualizar_posx() 
        else:
            self.player.parar()

        if keys[pg.K_w] and keys[pg.K_d]:   #x+ y-
            self.player.mover_positivo_diagonal()
            self.player.atualizar_posx()
            self.player.mover_negativo_diagonal()
            self.player.atualizar_posy()
        elif keys[pg.K_w] and keys[pg.K_a]: #x- y-
            self.player.mover_negativo_diagonal()
            self.player.atualizar_posx()
            self.player.atualizar_posy()
        elif keys[pg.K_s] and keys[pg.K_d]: #x+ y+
            self.player.mover_positivo_diagonal()
            self.player.atualizar_posx()
            self.player.atualizar_posy()
        elif keys[pg.K_s] and keys[pg.K_a]: #x- y+
            self.player.mover_negativo_diagonal()
            self.player.atualizar_posx()
            self.player.mover_positivo_diagonal()
            self.player.atualizar_posy()
        else:
            self.player.parar()

    def desenha(self):
        self.tela.fill('white')
        
        x = self.player.posicao[0]
        y = self.player.posicao[1]

        pg.draw.circle(
            self.tela,
            ConfigPersonagem.COR_PERSONAGEM,
            (x, y),
            ConfigPersonagem.RAIO_PERSONAGEM
        )
        
#def main():
#    game = Jogo()
#    game.run()