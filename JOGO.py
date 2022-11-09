import pygame as pg

from CONFIG_PERSONAGEM import *
from PERSONAGEM import *
from TIRO import *

class Jogo:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            (ConfigPersonagem.SCREEN_WIDTH, ConfigPersonagem.SCREEN_HEIGHT))

        self.px = ConfigPersonagem.POSX_PERSONAGEM
        self.py = ConfigPersonagem.POSY_PERSONAGEM
        
        self.player = pg.sprite.GroupSingle()
        self.player.add(Personagem(posicao=(self.px,self.py)))

        self.tiro = pg.sprite.Group()

        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.eventos()
            self.desenha()

    def eventos(self):
        self.keys = pg.key.get_pressed()

        if self.keys[pg.K_SPACE]:
            self.tiro.add(Tiro(posicao= (self.px,self.py)))

    def desenha(self):
        
        self.clock.tick(ConfigPersonagem.FPS)
        self.screen.fill('white')
        
        self.player.update()
        self.player.draw(self.screen)

        self.tiro.update()
        self.tiro.draw(self.screen)

        pg.display.update()
        
        

def main():
    game = Jogo()
    game.run()

if __name__ == '__main__':
    main()
            
