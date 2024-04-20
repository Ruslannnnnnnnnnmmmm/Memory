#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle,randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton,QGroupBox,QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Какой национальности не существует','Энцы','Смурфы','Чулымцы','Алеуты'))
 
    

app = QApplication([])
main_win = QWidget()



RadioGroupBox = QGroupBox('Варианты ответа')
question = QLabel('')
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
button = QPushButton('Ответить')
RadioGroupBox.setLayout(layout_ans1)
hlayot1 = QHBoxLayout()
hlayot1.addWidget(question,alignment= Qt.AlignCenter)
hlayot2 = QHBoxLayout()
ansGroupBox = QGroupBox()
hbox_ans = QVBoxLayout()
lb_correct = QLabel()
lb_answer = QLabel()
hbox_ans.addWidget(lb_correct, alignment= Qt.AlignTop | Qt.AlignLeft)
hbox_ans.addWidget(lb_answer, alignment=  Qt.AlignCenter)
ansGroupBox.setLayout(hbox_ans)
ansGroupBox.hide()
hlayot2.addWidget(RadioGroupBox, alignment= Qt.AlignCenter)
hlayot2.addWidget(ansGroupBox, alignment= Qt.AlignCenter)
hlayot3= QHBoxLayout()
hlayot3.addWidget(button, alignment = Qt.AlignCenter)
v_line = QVBoxLayout()
v_line.addLayout(hlayot1)
v_line.addLayout(hlayot2)
v_line.addLayout(hlayot3)
main_win.setLayout(v_line)
ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)
buttons = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def show_question():
    RadioGroupBox.show()
    ansGroupBox.hide()
    setText('Ответить')
    ButtonGroup.setExclusive(True)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(False)


def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)

def show_correct(res):
    lb_correct.setText(res)
    show_result()


def check_answer():
    if buttons[0].isChecked():
        show_correct("Правильно")
    else:
        show_correct('Неверно')

def show_result():
    RadioGroupBox.hide()
    ansGroupBox.show()
    button.setText('Следующий вопрос')

def next_question():
    cur_question = randint(0,len(question_list) - 1)
    ask(question_list[cur_question])

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

# def start_test():
#     if button.text() == 'Ответить':
#         show_result()
#     else:
#         show_guestion() 

# ask()
next_question()
button.clicked.connect(click_ok)

main_win.show()
app.exec_()






















#FROM RANDOW IMPORT SHUFFFLE