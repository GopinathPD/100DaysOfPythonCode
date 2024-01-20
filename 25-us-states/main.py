import pandas as pd
import turtle
from state_update import UpdateState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get the states data from csv
states_data = pd.read_csv("50_states.csv")

# Initialize the writing object
state_label = UpdateState()

# Check the state is available in the csv
states_score = 0
total_states = 50


# Update screen title
def update_title():
    screen.title(f"{states_score}/{total_states} States Correct")

guessed_states = []
game_on = True

while states_score <= total_states and game_on:
    # Get the user input and convert to Title case
    user_state = screen.textinput(title=f"{states_score}/{total_states} States Correct",
                                  prompt="What's another state's name?").title()

    answer_state = states_data[states_data["state"] == user_state]
    if user_state.lower() == "exit":
        game_on = False
    else:
        if answer_state.empty:
            pass
        else:
            x = answer_state["x"].iloc[0]
            y = answer_state["y"].iloc[0]
            state_name = answer_state["state"].iloc[0]
            state_label.update_state(x, y, state_name)
            states_score += 1
            guessed_states.append(state_name)

# Find the missing states
all_states = states_data["state"].tolist()
missing_states = list(set(all_states).difference(guessed_states))

# Write the missing states in csv
missing_states_csv = pd.DataFrame(missing_states)
missing_states_csv.to_csv("missing_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
