import turtle
import pandas
import time
from textboard import TextBoard

BACKGROUND_IMAGE = "IndiaMap.gif"

states = pandas.read_csv("indian_states.csv")

states_list = states.state.to_list()
visited_states = []

screen = turtle.Screen()
screen.addshape(BACKGROUND_IMAGE)
screen.title("Guess the Indian State")
screen.tracer(0)

turtle.shape(BACKGROUND_IMAGE)
score = TextBoard(turtle)
timer = TextBoard(turtle)
feedback = TextBoard(turtle)

game_on = True
count = 0
time_counter = 600

while game_on:
    score.board.goto(101, 290)
    timer.board.goto(253, 290)
    
    score.score(count)
    timer.timer(time_counter)
    
    screen.update()
    time_counter -= 1
    
    user_guess = screen.textinput(title="Guess the state", prompt="Can you name the state? or Type 'Exit' to exit").title()

    if user_guess == "Exit":
        break

    elif len(states_list) == len(visited_states):
        game_on = False
        feedback.board.goto(0, 0)
        feedback.you_won()
    
    elif user_guess in visited_states or user_guess not in states_list:
        continue
    
    elif user_guess in states_list:
        x = int(states[states.state == user_guess].x)
        y = int(states[states.state == user_guess].y)
        feedback.board.goto(x, y)
        feedback.state_name(user_guess)
        # feedback.write(arg=f"{user_guess}", align="center", font=("ribbon", 5, "bold"))
        visited_states.append(user_guess)
        count += 1

missed_states = [state_names for state_names in states_list if state_names not in visited_states]

missed_states_series = pandas.Series(missed_states)
missed_states_series.to_csv("output/report.csv")