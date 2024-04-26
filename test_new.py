import tkinter as tk
import random
from questions import questions


class App:
    '''Приложение'''
    def __init__(self, shuffle_questions=False) -> None:
        self.window = tk.Tk()
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.window.option_add('*Font', ('Consolas', 30))

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}')

        self.main_frame = tk.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        self.question_index = None
        self.correct_answers = None
        self.incorrect_answers = None
        self.shuffle_questions = shuffle_questions

        self.start()
        self.window.mainloop()

    def start(self) -> None:
        ''' Начинает викторину '''
        self.question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        if self.shuffle_questions:
            random.shuffle(questions)
        self.show_question()

    def show_question(self) -> None:
        ''' Создаёт виджеты и наполняет их контентом вопроса '''
        question = questions[self.question_index]
        tk.Label(self.main_frame, text=question['текст вопроса']).pack()
        for answer in question['варианты ответов']:
            tk.Button(
                self.main_frame,
                text=answer,
                command=lambda arg=answer: self.on_button(arg) 
            ).pack()

    def on_button(self, button_text: str) -> None:
        question = questions[self.question_index]
        if button_text == question['верный ответ']:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self) -> None:
        tk.Label(self.main_frame, text=f'верно: {self.correct_answers}').pack()
        tk.Label(self.main_frame, text=f'неверно: {self.incorrect_answers}').pack()
        tk.Button(self.main_frame, text='Заново', command=self.start()).pack()


App(shuffle_questions=True)
