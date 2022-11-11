import pygame as pg
import sys
from CONFIG_JOGO import ConfigJogo

class Lore:
    def __init__(self, tela):
        pg.init()
        self.tela = tela       
        self.fim = False
        self.width = self.tela.get_width()
        self.height = self.tela.get_height()
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
                #botao de sair
                if ev.type == pg.MOUSEBUTTONDOWN:
                    if self.width*0.5 <= self.mouse[0] <= self.width*0.5+140 and self.height-0.15*self.height <= self.mouse[1] <= self.height-0.15*self.height+40:
                        pg.quit()
                    if self.width*0.3 <= self.mouse[0] <= self.width*0.3+140 and self.height-0.15*self.height <= self.mouse[1] <= self.height-0.15*self.height+40:
                        self.fim = True
                        ConfigJogo.Tela = 1
    def atualiza_estado(self):
        pass

    def desenha(self):
        #textos
        text_titulo = ConfigJogo.bigfont.render("Joguissimo", True, (128, 0, 0))
        text_sair = ConfigJogo.smallfont.render('Sair' , True , ConfigJogo.color)
        text_voltar = ConfigJogo.smallfont.render('Voltar' , True , ConfigJogo.color)
        text_lore_1 = ConfigJogo.smallfont.render("Após beber Ousadia™ na calourada,", True, (120, 120, 120))
        text_lore_2 = ConfigJogo.smallfont.render("Tesla desmaia e tem um sonho.", True, (120, 120, 120))
        text_lore_3 = ConfigJogo.smallfont.render("Em seu sonho os componentes do circuito com que trabalhava", True, (120, 120, 120))
        text_lore_4 = ConfigJogo.smallfont.render("ganham vida e lutam entre si. Começa então", True, (120, 120, 120))
        text_lore_5 = ConfigJogo.smallfont.render("a guerra da eletrônica, onde você é o herói", True, (120, 120, 120))

        #titulo
        self.tela.blit(text_titulo, (self.width/2-text_titulo.get_width()/2,self.height-0.98*self.height))
        #texto lore
        self.tela.blit(text_lore_1, (self.width/2-text_lore_1.get_width()/2,self.height-0.7*self.height))
        self.tela.blit(text_lore_2, (self.width/2-text_lore_2.get_width()/2,self.height-0.6*self.height))
        self.tela.blit(text_lore_3, (self.width/2-text_lore_3.get_width()/2,self.height-0.5*self.height))
        self.tela.blit(text_lore_4, (self.width/2-text_lore_4.get_width()/2,self.height-0.4*self.height))
        self.tela.blit(text_lore_5, (self.width/2-text_lore_5.get_width()/2,self.height-0.3*self.height))

        #botao de sair
        if self.width*0.5 <= self.mouse[0] <= self.width*0.5+140 and self.height-0.15*self.height <= self.mouse[1] <= self.height-0.15*self.height+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[self.width*0.5,self.height-0.15*self.height,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[self.width*0.5,self.height-0.15*self.height,140,40])
        self.tela.blit(text_sair , (self.width*0.5+0.8*text_sair.get_width(),self.height-0.15*self.height))
        
        #botao de voltar
        if self.width*0.3 <= self.mouse[0] <= self.width*0.3+140 and self.height-0.15*self.height <= self.mouse[1] <= self.height-0.15*self.height+40:
            pg.draw.rect(self.tela,ConfigJogo.color_light,[self.width*0.3,self.height-0.15*self.height,140,40])
        else: 
            pg.draw.rect(self.tela,ConfigJogo.color_dark,[self.width*0.3,self.height-0.15*self.height,140,40])
        self.tela.blit(text_voltar , (self.width*0.3+text_voltar.get_width()/3,self.height-0.15*self.height))
        
        pg.display.flip()