import pygame as pg
import math as mt

#codigo pedro
import pygame as pg
from CONFIG_PERSONAGEM import ConfigPersonagem
import math as mt

class Personagem:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0
        self.lista_tipos = [0, 1, 2, 3, 4] #placeholder, mago, tank, lutador, atirador
        self.tipo = self.lista_tipos[0]
        self.color = "White"
        self.posicao = posicao
    
    def escolhe_tipo (self, seletor: int):
        self.tipo = self.lista_tipos[seletor]

        if self.tipo == 1:
            self.color = "Yellow"
        if self.tipo == 2:
            self.color = "Cyan"
        if self.tipo == 3:
            self.color = "Red"
        if self.tipo == 4:
            self.color = "Blue"

    #codigo pedro
    def mover_positivo(self):
        self.velocidade = ConfigPersonagem.VEL_PERSONAGEM
    def mover_negativo(self):
        self.velocidade = -ConfigPersonagem.VEL_PERSONAGEM
    def mover_positivo_diagonal(self):
        self.velocidade = ConfigPersonagem.VEL_PERSONAGEM / mt.sqrt(2)
    def mover_negativo_diagonal(self):
        self.velocidade = -(ConfigPersonagem.VEL_PERSONAGEM / mt.sqrt(2))
        
    
    def parar(self):
        self.velocidade = 0

    def atualizar_posx(self):
        x,y = self.posicao
        novo_x = x + self.velocidade

        if (novo_x >= ConfigPersonagem.RAIO_PERSONAGEM) and ((novo_x + ConfigPersonagem.RAIO_PERSONAGEM) <= ConfigPersonagem.SCREEN_WIDTH ):
                self.posicao = (novo_x,y)
   
    def atualizar_posy(self):
        x,y = self.posicao
        novo_y = y + self.velocidade

        if (novo_y >= ConfigPersonagem.RAIO_PERSONAGEM) and ((novo_y + ConfigPersonagem.RAIO_PERSONAGEM) <= ConfigPersonagem.SCREEN_HEIGHT ):
                self.posicao = (x,novo_y)
    
    def barra_de_vida(self):
        pass

    def tiro(self):
        pass


