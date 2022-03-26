import tkinter as tk  #импорт библиотеки tkinter

window = tk.Tk() # cоздание окна

label = tk.Label(text="Name") # cоздает ярлык
entry = tk.Entry(fg="yellow", bg="blue", width=50) # cоздает однострочное поле ввода
label.pack() # добавляет элемент в окно методом раметки pack()
entry.pack() # -#-
name = entry.get()
print(name)
window.mainloop() # указывает python что нужно запустить цикл событий Tkinter, требуется для событий вроде нажатия кнопки

