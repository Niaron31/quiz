from flask import *

from data import get_count_quiz
from random import randint
def index():
    global quiz, last_q
    count_quiz = get_count_quiz()
    quiz = randint(1,count_quiz)
    last_q = 0
    return '<a href= "/test"> Test </a>" + "<p>" + str(quiz)  + "</a>"'



def test():
    global last_q

    cur_q = get_count_after(quiz,last_q)
    if cur_q is None or len(cur_q) == 0:
        redirect(url_for('result'))

def result():
    return "result"




app = Flask(__name__)
app.add_url_rule("/", "index",index)
app.add_url_rule("/test", 'test',test)
app.add_url_rule("/result",'result',result)

app.run()