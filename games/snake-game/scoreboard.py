from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("data.txt")
        self.high_score = data.read()
        data.close()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score board : {self.score}, High score : {self.high_score}", align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(float(self.high_score)):
            self.high_score = self.score
            data = open("data.txt",mode='w')
            data.write(str(self.high_score))
            data.close()
        self.score = 0
        self.update_scoreboard()
    def increment_score(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.home()
        self.write(arg="Game over",align=ALLIGNMENT,font=FONT)