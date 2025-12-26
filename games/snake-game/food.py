import random
from turtle import Turtle

colors = ["red","green","blue","pink","orange","magenta","cyan","yellow"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")

        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh()


    def refresh(self):
        self.color(random.choice(colors))
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
