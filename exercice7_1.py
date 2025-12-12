import turtle

# Création de la tortue
t = turtle.Turtle()
t.speed(3)

# Fonction pour dessiner un triangle équilatéral d'une couleur donnée
def triangle(couleur):
    t.color(couleur)
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

# Dessin de plusieurs triangles à différents endroits et couleurs
t.penup()
t.goto(-200, 0)
t.pendown()
triangle('red')

t.penup()
t.goto(0, 0)
t.pendown()
triangle('blue')

t.penup()
t.goto(200, 0)
t.pendown()
triangle('green')

t.penup()
t.goto(-100, -150)
t.pendown()
triangle('yellow')

turtle.done()