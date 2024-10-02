import turtle
import pandas
#from brain import AnswerText
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Name a state").title()


    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        state_save = pandas.DataFrame(missing_states)
        state_save.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
    else: print("You already guessed that state")




