import turtle


import pandas

screen = turtle.Screen()
screen.title("U.S. States Game.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

remaining_state_data ={
    "states" : [],
    "x" : [],
    "y"  : []
}


def turtle_write(state_x,state_y,state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(state_x,state_y)
    t.write(state)

def remaining_state(guess_state,state_list,df):
    for item in state_list:
        if item not in guess_state:
            remaining_state_data["states"].append(item)
            x = df[df["state"] == item].x.item()
            y = df[df["state"] == item].y.item()
            remaining_state_data["x"].append(x)
            remaining_state_data["y"].append(y)

    remaining_state_df = pandas.DataFrame(remaining_state_data)
    remaining_state_df.to_csv("remaining_states.csv")
    print("successfully created the remaning list file")



# test = "alabama"
#
df = pandas.read_csv("50_states.csv")


states_list = df["state"].tolist()
count = 0
guessed_state = []
while len(guessed_state) < len(states_list):

    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(states_list)}Guess the state", prompt="What's another states name?").title()

    if answer_state.lower() == "exit":
        break

    if answer_state in states_list:
        data = df[df["state"] == answer_state]
        turtle_write(data.x.item(),data.y.item(),answer_state)
        guessed_state.append(answer_state)






remaining_state(guessed_state,states_list,df)




