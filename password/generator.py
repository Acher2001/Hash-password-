from tkinter import *
import hashlib
import os


root=Tk()

password='0'

def clic():
    password=str(password0.get())
    s = os.urandom(32)
    file2=open('salt.txt','w')
    file2.write(str(s))
    file2.close()

    f1=open('salt.txt','r')
    salt=f1.read()
    f1.close()

    key=hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    file1=open('key.txt','w')
    file1.write(str(key))
    file1.close()


    print(key)
    print("\n\n",salt)

root['bg']='#fafafa'  #Вводим фон
root.title('Проба 1')  #Вводим название
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
btn=Button(frame, text='Сохранить', bg='#fafafa', command=clic)  #Кнопка
btn.pack()



root.mainloop()  #Постояный цикл запуска окна
