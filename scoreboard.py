from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-200, 250)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)

    def score_increase(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.penup()
        self.home()
        self.write(arg=f"Game over", align="center", font=FONT)

