from arkanoid import ANCHO, ALTO, FPS, levels
from arkanoid.entities import Marcador, Bola, Raqueta, Ladrillo
import pygame as pg
import sys

class Escene():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.todoGrupo = pg.sprite.Group()
        self.reloj = pg.time.Clock()

    def reset(self):
        pass

    def bucle_principal(self):
        pass

    def maneja_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or \
                evento.type == pg.KEYDOWN and evento.key == pg.K_q:
                    pg.quit()
                    sys.exit()

    def bucle_principal(self):
        pass
    '''
    while True:
            self.maneja_eventos()
            self.todoGrupo.update(dt)
            self.todoGrupo.draw(self.pantalla)
            pg.display.flip()
            '''

class Game(Escene):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.grupoJugador = pg.sprite.Group()
        self.grupoLadrillos = pg.sprite.Group()

        self.cuentaPuntos = Marcador(10,10, fontsize=50)
        self.cuentaVidas = Marcador(790, 10, "topright", 50, (255, 255, 0))
        self.cuentaVidas.plantilla = "Vidas: {}"
        self.fondo = pg.image.load("./images/background.png")

        self.bola = Bola(ANCHO // 2, ALTO // 2)
        self.todoGrupo.add(self.bola)

        self.raqueta = Raqueta(x = ANCHO//2, y = ALTO - 40)
        self.grupoJugador.add(self.raqueta)

        self.todoGrupo.add(self.grupoJugador)

    def reset(self):
        self.vidas = 3
        self.puntuacion = 0
        self.level = 0
        self.todoGrupo.remove(self.grupoLadrillos)
        self.grupoLadrillos.empty()
        self.disponer_ladrillos(levels[self.level]) #Llamamos a la funcion y le colocamos la lista de levels
        self.todoGrupo.add(self.grupoLadrillos)
        self.todoGrupo.remove(self.cuentaPuntos, self.cuentaVidas)
        self.todoGrupo.add(self.cuentaPuntos, self.cuentaVidas)


    def disponer_ladrillos(self, level):
        for fila, cadena in enumerate(level):
            for columna, caracter in enumerate(cadena):
                if caracter in 'DX':
                    x = 5 + (100 * columna)
                    y = 5 + (40 * fila)
                    ladrillo = Ladrillo(x, y, caracter == 'X')
                    self.grupoLadrillos.add(ladrillo)

    def bucle_principal(self):
        game_over = False
        reloj = pg.time.Clock()
        while not game_over and self.vidas > 0: 
            dt = reloj.tick(FPS)

            self.maneja_eventos()

            self.cuentaPuntos.text = self.puntuacion
            self.cuentaVidas.text = self.vidas 
            self.bola.prueba_colision(self.grupoJugador)
            tocados = self.bola.prueba_colision(self.grupoLadrillos) #Usamos el prueba_colision de la bola para comprobar que ladrillos han sido tocados
            for ladrillo in tocados:
                self.puntuacion += 5 #acumulación de puntos
                if ladrillo.desaparece(): #Si la funcion nos devuelve True...
                    self.grupoLadrillos.remove(ladrillo) #Eliminamos el ladrillo correspondiente 
                    self.todoGrupo.remove(ladrillo) #Quitamos el ladrillo del grupo
                    if len(self.grupoLadrillos) == 0: #Cuando hayan sido eliminados todos los ladrillos, pasamos de nivel
                        self.level += 1
                        self.disponer_ladrillos(levels[self.level])
                        self.todoGrupo.add(self.grupoLadrillos)

            self.todoGrupo.update(dt)
            if self.bola.estado == Bola.Estado.muerta:
                self.vidas -= 1

            self.pantalla.blit(self.fondo, (0,0))
            self.todoGrupo.draw(self.pantalla)

            pg.display.flip()

class Portada(Escene):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.instrucciones = Marcador(ANCHO // 2, ALTO // 2, "center", 50, (255, 255, 0))
        self.instrucciones.text = "Pulsa espacio para jugar"
        self.todoGrupo.add(self.instrucciones)

    def bucle_principal(self):
        game_over = False #seguimos en mismo esquema que en el juego
        while not game_over:
            dt = self.reloj.tick(FPS)

            self.maneja_eventos()

            teclas_pulsadas = pg.key.get_pressed() #Que detecte las teclas pulsadas
            if teclas_pulsadas(pg.K_SPACE): #Si presionas SPACE...
                game_over = True

            self.todoGrupo.update(dt)
            self.pantalla.fill((0, 0, 0))
            self.todoGrupo.draw(self.pantalla)

            pg.display.flip()