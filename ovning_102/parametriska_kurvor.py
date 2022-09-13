import turtle as t
import numpy as np
from operator import add, mul

RANGE_STAND = np.arange(-2, 2, 0.025)
RANGE_TRIG = np.arange(0, 2*np.pi, 0.025)
RANGE_LEAF = np.arange(-10, 7, 0.025)

parabel = lambda t: [t**2, t]
hyperbel = lambda t: [np.cosh(t), np.sinh(t)]
lemniskata = lambda t: [np.cos(t)/(1+np.sin(t)**2), np.cos(t)*np.sin(t)/(1+np.sin(t)**2)]
asteriod = lambda t: [np.cos(t)**3, np.sin(t)**3]
descartes = lambda t: [t/(1+t**3), t**2/(1+t**3)]

counter = 0
def plot_func(func, range, origo, ab):
    function = lambda t: list(map(add, map(mul, func(t), ab), origo))
    global counter; tim.color(["Red", "Pink", "Blue", "Yellow", "Green"][counter%5]); counter += 1
    tim.penup()
    tim.goto(function(range[0]))
    tim.pendown()
    for t in range:
        tim.goto(function(t))

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
plot_func(parabel, RANGE_STAND, origo, (50, 50))
plot_func(hyperbel, RANGE_STAND, origo, (50, 50))
plot_func(lemniskata, RANGE_TRIG, origo, (50, 50))
plot_func(asteriod, RANGE_TRIG, origo, (50, 50))
plot_func(descartes, RANGE_LEAF, origo, (50, 50))


screen.exitonclick()
