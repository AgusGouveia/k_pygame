from arkanoid import ANCHO, ALTO, FPS
import pygame as pg
from arkanoid.escenes import Portada, Game

pg.init()

class Arkanoid():
    def __init__(self):
            pantalla = pg.display.set_mode((ANCHO, ALTO))
            self.escenas = [Portada(pantalla), Game(pantalla)] #Metemos las escenas en una lista para que salte de una a otra y les inyectamos la pantalla
            self.escena_activa = 0
    
    def start(self):
        while True:
            la_escena = self.escenas[self.escena_activa]
            la_escena.reset()
            la_escena.bucle_principal() #Pertenece a portada y game

            self.escena_activa += 1
            if self.escena_activa >= len(self.escenas):
                self.escena_activa = 0
    