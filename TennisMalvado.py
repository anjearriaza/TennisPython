import turtle
import random
from jugador import Jugador

# Ventana

ventana = turtle.Screen()
ventana.title("Juego Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Jugadores
jugadorA = Jugador("Antonio", Jugador.Posicion.IZQUIERDA)
jugadorB = Jugador("Jona", Jugador.Posicion.DERECHA)

# Linea de division
division = turtle.Turtle()
division.color("white")
division.goto(0, 300)
division.goto(0, -300)

# Pelota
pelota = turtle.Turtle()
velocidad = 0
pelota.speed(velocidad)
pelota.shape("circle")
pelota.color("white")
pelota.shapesize(0.5)
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 3
pelota.dy = 3

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("{0.nombre}: {0.puntuacion}			{1.nombre}: {1.puntuacion}".format(jugadorA, jugadorB),
               align="center", font=("Courier", 24, "normal"))

# Incrementador de velocidad
contador = 0

# Funciones


def signo():
    x = random.randint(-1, 1)
    while (x == 0):
        x = random.randint(-1, 1)

    return(x/abs(x))


def posicionLibre(x):
    if(x > 0):
        y_top = jugadorB.ycor()+50
        y_bottom = jugadorB.ycor()-50
        if(300-y_top <= y_bottom+300):
            regalo.y = random.randint(-250, y_bottom)
        else:
            regalo.y = random.randint(y_top, 250)
    else:
        y_top = jugadorA.ycor()+50
        y_bottom = jugadorA.ycor()-50
        if(300-y_top <= y_bottom+300):
            regalo.y = random.randint(-250, y_bottom)
        else:
            regalo.y = random.randint(y_top, 250)
    return(regalo.y)


# Regalo
regalo = turtle.Turtle()
regalo.speed(0)
regalo.shape("turtle")
regalo.color("black")
regalo.penup()
regalo.x = signo()*250
regalo.y = random.randint(-250, 250)
regalo.goto(regalo.x, regalo.y)

# Tempo
tempo = 0
tempo_random = random.randint(1, 10)

# Teclado
ventana.listen()
ventana.onkeypress(jugadorA.up, "d")
ventana.onkeypress(jugadorA.down, "c")
ventana.onkeypress(jugadorB.up, "Up")
ventana.onkeypress(jugadorB.down, "Down")

while True:
    ventana.update()

    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)

    # Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        jugadorA.punto()
        marcador.clear()
        marcador.write("{0.nombre}: {0.puntuacion}			{1.nombre}: {1.puntuacion}".format(jugadorA, jugadorB),
                       align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        jugadorB.punto()
        marcador.clear()
        marcador.write("{0.nombre}: {0.puntuacion}			{1.nombre}: {1.puntuacion}".format(jugadorA, jugadorB),
                       align="center", font=("Courier", 24, "normal"))

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
        and (pelota.ycor() < jugadorB.ycor()+50
             and pelota.ycor() > jugadorB.ycor()-50)):
        if (contador > 20):
            pelota.dx *= -1
            tempo += 1
            pelota.color("blue")
        else:
            pelota.dx *= -1.25
            tempo += 1
            pelota.color("blue")
            contador += 1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
        and (pelota.ycor() < jugadorA.ycor()+50
             and pelota.ycor() > jugadorA.ycor()-50)):
        if (contador > 20):
            pelota.dx *= -1
            tempo += 1
            pelota.color("red")
        else:
            pelota.dx *= -1.25
            tempo += 1
            pelota.color("red")
            contador += 1
    if (tempo+tempo_random > 12):
        regalo.x = signo()*350
        regalo.y = posicionLibre(regalo.x)
        regalo.goto(regalo.x, regalo.y)
        regalo.color("green")
        
        if (regalo.x > 0):
            
            epsilon = 0
            regalo_top = regalo.ycor()+epsilon
            regalo_bottom = regalo.ycor()-epsilon
            jugadorB_top = jugadorB.ycor()+50
            jugadorB_bottom = jugadorB.ycor()-50
            print(regalo_top)
            print(regalo_bottom)
            print(jugadorB_top)
            print(jugadorB_bottom)

            if ((regalo_top > jugadorB_bottom and regalo_top < jugadorB_top) or (regalo_bottom > jugadorB_bottom and regalo_bottom < jugadorB_top)):
                print("toco")
                regalo.color("black")
                regalo.x = signo()*25
                regalo.y = random.randint(-250, 250)
                regalo.goto(regalo.x, regalo.y)
                tempo = -10
        else:
            print(regalo.x)
            epsilon = 0
            regalo_top = regalo.ycor()+epsilon
            regalo_bottom = regalo.ycor()-epsilon
            jugadorA_top = jugadorA.ycor()+50
            jugadorA_bottom = jugadorA.ycor()-50
            print(regalo_top)
            print(regalo_bottom)
            print(jugadorA_top)
            print(jugadorA_bottom)


            if ((regalo_top > jugadorA_bottom and regalo_top < jugadorA_top) or (regalo_bottom > jugadorA_bottom and regalo_bottom < jugadorA_top)):
                print("toco")
                regalo.color("black")
                regalo.x = signo()*25
                regalo.y = random.randint(-250, 250)
                regalo.goto(regalo.x, regalo.y)
                tempo = -10

    if (tempo > -9):
        regalo.color("black")
        regalo.x = signo()*25
        regalo.y = random.randint(-250, 250)
        regalo.goto(regalo.x, regalo.y)
