import turtle
import time

turtle = turtle.Turtle()
turtle.setup(800,600)
placelist = []
#turtle.speed(10000)

def plade():
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.goto(-150,50)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(300)
        turtle.right(180)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(180)


def kryds(x,y):
    for coordinate in placelist:
        print(coordinate)
        if coordinate == str(x)+str(y):
            print("match")
            return
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(-140 + x*100, -60 + y*100)
    turtle.pendown()
    turtle.goto(turtle.position()[0] + 80, turtle.position()[1] - 80)
    turtle.penup()
    turtle.goto(-140 + x*100, -140 + y*100)
    turtle.pendown()
    turtle.goto(turtle.position()[0] + 80, turtle.position()[1] + 80)
    placelist.append(str(x)+str(y))

def bolle(x,y):
    for coordinate in placelist:
        print(coordinate)
        if coordinate == str(x)+str(y):
            print("match")
            return
    turtle.pencolor('red')
    turtle.penup()
    turtle.goto(-100 + x*100, -140 + y*100)
    turtle.pendown()
    turtle.circle(40)
    placelist.append(str(x)+str(y))

def klik_kryds(x,y):
    print('kryds: ' + str(x) + ', ' + str(y))
    kryds(x,y)

def klik_bolle(x,y):
    print('bolle: ' + str(x) + ', ' + str(y))
    bolle(x,y)

# tegn spillepladen
plade()

print('klar til at spille - tryk i felterne!')

for x in range(0,20):
    krydsbolle = input("Kryds eller bolle? ")
    if krydsbolle == "kryds":
        felterFraVenstre = int(input("Hvor mange felter fra venstre? "))
        felterFraVenstre = felterFraVenstre - 1
        felterFraBunden = int(input("Hvor mange felter fra bunden? "))
        felterFraBunden = felterFraBunden - 1

        # Test if values are in the allowed range
        if felterFraVenstre <= 2 and felterFraBunden <= 2:
            klik_kryds(felterFraVenstre,felterFraBunden)
    elif krydsbolle == "bolle":
        felterFraVenstre = int(input("Hvor mange felter fra venstre? "))
        felterFraVenstre = felterFraVenstre - 1
        felterFraBunden = int(input("Hvor mange felter fra bunden? "))
        felterFraBunden = felterFraBunden - 1

        # Test if values are in the allowed range
        if felterFraVenstre <= 2 and felterFraBunden <= 2:
            klik_bolle(felterFraVenstre,felterFraBunden)
