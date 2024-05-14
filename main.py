import os
import tkinter as tk

#путь к файлу
full_path = __file__

#путь к папке
directory_path = os.path.dirname(full_path)

#путь к папке с изображением
images_path = os.path.join(directory_path, 'img')

#путь к изображению
image_path = os.path.join(images_path, '01.png')

window = tk.Tk()
photo_image = tk.PhotoImage(file=image_path)

#показываем изображение
tk.Label(window, image=photo_image).pack()
window.mainloop()