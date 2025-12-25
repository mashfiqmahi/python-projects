import turtle
import pandas
screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer_states = []
while len(answer_states) < 50:
    user_input = screen.textinput(title=f"{len(answer_states)}/50 states correct",prompt="What's another state name?")

    # Check if the user clicked "Cancel" or closed the window
    if user_input is None:
        missing_states = [state for state in all_states if state not in answer_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    answer_state = user_input.title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in answer_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("data.txt")
        break

    if answer_state in all_states and answer_state not in answer_states:
        answer_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)

screen.exitonclick()


