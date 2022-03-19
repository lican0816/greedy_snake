from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
FONT_COLOR = 'white'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # Initial the score to 0
        self.color(FONT_COLOR)
        self.penup()  # Does not draw line
        self.goto(0, 270)  # Show in the top middle
        self.update_score_display()
        self.hideturtle()  # Hide the turtle from screen

    def increase_score(self):
        """
        Increase the score by 1
        """
        self.score += 1
        self.update_score_display()

    def update_score_display(self):
        """
        Update the score showing on the screen
        """
        self.clear()  # Clear the previous score on the screen
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Show GAME OVER in the center of screen
        """
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
