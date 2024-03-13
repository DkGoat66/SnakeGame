from turtle import Turtle

# Global constants for scoreboard display
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Load high score from an external file
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # Setting up initial scoreboard appearance
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear existing scoreboard and update with new scores
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Update high score if current score surpasses it, reset the score to 0
        if self.score > self.high_score:
            self.high_score = self.score
            # Write a new high score to external file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        # Increase score by 1 and update scoreboard
        self.score += 1
        self.update_scoreboard()
