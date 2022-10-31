#sugestao de mudanca de codigo
#pensei inicialmente como arquivo separado, mas acho que faz mais sentido deixar em jogo

import pygame as pg
from PERSONAGEM import Personagem

pressed = pg.key.get_pressed()

personagem = Personagem

#q, e, r comentados pois ainda nao temos um arquivo de habilidades para importar pro nosso personagem e ativar aqui
#diagonais comentadas pois nao sei se estao bem definidas

dic = {
    pg.K_w : personagem.mover_cima(),
    pg.K_a : personagem.mover_esquerda(),
    pg.K_s : personagem.mover_baixo(),
    pg.K_d : personagem.mover_direita(),
    #pg.K_q : personagem.habilidade_q(),
    #pg.K_e : personagem.habilidade_e(),
    #pg.K_r : personagem.habilidade_r(),
    #pg.K_w and pg.K_d : personagem.mover_diagonal_sup_dir(),
    #pg.K_w and pg.K_a : personagem.mover_diagonal_sup_esq(),
    #pg.K_s and pg.K_d : personagem.mover_diagonal_inf_dir(),
    #pg.K_s and pg.K_a : personagem.mover_diagonal_inf_esq()

}

for k, fn in dic.items():
    if(pressed[k]) or (pg.event.type == pg.KEYDOWN and pg.event.key == k):
        fn()

