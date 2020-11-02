#Создоно 26.10.2020 
#Черепанов Александр Михаилович
#hash-password(generator)
import hashlib
import os

password=str(input('введите пароль: '))

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

input("\n\nВведите Enter. чтобы выйти.")
