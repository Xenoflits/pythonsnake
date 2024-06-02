from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hiscore = 0
       
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.hiscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.hiscore:
            self.hiscore = self.score
        self.clear()
        self.update_scoreboard()
        
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        
        self.reset()
        

