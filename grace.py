"""
Beispiel für ein blumiges Mandala mit Farbverlauf
-----
Grace Hopper entwickelte den ersten Compiler, der menschenlesbare Programmiersprachen in
maschinenlesbare Befehle übersetzen kann. Außerdem prägte sie das Sprichwort des
Bugs (Insekt) im Code.
"""

import colorsys
import turtle
from schildkroete import *

# Fenster erstellen
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Schildkröte rufen
grace = Schildkroete()
grace.dicke(4)
grace.geschwindigkeit("fastest")
farbton = 0.0

def LinksDrehen(grad):
    grace.links(grad)
    
def zeichene_Blume(grace, runde, farbton):
    farbe = colorsys.hsv_to_rgb(farbton, 1, 1)
    grace.farbe(farbe)
    grace.kreis(190 - runde, 100)
    grace.links(90)
    grace.kreis(190 - runde, 100)
    grace.rechts(61)


for runde in range(182):

    # grace.pencolor(farbe)
    #Fuer jede Bluete wird eine neue farbe gewaehlt
    farbton += 0.005
    #an die methode ubergeben wir:
    #unsere turtle per namen grace
    #durch laufvariable runde verkleinert sich die blume jeden durchlauf
    #weil runde jeden durchlauf groesser wird bis 185 erreicht ist
    #wir zeichen die Blume mit neuem Farbton
    zeichene_Blume(grace, runde, farbton)
    #grace.circle(190 - runde, 100)
    #grace.left(90)
    #grace.circle(190 - runde, 100)
    #grace.right(61)
    #time.sleep(0.5)

grace.unsichtbar()
screen.mainloop()
