"""
Spencer Kirby
11/27/24
better version of old code 
"""
import math
import turtle
from sympy import symbols, Eq, solve

EULER_NUM = math.e
SCREEN_WIDTH_DEFAULT = 600
SCREEN_HEIGHT_DEFAULT = 600
STEP_DEFAULT = 0.1

def main():
    while True:
        operation = int(input("Select operation: 1 - Add, 2 - Sub, 3 - Mul, 4 - Div, "
                              "5 - Quadratics, 6 - Interest, 7 - Exponents, "
                              "8 - Cubic Extrema, 9 - Average: "))
        mode = int(input("Graph options: 0 - Numbers, 1 - Graph, 2 - Both: "))

        step, screen_width, screen_height = (STEP_DEFAULT, SCREEN_WIDTH_DEFAULT, SCREEN_HEIGHT_DEFAULT)
        if mode in [1, 2] and int(input("Custom graphing? 1 - Yes, 2 - No: ")) == 1:
            step = float(input("Graphing step: "))
            screen_width = int(input("Screen width: "))
            screen_height = int(input("Screen height: "))

        if operation in {1, 2, 3, 4}:
            a, b = float(input("First number: ")), float(input("Second number: "))
            print(a + b if operation == 1 else a - b if operation == 2 else a * b if operation == 3 else "Can't divide by zero" if b == 0 else a / b)

        elif operation == 5:
            a, b, c = [float(input(f"Enter {x}: ")) for x in ["A", "B", "C"]]
            d = b**2 - 4*a*c
            print("No real solutions" if d < 0 else -b / (2 * a) if d == 0 else f"Roots: {(-b - math.sqrt(d)) / (2 * a)}, {(-b + math.sqrt(d)) / (2 * a)}")

        elif operation == 6:
            p, r, t, n = float(input("Principal: ")), float(input("Rate: ")), float(input("Years: ")), int(input("Compounds/year (0 for continuous): "))
            print(p * math.exp(r * t) if n == 0 else p * (1 + r / n)**(n * t))

        elif operation == 7:
            print(float(input("Base: ")) ** float(input("Exponent: ")))

        elif operation == 8:
            a, b, c = [float(input(f"Enter {x}: ")) for x in ["A", "B", "C"]]
            eq = Eq(3 * a * symbols('x')**2 + 2 * b * symbols('x') + c, 0)
            print(solve(eq))

        elif operation == 9:
            n = int(input("Count: "))
            print(sum(float(input(f"Number {i+1}: ")) for i in range(n)) / n)

        if mode in [1, 2]:
            screen = turtle.Screen()
            screen.setup(screen_width, screen_height)
            screen.bgcolor("#333")
            screen.tracer(0)
            Graph("#FF6347", lambda x: x, 2, True, screen_width, screen_height).draw()
            screen.update()

        if input("Continue? (Y/N): ").strip().upper() != "Y":
            break

class Graph:
    def __init__(self, color, equation, dot_size, graph_line, width, height):
        self.eq = equation
        self.line_size = dot_size
        self.width, self.height = width, height
        self.t = turtle.Turtle() if graph_line else None
        if self.t:
            self.t.pensize(dot_size)
            self.t.speed(0)
            self.draw_axes()

    def draw_axes(self):
        self.t.color("#000")
        for coord in [((-self.width / 2, 0), (self.width / 2, 0)), ((0, -self.height / 2), (0, self.height / 2))]:
            self.t.penup(), self.t.goto(*coord[0]), self.t.pendown(), self.t.goto(*coord[1]), self.t.penup()

    def draw(self):
        if not self.t:
            return
        for x in range(-self.width // 2, self.width // 2):
            y = self.eq(x)
            if math.isnan(y):
                self.t.penup()
            else:
                self.t.goto(x, y)
                self.t.dot(self.line_size)

if __name__ == "__main__":
    main()
