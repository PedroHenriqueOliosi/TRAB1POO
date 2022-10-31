import sys
import pygame as pg

from CONFIG_PERSONAGEM import ConfigPersonagem
from PERSONAGEM import Personagem

class Jogo:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            (ConfigPersonagem.SCREEN_WIDTH, ConfigPersonagem.SCREEN_HEIGHT))

        px = ConfigPersonagem.POSX_PERSONAGEM
        py = ConfigPersonagem.POSY_PERSONAGEM
        
        self.player = Personagem(posicao=(px,py))
        self.clock = pg.time.Clock()
    def run(self):
        while True:
            self.eventos()
            self.desenha()
    
    def eventos(self):
       pressed = pg.key.get_pressed()

       dic = {
           pg.K_w : self.player.mover_cima(),
           pg.K_a : self.player.mover_esquerda(),
           pg.K_s : self.player.mover_baixo(),
           pg.K_d : self.player.mover_direita()
       }

       for k, fn in dic.items():
           if(pressed[k]) or (pg.event.type == pg.KEYDOWN and pg.event.key == k):
              fn()

    def desenha(self):
        self.screen.fill('white')
        self.player.desenho(self.screen)
        self.player.desenho(self.screen)
        pg.display.flip()
        self.clock.tick(ConfigPersonagem.FPS)
        

def main():
    game = Jogo()
    game.run()

if __name__ == '__main__':
    main()
            
