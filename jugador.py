import turtle
from enum import Enum


class Jugador(turtle.Turtle):
    """La clase jugador contiene la posición de cada jugador,
    su puntuación así como lo relativo a cómo dibujar cada jugador
    """

    class Posicion(Enum):
        IZQUIERDA = 1
        DERECHA = 2

    def __init__(self, nombre, posicion):
        super().__init__()
        self.nombre = nombre
        self.puntuacion = 0

        if posicion == Jugador.Posicion.IZQUIERDA:
            a = -350
        elif posicion == Jugador.Posicion.DERECHA:
            a = 350
        else:
            raise Exception("La posición del jugador debe ser una de las permitidas")

        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(a, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

    def punto(self):
        self.puntuacion += 1
