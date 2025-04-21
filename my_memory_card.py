from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup, QInputDialog)
from random import *
from time import *


class Question():
    def __init__(self, question, right_answer,
    wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

question_list.append(Question('1.Перевод:"My life is my poetry, my love making is my legacy".', 'моя жизнь - моя поэзия, моя любовь - мое наследие', 'моя жизнь - мои правила, моя любовь - моя жизнь ', 'моя жизнь - моё всё, моя любовь - мое утешение ', 'моя жизнь - моя жажда, моя любовь - мое всё'))
question_list.append(Question('2.Дата рождения Ланы Дель Рей.', '21.06.1985', '21.11.1999', '13.09.1995', '21.04.1982'))
question_list.append(Question('4.Как называется эта теория: "Вселенная состоит из крохотных колеблющихся струн, каждая нота которых соответствует элементарной частице".', 'теория струн', 'теория Шрёдингера', 'теория параллельных миров', 'теория всего'))
question_list.append(Question('5.Кто создал данную формулу: "E = mс2".', 'Энштейн', 'Максвелл', 'Шредингер', 'Ньютон'))
question_list.append(Question('6.Ученый, заложивший основы электричества и магнетизма.', 'Майкл Фарадей', 'Джеймс Максвелл', 'Ньютон', 'Архимед'))
question_list.append(Question('7.Значимое свойство во Вселенной, указывающее на глубокий основополагающий физический принцип.', 'симметрия', 'сила притяжения', 'вакуум', 'бесконечность'))
question_list.append(Question('8.Сколько штатов в США.', '50', '51', '52', '49'))
question_list.append(Question('9.Годы первой мировой войны.', '1914-1918', '1920-1939', '1916-1918', '1939-1941'))
question_list.append(Question('10.Годы второй мировой войны.', '1939-1945', '1941-1945', '1913-1945', '1949-1953'))
question_list.append(Question('11.Столица Шотландии.', 'Эдинбург', 'Скотлэнд', 'Швеция', 'Ефрейбург'))
question_list.append(Question('12.Как переводится:"betrayal".', 'предательство', 'доверие', 'обида', 'знакомство'))
question_list.append(Question('13.Как сказать "будь проще."', 'keep it simple', 'keep it real', 'keep it simply', 'keep it so'))


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400,200)

#создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
window.count = 0
window.total = 0
lb_counter = QLabel('Cчёт: ' + str(window.count))
lb_counter.setStyleSheet('color: rgb(198,54,120);')
lb_total = QLabel('Всего вопросов: ' + str(window.total))
lb_total.setStyleSheet('color: rgb(43,44,124);')
window.start = time()
label = QLabel(' ')


RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

#Создаем панель результата
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неверно') #здесь размещается надпись правильно или неправильно
lb_Correct = QLabel('Правильный ответ') #здесь будет написан текст правильного ответа
lb_Correct.setStyleSheet("font-size: 15px")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

#Размещаем все виджеты в окне
layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout()  #варианты ответов или результат теста
layout_line3 = QHBoxLayout()  #кнопка ответить

layout_line1.addWidget(lb_Question, alignment=Qt.AlignLeft )
layout_line1.addWidget(lb_counter, alignment=Qt.AlignRight)
layout_line1.addWidget(lb_total, alignment=Qt.AlignRight)
#размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(label, alignment = Qt.AlignCenter)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
label.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) #кнопка должна быть большой
layout_line3.addStretch(1)
#теперь созданные строки разместим друг под другом:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #пробелы между содержимым

def show_result(): 
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')

    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
        
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись 
    'результат' и покажем нужную панель '''
    lb_Result.setText(res)
    if res == 'Правильно!':
        lb_Result.setStyleSheet('color: rgb(0,128,0);')
    else:
        lb_Result.setStyleSheet('color: rgb(255,0,0);')
    show_result()


def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и 
    показать панель ответов '''
    window.total += 1
    lb_total.setText('Всего вопросов: ' + str(window.total))
    if answers[0].isChecked():
        layout_res.addWidget(lb_Result, alignment=Qt.AlignCenter)
        lb_Correct.hide()
        show_correct('Правильно!')
        window.count += 1
        lb_counter.setText('Счёт: ' + str(window.count))
        if window.count == int(personal_choice):
            RadioGroupBox.hide()
            AnsGroupBox.hide()
            lb_Question.hide()
            btn_OK.hide()
            label.show()
            window.end = time()
            window.time = window.end - window.start
            window.time = window.time // 1
            lb_time = QLabel('Время прохождения: ' + str(window.time) + ' сек')
            layout_line2.addWidget(lb_time, alignment = Qt.AlignCenter)
            label.setText('Вы набрали ' + str(personal_choice) + ' очка(ов)! Тренировка окончена!')
            
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            lb_Correct.show()
            layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
            layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
            AnsGroupBox.setLayout(layout_res)
            show_correct('Неверно!')
            window.count -= 1
            lb_counter.setText('Счёт: ' + str(window.count))

def next_question():
    ''' задает следующий вопрос из списка'''
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]# взяли вопрос
    ask(q) #спросили
    
def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Следующий вопрос':
        next_question()

personal_choice, ok = QInputDialog.getText(
        window, "Тренировка", "Введите количество очков: "
    )

btn_OK.clicked.connect(click_ok) #проверяем что панель ответов показывается при нажатии на кнопку
next_question()
window.setLayout(layout_card)
window.show()
app.exec_()

