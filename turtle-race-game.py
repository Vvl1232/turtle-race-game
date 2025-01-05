from turtle import Turtle, Screen
import random as rd

# Initialize screen
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")

# Function to get user bet
def get_user_bet():
    while True:
        user_bet = s.textinput(title="Make your bet on which turtle might win!!!",
                               prompt="Enter a color from 'pink'/'red'/'beige'/'green'/'DeepSkyBlue'/'purple'/'orange'")
        if user_bet in colors:
            return user_bet
        print("Invalid color. Please enter a valid color.")

# Initialize game
s.title("TURTLE RACE")
colors = ["pink", "red", "beige", "green", "DeepSkyBlue", "purple", "orange"]
positions = [0, 90, 180, 270, -90, -180, -270]
all_turtles = []

# Get user bet
user_bet = get_user_bet()
print(user_bet)

# ==================================random steps function===========================
step = [2, 4, 6, 7, 8]

def go():
    global is_race_on
    while is_race_on:
        for turtle in all_turtles:
            move = rd.choice(step)
            turtle.forward(move)
            if turtle.xcor() > 280:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"Congratulations! The {winning_color} turtle won!")
                else:
                    print(f"Sorry, the {winning_color} turtle won. Better luck next time!")

# ==================================Turtles==========================================
for turtle_index in range(7):
    t = Turtle()
    t.pu()
    t.color(colors[turtle_index])
    t.shape('turtle')
    t.goto(x=-290, y=positions[turtle_index])
    all_turtles.append(t)

# ==================================action to game play=================================================
is_race_on = False
if user_bet in colors:
    is_race_on = True
    go()
else:
    print("Invalid color. Please enter a color")

s.exitonclick()
