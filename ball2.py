import pygame as pg
import sys
from random import randint


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO)) #Creacion de la pantalla
reloj = pg.time.Clock() # Controlador de FPS

class Bola():
    def __init__(self, x, y, vx, vy, xv, xy, color,radio):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.xv = xv
        self.xy = xy
        self.color = color
        self.radio = radio

    def rebotaX(x):
        if x <=0 or x >=ANCHO:
            return -1

        return 1

    def rebotaY(y):
        if y <=0 or y >=ALTO:
            return -1

        return 1

bolas = []
for _ in range(20): #Crear 10 bolas con valores randoms (randint)
    bola = Bola(randint(0, ANCHO),
                randint(0, ALTO),
                randint(5, 10),
                randint(5, 10),
                randint(-10, -5),
                randint(-10, -5),
                (randint(0, 255), randint(0,255), randint(0,255)),
                randint(10, 15))

    bolas.append(bola)

game_over = False
while not game_over:
    v = reloj.tick(10)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # Modificación de estado
    for bola in bolas:
        bola.x += bola.vx
        bola.y += bola.vy
        bola.x += bola.xv
        bola.y += bola.xy

        bola.vy *= Bola.rebotaY(bola.y)
        bola.vx *= Bola.rebotaX(bola.x)
        bola.xv *= Bola.rebotaX(bola.x)
        bola.xy *= Bola.rebotaY(bola.y)


    # Gestión de la pantalla
    pantalla.fill(NEGRO) #Recolocar pantalla
    for bola in bolas:
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), bola.radio) #Creacion de la bola


    pg.display.flip() #Refrescar pantalla

pg.quit()
sys.exit()

#Este creo que funciona sin problema, solo que a veces la bola se queda quieta en el lugar, no entiendo el motivo.