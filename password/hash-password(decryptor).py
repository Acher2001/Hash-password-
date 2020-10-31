import hashlib
import os

password=str(input("введите пароль: "))

f1=open('salt.txt','r')
salt=f1.read()
f1.close()

f2=open('key.txt','r')
key=f2.read()
f2.close()

new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

if key == new_key:
    print("пароль правельный")
else:
    print("пароль неверен")
input("\n\nВведите Enter. чтобы выйти.")