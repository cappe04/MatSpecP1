import turtle as t
import numpy as np
from operator import add
FONTSIZE = 24


def calc_ellipse(t, origo):
    """
    Paramater: Ett tal och en tupel (koordinat)
    Returnerar: En koordinat
    Kommentar: Returkoordinaterna ligger på en ellips
    """
    # a och b styr storlek och form på ellipsen
    a = 100
    b = 50
    x = a*np.cos(t)
    y = b*np.sin(t)

    # Exempel på hur returen fungerar:
    # Om x = 100, y = 200 och origo = (30, -50)
    # så returneras (130, 150)
    return list(map(add, (x, y), origo))


def plot_ellipse(origo):
    """
    Parameter: En tupel (koordinat), som anger centrum för ellipsen
    Returnerar: Inget
    Kommentar: Proceduren ritar ellipsen, koordinater beräknas i
    funktionen calc_ellips
    """
    tim.color("Red")
    tim.penup()
    tim.goto(calc_ellipse(0, origo))  # Gå till första punkten på ellipsen
    tim.pendown()

    # Skapar en lista med tal mellan 0 och 2*pi med avståndet 0.025, dvs
    # 0, 0.025, 0.050, ... ,6.275
    t = np.arange(0, 2*np.pi, 0.025)

    for i in t:  # Ritar ellipsen
        tim.goto(calc_ellipse(i, origo))


def print_text(text, origo):
    """
    Parametrar: En text och en tupel (koordinat) som anger centrum för texten
    Returnerar: Inget
    Kommentar: Procedur som skriver ut texten i ellipsen
    """
    tim.penup()
    tim.color("white")
    tim.goto(origo[0], origo[1] - FONTSIZE/2)
    tim.write(text, font=("Arial", FONTSIZE, "normal"), align="center")


### Huvudprogram ###
tim = t.Turtle()
tim.hideturtle()
tim.pensize(6)
tim.shape("triangle")
tim.shapesize(0.4)
tim.speed(0)  # 0 - 10, 1 - 10 ökad hastighet, 0 snabbast
screen = t.Screen()
screen.bgcolor("Black")
screen.setup(900, 600)
screen.title("Några parametriska kurvor")

origo = (-300, 150)  # Runt vilken punkt plotten ska vara centererad
plot_ellipse(origo)  # Plottar ellipsen
print_text("Ellips", origo)  # Skriver texten i ellipsen

screen.exitonclick()
