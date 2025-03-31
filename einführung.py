"""
Hier steht eine Beschreibung des Programms
"""
# import colorsys
import turtle
#https://docs.python.org/3/library/turtle.html

# # *** 3 ***
# # Funktionen kann man immer wieder verwenden
# def zeichne_viereck(größe):
#     for farbe in ["yellow", "orange", "red", "purple"]:
#         kame.pencolor(farbe)
#         kame.forward(größe)
#         kame.left(90)

# *** 0 ***
# Fenster erstellen
screen = turtle.Screen()
screen.setup(1.0, 1.0)
# screen.bgcolor("black") # https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/colors.png

# *** 0 ***
# Schildkröte einstellen
kame = turtle.Turtle()
# kame.shape("turtle") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
# kame.color("dark green") # Google: Farbwähler -> "#ad03fc"
# kame.speed(1) # langsam 1..10 schnell; 0 ohne Animation
# kame.pensize(4)

# # *** 1 ***
# # Dies ist eine Kommentarzeile
# # Färben, bewegen und drehen
# kame.pencolor("pink")
# kame.forward(50)
# kame.left(90)
# kame.forward(50)
# kame.left(90)
# # Bewegen ohne zu malen
# kame.up()
# kame.forward(50)
# kame.down()
# kame.pencolor("light blue")
# kame.left(90)
# kame.forward(50)

# # *** 2 ***
# # Zeichnen eines bunten Vierecks
# for farbe in ["yellow", "orange", "red", "purple"]:
#     kame.pencolor(farbe)
#     kame.forward(100)
#     kame.left(90)

# # *** 3 ***
# # Verwenden einer Funktion
# zeichne_viereck(100)
# zeichne_viereck(50)

# # *** 4 ***
# # Zeichnen eines Kreises
# kame.pencolor("light blue")
# kame.circle(100)

# # *** 5 ***
# # Verwenden eines Farbverlaufs
# farbton = 0
# sättigung = 1
# helligkeit = 1
# for runde in range(100):
#     farbe = colorsys.hsv_to_rgb(farbton, sättigung, helligkeit)
#     kame.pencolor(farbe)
#     farbton += 0.01
#     # sättigung += 0.01
#     # helligkeit += 0.01
#     kame.circle(runde * 2)

# kame.hideturtle()
screen.mainloop()
