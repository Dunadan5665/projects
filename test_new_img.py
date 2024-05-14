import tkinter as tk
import random
from questions import questions
import datetime
import os


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

        full_path = __file__  #путь к файлу
        directory_path = os.path.dirname(full_path)  #путь к папке
        self.image_path = os.path.join(directory_path, 'img')  #путь к папке с изображением

        self.start_time = None
        self.end_time = None

        self.start()
        self.window.mainloop()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def start(self) -> None:
        ''' Начинает викторину '''
        self.start_time = datetime.datetime.now()
        self.question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        if self.shuffle_questions:
            random.shuffle(questions)
        self.clear_main_frame()
        self.show_question()

    def show_question(self) -> None:
        ''' Создаёт виджеты и наполняет их контентом вопроса '''
        question = questions[self.question_index]
        if question.get('картинка') is not None:
            self.img_name = question['картинка']
            file = os.path.join(self.image_path, self.img_name)
            photo_image = tk.PhotoImage(file=file)
            tk.Label(
                master=self.main_frame,
                image=photo_image
            ).pack
        tk.Label(
            self.main_frame, text=question['текст вопроса']
            ).pack(pady=(0, 30))
        buttons_frame = tk.Frame(self.main_frame)
        buttons_frame.pack()
        for answer in question['варианты ответов']:
            tk.Button(
                buttons_frame,
                text=answer,
                command=lambda arg=answer: self.on_button(arg)
            ).pack(
                side='left',
                padx=20
                )

    def on_button(self, button_text: str) -> None:
        question = questions[self.question_index]
        if button_text == question['верный ответ']:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        self.clear_main_frame()

        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self) -> None:
        self.end_time = datetime.datetime.now()
        total_time = self.end_time - self.start_time

        tk.Label(
            self.main_frame,
            text=f'Всего вопросов: {len(questions)}'
        ).pack()

        tk.Label(
            self.main_frame,
            text=f'время: {total_time}'
        ).pack()

        tk.Label(
            self.main_frame,
            text=f'верно: {self.correct_answers}'
            ).pack()

        tk.Label(
            self.main_frame,
            text=f'неверно: {self.incorrect_answers}'
            ).pack()

        tk.Button(
            self.main_frame,
            text='Заново',
            command=lambda: self.start()
            ).pack()


App(shuffle_questions=True)

