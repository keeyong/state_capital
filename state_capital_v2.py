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

states = [ "California", "Nevada", "Washington" ]
capitals = [ "Sacramento", "Carson City", "Olympia" ]
index = 0

while (index < len(states)):
    state = states[index]
    capital = capitals[index]
    if get_and_check_answer(state, capital):
        correct = correct + 1
        print("Good job!")
    else:
        print("Incorrect. The anwer is " + capital + ".")
    display_point(correct)
    index = index + 1
