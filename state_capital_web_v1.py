import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

"""
Run this from your shell
and then visit http://localhost:4000/ from your browser
"""

home_html = """
<html>
<body background='http://flightattendanttraininghq.com/wp-content/uploads/2017/09/Quiz-Time.png'>
<center>
<h1>Welcome to Quiz World</h1>
<hr>
<li><a href='/state_capital'>State Capital</li>
</center>
</html>
"""

question_answer_html_header = """
<html>
<body>
    <center>
    <h1>State Capital Questions</h1>
"""
question_answer_html_footer = """    
    </center>
</body>
</html>
"""

def get_state_capital():
    sc = []
    conn = pymysql.connect(host='localhost',
                       user='root', password='keeyonghan',
                       db='test', charset='utf8')
    curs = conn.cursor()
    sql = "select state, capital from state_capital"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        sc.append({ 'state':row[0], 'capital':row[1] })
    conn.close()
    return sc

@app.route("/")
def index():
    return home_html

@app.route("/state_capital", methods=['GET'])
def state_capital():
    sc_list = get_state_capital()
    html = question_answer_html_header
    for sc in sc_list:
        qa_pair = "<h3>Capital of <b>" + sc['state'] + "</b> is <i>" + sc['capital'] + "</i></h3><p>"
        html += qa_pair
    html += question_answer_html_footer
    return html
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
