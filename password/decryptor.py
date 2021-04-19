from tkinter import *
import hashlib
import os
from tkinter import messagebox

root=Tk()
password='0'
info_str='0'


def clic():
    password=str(password0.get())

    f1=open('salt.txt','r')
    salt=f1.read()
    f1.close()

    f2=open('key.txt','r')
    key=f2.read()
    f2.close()

    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)

    if key == str(new_key):
        otv="правельный"
    else:
        otv="неверен"

    info_str=f'Пароль: {otv}'
    messagebox.showinfo(title='Обработка пароля', message=info_str)

root['bg']='#fafafa'  #Вводим фон
root.title('Пароль')  #Вводим название
root.wm_attributes('-alpha', 0.85)  #Вводим прозрачность окна
root.geometry('300x100')  #Вводим размер окна

root.resizable(width=False, height=False)  #Огроничение размера окна

canvas=Canvas(root, height=300, width=100)  #Создоём холст
canvas.pack()

frame=Frame(root, bg='red')  #Рамка с другими виз. кампонентоми
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)  #Обект

title=Label(frame, text='Введите пароль', bg='#990066', font=40)  #Текст
title.pack()
password0=Entry(frame, bg='#fafafa', show='*')
password0.pack()
btn=Button(frame, text='Проверить', bg='#fafafa', command=clic)  #Кнопка
btn.pack()


root.mainloop()  #Постояный цикл запуска окна
