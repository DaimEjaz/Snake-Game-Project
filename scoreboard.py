from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 18, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f'Score: {self.score}', False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.display_score()
