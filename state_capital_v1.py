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

# === California
if get_and_check_answer("California", "SACRAMENTO"):
    correct = correct + 1
    print("Good job!")
else:
    print("Incorrect. The anwer is " + real_answer + ".")
display_point(correct)

# === Nevada
if get_and_check_answer("Nevada", "Carson City"):
    correct = correct + 1
    print("Good job!")
else:
    print("Incorrect. The anwer is " + real_answer + ".")
display_point(correct)

# === Washington
if get_and_check_answer("Washington", "Olympia"):
    correct = correct + 1
    print("Good job!")
else:
    print("Incorrect. The anwer is " + real_answer + ".")
display_point(correct)
