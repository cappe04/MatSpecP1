import turtle as t


def move_to(start_coord, mark=False):
    """
    Parametrar: En tupel (koordinat) och en boolean
    Den boolska parametern mark anger om ett streck ska ritas
    under förflyttningen
    Returnerar: inget
    """
    if not mark:
        tim.penup()
    tim.goto(start_coord)
    tim.pendown()  # Glöm inte att sätta ned pennan igen där det behövs


### Huvudprogram ###
tim = t.Turtle()  # Sköldpaddan kan döpas till vilket variabelnamn som helst
# tim.hideturtle() # Kan avkommenteras när programmet är klart
tim.pensize(5.0)  # Kan vara vilket tal x som helst, x > 0
tim.shape("turtle")
tim.shapesize(1.0)  # Kan vara vilket tal x som helst, x > 0
tim.speed(2)  # Heltal 0 - 10 (1 - 10 ökande hastighet, 0 är snabbast)
screen = t.Screen()
screen.title("Polygoner")
screen.bgcolor("wheat1")
screen.setup(900, 600)  # Screensize WxH, in pixels

# Namngivna färger finns på https://cs111.wellesley.edu/labs/lab02/colors
tim.color('DarkBlue', 'aquamarine')

# Här ritas själva kvadraten
tim.begin_fill()
start_coord = (-300, 150)
move_to(start_coord)
for i in range(4):
    tim.forward(150)
    tim.right(90)
tim.end_fill()

screen.exitonclick()
