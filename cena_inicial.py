import pygame as pg
import sys
from CONFIG_JOGO import ConfigJogo

class Inicial:
    def __init__(self, tela):
        pg.init()
        self.tela = tela       
        self.fim = False
        self.mouse = pg.mouse.get_pos()
        
        
    def rodar(self):
        while not self.fim:
            self.desenha()
            self.tratamento_eventos()
            #self.atualiza_estado()

    def tratamento_eventos(self):
        while True:
            mouse_anterior = self.mouse
            self.mouse = pg.mouse.get_pos()

            if (self.mouse != mouse_anterior):
                self.desenha()
                print(ConfigJogo.Tela)

            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    sys.exit(0)
                #botao de PvP
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if 0 <= self.mouse[0] <= 900 and 0 <= self.mouse[1] <= 300:
                        pg.quit()
                        sys.exit(0)
                #botao de PvC
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.45*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.45*ConfigJogo.ALTURA_TELA+40:
                        pg.quit()
                        sys.exit(0)
                #botao de lore
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.3*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.3*ConfigJogo.ALTURA_TELA+40:
                        ConfigJogo.Tela = 2
                        print("mudou")
                        print(ConfigJogo.Tela)
                        self.fim = True
                        
                #botao de sair
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA+40:
                        pg.quit()
                        sys.exit(0)
                
    def atualiza_estado(self):
        pass

    def desenha(self):
        #textos
        text_titulo = ConfigJogo.bigfont.render("Joguissimo", True, (0, 128, 0))
        text_sair = ConfigJogo.smallfont.render('Sair' , True , ConfigJogo.color)
        text_lore = ConfigJogo.smallfont.render('Lore' , True , ConfigJogo.color)
        text_pvc = ConfigJogo.smallfont.render('PvC' , True , ConfigJogo.color)
        text_pvp = ConfigJogo.smallfont.render('PvP' , True , ConfigJogo.color)

        #titulo
        self.tela.blit(text_titulo, (ConfigJogo.LARGURA_TELA/2-text_titulo.get_width()/2,ConfigJogo.ALTURA_TELA-0.9*ConfigJogo.ALTURA_TELA))

        #botao de PvP
        if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.6*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.6*ConfigJogo.ALTURA_TELA+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.6*ConfigJogo.ALTURA_TELA,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.6*ConfigJogo.ALTURA_TELA,140,40])
        self.tela.blit(text_pvp , (ConfigJogo.LARGURA_TELA/2-text_pvp.get_width()/1.5,ConfigJogo.ALTURA_TELA-0.59*ConfigJogo.ALTURA_TELA))

        #botao de PvC
        if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.45*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.45*ConfigJogo.ALTURA_TELA+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.45*ConfigJogo.ALTURA_TELA,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.45*ConfigJogo.ALTURA_TELA,140,40])
        self.tela.blit(text_pvc , (ConfigJogo.LARGURA_TELA/2-text_pvc.get_width()/1.5,ConfigJogo.ALTURA_TELA-0.44*ConfigJogo.ALTURA_TELA))

        #botao de lore
        if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.3*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.3*ConfigJogo.ALTURA_TELA+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.3*ConfigJogo.ALTURA_TELA,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.3*ConfigJogo.ALTURA_TELA,140,40])
        self.tela.blit(text_lore , (ConfigJogo.LARGURA_TELA/2-text_lore.get_width()/1.5,ConfigJogo.ALTURA_TELA-0.29*ConfigJogo.ALTURA_TELA))

        #botao de sair
        if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA,140,40])
        self.tela.blit(text_sair , (ConfigJogo.LARGURA_TELA/2-text_sair.get_width()/1.5,ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA))
            
        pg.display.flip()



