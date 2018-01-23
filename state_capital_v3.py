print("Welcome to State Quiz!")
correct = 0

def get_and_check_answer(state, real_answer):
    user_answer = input("What is the capital of " + state + "?")
    if (real_answer.upper() == user_answer.upper()):
        return True
    else:
        return False

def display_point(point):
    print("You have " + str(point) + " point(s).")

state_capital = {
     "California": "Sacramento",
     "Nevada": "Carson City",
     "Washington": "Olympia"
}

for state, capital in state_capital.items():
    if get_and_check_answer(state, capital):
        correct = correct + 1
        print("Good job!")
    else:
        print("Incorrect. The anwer is " + capital + ".")
    display_point(correct)
