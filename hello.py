import pygame as pg
import sys

def fin_juego():
    pg.quit()
    sys.exit()

pg.init()
pantalla = pg.display.set_mode((600, 400)) #Creacion de la pantalla
pg.display.set_caption("Hola")

game_over = False
while not game_over:
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True #Colocar la salida del bucle colocando el True o tambien seria posible colocnado el fin_juego


    #Gestion del estado
    print('Hola mundo')

    #Refrescar la pantalla
    pantalla.fill((0, 255, 0)) #Color de pantalla
    pg.display.flip() #Literalmente refrescar la pantalla. Indispensable.


fin_juego()