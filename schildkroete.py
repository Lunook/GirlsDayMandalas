import turtle

class Schildkroete:
    def __init__(self):
        self.obj = turtle.Turtle()


    def dicke(self, dicke):
      self.obj.pensize(dicke)

    def farbe(self, farbe):
      self.obj.pencolor(farbe)

    def geschwindigkeit(self, geschwindigkeit):
      #if geschwindigkeit == "schnel;":
      #  print("You are too old to party, granny.")
      #elif age < 0:
      #  print("You're yet to be born")
      #elif age >= 18:
      #  print("You are allowed to party")
      #else: 
      #  "You're too young to party"

      self.obj.speed(geschwindigkeit)

    def vor(self, strecke):
      self.obj.forward(strecke)

    def hinten(self, strecke):
      self.obj.backward(strecke)

    def links(self, grad):
      self.obj.left(grad)

    def rechts(self, grad):
      self.obj.right(grad)

    def kreis(self, radius):
      self.obj.circle(radius)

    def kreis(self, radius, grad):
      self.obj.circle(radius, grad)

    def unsichtbar(self):
      self.obj.hideturtle()