import pymysql
'''
create table test.state_capital (
    state varchar(32),
    capital varchar(64)
);

insert into test.state_capital value ("California", "Sacramento");
insert into test.state_capital value ("Nevada", "Carson City");
insert into test.state_capital value ("Washington", "Olympia");

'''
def get_state_capital():
    sc = { }
    conn = pymysql.connect(host='localhost',
                       user='root', password='keeyonghan',
                       db='test', charset='utf8')
    curs = conn.cursor()
    sql = "select state, capital from state_capital"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        state = row[0]
        capital = row[1]
        sc[state] = capital
    return sc

def get_and_check_answer(state, real_answer):
    user_answer = input("What is the capital of " + state + "?")
    if (real_answer.upper() == user_answer.upper()):
        return True
    else:
        return False

def display_point(point):
    print("You have " + str(point) + " point(s).")

print("Welcome to State Quiz!")
correct = 0

state_capital = get_state_capital()

for state, capital in state_capital.items():
    if get_and_check_answer(state, capital):
        correct = correct + 1
        print("Good job!")
    else:
        print("Incorrect. The anwer is " + capital + ".")
    display_point(correct)
