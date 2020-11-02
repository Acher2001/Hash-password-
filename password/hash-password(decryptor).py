#Создоно 26.10.2020 
#Черепанов Александр Михаилович
#hash-password(decryptor)
import hashlib
import os

password=str(input("введите пароль: "))

f1=open('salt.txt','r')
salt=f1.read()
f1.close()

f2=open('key.txt','r')
key=f2.read()
f2.close()

new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)

if key == str(new_key):
    print("пароль правельный")
else:
    print("пароль неверен")
input("\n\nВведите Enter. чтобы выйти.")
