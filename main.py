import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("India States Game")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("India_states.csv")
states = data['state'].to_list()


guessed_states = []
while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states correct",
                                    prompt="whats another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # missing_states = []
        # for state in state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("India_states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




