import pygame as pg
import sys
from CONFIG_JOGO import ConfigJogo
from personagem import Personagem

class SelecaoPVP:
    def __init__(self, tela):
        pg.init()
        self.tela = tela       
        self.fim = False
        self.mouse = pg.mouse.get_pos()
        self.escolha_1 = 0
        self.escolha_2 = 0
        
        
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

            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                #botao de sair
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if 370 <= self.mouse[0] <= 510 and 380 <= self.mouse[1] <= 425:
                        pg.quit()

                #botoes de escolha pro jog 1
                #p1
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.2 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.2 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.5 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.5 + 40:
                        ConfigJogo.tipo_jog_1 = 1
                        #Personagem.escolhe_tipo(jog_1, 1)
                        self.escolha_1 = 1
                        print("jog 1: 1")
                #p2
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.255 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.255 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.5 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.5 + 40:
                        ConfigJogo.tipo_jog_1 = 2
                        #Personagem.escolhe_tipo(jog1, 2)
                        self.escolha_1 = 1
                        print("jog 1: 2")
                #p3
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.2 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.2 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.61 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.61 + 40:
                        ConfigJogo.tipo_jog_1 = 3
                        #Personagem.escolhe_tipo(jog1, 3)
                        self.escolha_1 = 1
                        print("jog 1: 3")
                #p4
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.25 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.25 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.61 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.61 + 40:
                        ConfigJogo.tipo_jog_1 = 4
                        #Personagem.escolhe_tipo(jog1, 4)
                        self.escolha_1 = 1
                        print("jog 1: 4")

                #botoes de escolha pro jog 1
                #p1
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.7 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.7 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.5 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.5 + 40:
                        ConfigJogo.tipo_jog_2 = 1
                        #Personagem.escolhe_tipo(jog_2, 1)
                        self.escolha_2 = 1
                        print("jog 2: 1")
                #p2
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.755 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.755 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.5 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.5 + 40:
                        ConfigJogo.tipo_jog_2 = 2
                        #Personagem.escolhe_tipo(jog2, 2)
                        self.escolha_2 = 1
                        print("jog 2: 2")
                #p3
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.7 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.7 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.61 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.61 + 40:
                        ConfigJogo.tipo_jog_2 = 3
                        #Personagem.escolhe_tipo(jog2, 3)
                        self.escolha_2 = 1
                        print("jog 2: 3")
                #p4
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if ConfigJogo.LARGURA_TELA*0.75 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA*0.75 + 40 and \
                        ConfigJogo.ALTURA_TELA*0.61 <= self.mouse[1] <= ConfigJogo.ALTURA_TELA*0.61 + 40:
                        ConfigJogo.tipo_jog_2 = 4
                        #Personagem.escolhe_tipo(jog2, 4)
                        self.escolha_2 = 1
                        print("jog 2: 3")

                if(self.escolha_1 + self.escolha_2 == 2):
                    ConfigJogo.Tela = 4
                    self.fim = True

                
    def atualiza_estado(self):
        pass

    def vai_pra_tela_batalha (self):
        pass

    def desenha(self):
        #textos
        text_titulo = ConfigJogo.bigfont.render("Joguissimo", True, (128, 0, 0))
        text_sair = ConfigJogo.smallfont.render('Sair:' , True , ConfigJogo.color)
        text_player1 = ConfigJogo.smallfont.render('Player 1:' , True , ConfigJogo.color)
        text_player2 = ConfigJogo.smallfont.render("Player 2:", True, (120, 120, 120))
        
        #titulo
        self.tela.blit(text_titulo, (ConfigJogo.LARGURA_TELA/2-text_titulo.get_width()/2,ConfigJogo.ALTURA_TELA-0.9*ConfigJogo.ALTURA_TELA))
        
        #texto player
        self.tela.blit(text_player1, (ConfigJogo.LARGURA_TELA*0.2, ConfigJogo.ALTURA_TELA*0.35))
        self.tela.blit(text_player2, (ConfigJogo.LARGURA_TELA*0.6, ConfigJogo.ALTURA_TELA*0.35))
        
        #botao de sair
        if ConfigJogo.LARGURA_TELA/2-80 <= self.mouse[0] <= ConfigJogo.LARGURA_TELA/2+70 and ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA <= self.mouse[1] <= ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[ConfigJogo.LARGURA_TELA/2-80,ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA,140,40])
        self.tela.blit(text_sair , (ConfigJogo.LARGURA_TELA/2-text_sair.get_width()/1.5,ConfigJogo.ALTURA_TELA-0.15*ConfigJogo.ALTURA_TELA))
        
        #botoes player 1
        #jog 1
        pg.draw.rect(self.tela,"Yellow",[ConfigJogo.LARGURA_TELA*0.2,ConfigJogo.ALTURA_TELA*0.5, 40, 40])
        #jog 2
        pg.draw.rect(self.tela,"Cyan",[ConfigJogo.LARGURA_TELA*0.255,ConfigJogo.ALTURA_TELA*0.5, 40, 40])
        #jog 3
        pg.draw.rect(self.tela,"Red",[ConfigJogo.LARGURA_TELA*0.2,ConfigJogo.ALTURA_TELA*0.61, 40, 40])
        #jog 4
        pg.draw.rect(self.tela,"Blue",[ConfigJogo.LARGURA_TELA*0.255,ConfigJogo.ALTURA_TELA*0.61, 40, 40])


        #botoes player 2
        #jog 1
        pg.draw.rect(self.tela,"Yellow",[ConfigJogo.LARGURA_TELA*0.7,ConfigJogo.ALTURA_TELA*0.5, 40, 40])
        #jog 2
        pg.draw.rect(self.tela,"Cyan",[ConfigJogo.LARGURA_TELA*0.755,ConfigJogo.ALTURA_TELA*0.5, 40, 40])
        #jog 3
        pg.draw.rect(self.tela,"Red",[ConfigJogo.LARGURA_TELA*0.7,ConfigJogo.ALTURA_TELA*0.61, 40, 40])
        #jog 4
        pg.draw.rect(self.tela,"Blue",[ConfigJogo.LARGURA_TELA*0.755,ConfigJogo.ALTURA_TELA*0.61, 40, 40])

        pg.display.flip()



