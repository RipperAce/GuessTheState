class TextBoard:
    def __init__(self, turtle):
        board = turtle.Turtle()
        board.hideturtle()
        board.color("black")
        board.penup()

        self.board = board

    def game_over(self):
        self.board.goto(0, 0)
        self.board.write(arg="Game Over!", align="center", font=("arial", 20, "bold"))

    def you_won(self):
        self.board.goto(0, 0)
        self.board.write(arg="You guessed all correctly!", align="center", font=("arial", 20, "bold"))

    def score(self, count):
        self.board.clear()
        self.board.write(arg=f"Score: {count}", align="center", font=("ribbon", 20, "bold"))

    def timer(self, time):
        self.board.clear()
        mins, secs = divmod(time, 60)
        time_count = '{:02d}:{:02d}'.format(mins, secs)
        self.board.write(arg=f"Time: {time_count}", align="center", font=("ribbon", 20, "bold"))

    def state_name(self, name):
        self.board.write(arg=f"{name}", align="center", font=("ribbon", 5, "bold"))