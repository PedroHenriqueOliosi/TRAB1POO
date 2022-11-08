import pygame as pg

from CONFIG_PERSONAGEM import ConfigPersonagem
from PERSONAGEM import Personagem

class Jogo:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            (ConfigPersonagem.SCREEN_WIDTH, ConfigPersonagem.SCREEN_HEIGHT))

        self.px = ConfigPersonagem.POSX_PERSONAGEM
        self.py = ConfigPersonagem.POSY_PERSONAGEM
        
        self.player = pg.sprite.GroupSingle()
        self.player.add(Personagem(posicao=(self.px,self.py)))

        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.desenha()

    def desenha(self):
        
        self.screen.fill('white')
        
        self.player_surf = pg.image.load('C:\POO\TRAB_1\patrick.png').convert_alpha()
        self.player_surf = pg.transform.scale(self.player_surf, ConfigPersonagem.TAMANHO)
        self.player_rect = self.player_surf.get_rect(topleft = (self.px,self.py))

        self.screen.blit(self.player_surf,self.player_rect)
        
        pg.display.update()
        self.player.draw(self.screen)
        self.player.update()
        pg.display.flip()
        self.clock.tick(ConfigPersonagem.FPS)
        

def main():
    game = Jogo()
    game.run()

if __name__ == '__main__':
    main()
            
