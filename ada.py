"""
Beispiel für ein Sternen-Mandala aus Kreisen
-----
Ada Lovelace war die erste Programmiererin, vor allen Männern und bevor Computer
überhaupt erfunden worden waren.
"""
from schildkroete import *

import turtle

#class Schildkroete(turlte.Turtle):
 #   def __init__(self):••••••••••••
        


def ringe_zeichnen_drehen(ada, radius, anzahl_ringe, verkleinerung, drehung):
    for i in range(anzahl_ringe):
        #wir zeichnen unserer kreis mit dem gegebenen radius
        ada.kreis(radius, 360)
        #wir wechseld die farbe fuer jeden kreis
        ada.farbe(farbe[i])
        #wir verkleinern unseren radius um die gegebene verkleinerung
        radius -= verkleinerung

    #wir drehen unseren kreis um die gegebene drehung
    ada.rechts(drehung)


# Fenster erstellen
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Schildkröte rufen
ada = Schildkroete()
ada.dicke(5)
ada.farbe("#ed0ed3")
ada.geschwindigkeit(0)
durchlaufvariable = 0

farbe = ["#0e6251","#117864", "#148f77" , "#1ba38a", "#17a589", 
         "#1abc9c","#48c9b0","#5be0c0", "#7cf3d0", "#9cf6e0", "#76d7c4"]
#wir wollen insgesamt 12 Ringkonstrukte zeichnen, bis das geschehen ist wiederholen wir
while durchlaufvariable < 11:
    """wir setzen unseren initialen radius auf 150"""
    radius = 150
    """#hier erstellen wir wie unsere ring konstrukte aussehen sollen
    #wir ubergeben an die methode:
    #unsere turtle per namen ada
    #radius, variablenname so dass wir den tatsaechlich verklienern koennen
    #anzahl der Rinke im grossen Ring
    #wie viel kliener die inneren kreise jeweils werden 
    #wie viel Grad nach einem konstrukt nach rechts gedreht wird """
    
    ringe_zeichnen_drehen(ada, radius, 10, 5, 36)
    #hiermit koennte jedes rinkonstrunkt eine neue farbe haben:
    #ada.pencolor(farbe[durchlaufvariable])
  
    #wir zahlen 1 hoch so dass unsere schleife ach zu einem Ende kommt
    durchlaufvariable += 1
   

ada.unsichtbar()
screen.mainloop()




