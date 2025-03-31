"""
Beispiel für ein Spiral-Mandala mit Kanten
-----
Radia Perlman ist eine Netzwerktechnikerin, die viele wichtige Protokolle für die
Kommunikation von Geräten über das Internet entwickelt hat. Dank ihr läuft das Internet
heutzutage größtenteils stabil und reibungslos. Das brachte ihr den Spitznamen
"Mutter des Internets" ein.
"""

import turtle
from schildkroete import *

# Fenster erstellen
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("black")
# Schildkröte rufen
radia = Schildkroete()
radia.dicke(4)
radia.geschwindigkeit("fastest")

farben = ["#7D37F0", "#28D7B9", "#0F234B", "#FFE606"]
for runde in range(280):
    radia.farbe(farben[runde%4])
    radia.vor(runde)
    radia.links(59)
    
radia.unsichtbar()

screen.mainloop()
