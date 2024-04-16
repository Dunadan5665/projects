import tkinter

questions = [
    {
        'текст вопроса': 'Какой из этих типов данных изменякмый?',
        'варианты ответов': ['tuple', 'list', 'str', 'int'],
        'индекс верного ответа': 1
    },
    {
        'текст вопроса': 'Какой оператор умножает цифры?',
        'варианты ответов': ['*', '**', 'x', '×'],
        'индекс верного ответа': 0
    }
]


class App:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Consolas', 30))
        self.widht = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.widht}x{self.height}')
        self.question_number = None
        self.label_question_text = None
        self.label_answer_text_1 = None
        self.label_answer_text_2 = None
        self.label_answer_text_3 = None
        self.label_answer_text_4 = None
        self.button_answer_1 = None
        self.button_answer_2 = None
        self.button_answer_3 = None
        self.button_answer_4 = None
        self.make_widgets()
        self.position_widgets()
        self.start()
        self.window.mainloop()

    def make_widgets(self) -> None:
        '''  Создать экземпляры виджетов '''
        self.label_question_text = tkinter.Label(self.window)
        self.label_answer_text_1 = tkinter.Label(self.window)
        self.label_answer_text_2 = tkinter.Label(self.window)
        self.label_answer_text_3 = tkinter.Label(self.window)
        self.label_answer_text_4 = tkinter.Label(self.window)
        self.button_answer_1 = tkinter.Button(
            self.window, text='1', command=lambda: self.on_click(1)
        )
        self.button_answer_2 = tkinter.Button(
            self.window, text='2', command=lambda: self.on_click(2)
        )
        self.button_answer_3 = tkinter.Button(
            self.window, text='3', command=lambda: self.on_click(3)
        )
        self.button_answer_4 = tkinter.Button(
            self.window, text='4', command=lambda: self.on_click(4)
        )

    def position_widgets(self) -> None:
        ''' Позиционирует виджеты в окнек '''
        self.label_question_text.pack()
        self.label_answer_text_1.pack()
        self.label_answer_text_2.pack()
        self.label_answer_text_3.pack()
        self.label_answer_text_4.pack()
        self.button_answer_1.pack()
        self.button_answer_2.pack()
        self.button_answer_3.pack()
        self.button_answer_4.pack()

    def start(self) -> None:
        self.question_number = 0
        self.label_question_text['text'] = questions[self.question_number]['текст вопроса']
        self.label_answer_text_1['text'] = '1.' + questions[self.question_number]['варианты ответов'][0]
        self.label_answer_text_2['text'] = '2.' + questions[self.question_number]['варианты ответов'][1]
        self.label_answer_text_3['text'] = '3.' + questions[self.question_number]['варианты ответов'][2]
        self.label_answer_text_4['text'] = '4.' + questions[self.question_number]['варианты ответов'][3]

    def on_click(self, button_number: int) -> None:
        print(f'нажата кнопка {button_number}')


App()
