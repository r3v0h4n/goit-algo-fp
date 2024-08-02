import turtle
import math

def draw(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    
    t.left(45)
    draw(t, length * math.sqrt(2) / 2, level - 1)
    
    t.right(45 + 45)
    draw(t, length * math.sqrt(2) / 2, level - 1)
    
    t.left(45)
    t.backward(length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.speed(0)
    
    t.left(90)
    t.up()
    t.goto(0, -200)
    t.down()
    
    draw(t, 100, level)
    
    screen.mainloop()

if __name__ == "__main__":
    main()