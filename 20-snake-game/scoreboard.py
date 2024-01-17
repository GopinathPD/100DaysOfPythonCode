from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def write_score(self):
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(f"Score : {self.score}", True, align=ALIGNMENT, font=FONT)
