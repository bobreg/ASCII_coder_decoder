from tkinter import *


def shifrator(): # Зашифровываем
    windowSecretPass.delete(first=0, last=END)
    key = int(windowKey.get())
    password = list(windowPassword.get())
    sumSumbols = len(password)
    for i in range(sumSumbols):
        password[i] = ord(password[i]) # конвертируем каждый символ в код ASCII
    for i in range(sumSumbols):
        password[i] = password[i] + key
    for i in range(sumSumbols):
        password[i] = chr(password[i]) # конвертируем код ASCII в символ
    newOpenPassword = ''
    for i in range(sumSumbols):
        newOpenPassword = newOpenPassword + password[i] # набираем символы в строку
    newOpenPassword = newOpenPassword + str(key) # приставляем ключ в конце
    windowSecretPass.insert(0, newOpenPassword) # отправляем пользователю


def rasshifrator():
    windowSecretPass.delete(first=0, last=END)
    key = int(windowKey.get())
    password = list(windowPassword.get())
    sumSumbols = len(password)
    password = list(password)
    for i in range(sumSumbols):
        password[i] = ord(password[i])
    for i in range(sumSumbols - 1):
        password[i] = password[i] - key
    for i in range(sumSumbols - 1):
        password[i] = chr(password[i])
    newSecretPassword = ''
    for i in range(sumSumbols - 1):
        newSecretPassword = newSecretPassword + password[i]
    windowSecretPass.insert(0, newSecretPassword)

# Создание окна
window = Tk()
window.title("Шифровальшик для паролей V 2.0 beta")
window.geometry("400x250")

# Создание элементов
label1 = Label(text="Только английские буквы и цифры. Ключ не более четырёх")
label2 = Label(text="Входные символы")
label3 = Label(text="Ключ")
label4 = Label(text="Выходные символы")
windowPassword = Entry()
windowKey = Entry(width=2)
windowSecretPass = Entry()
button1 = Button(text='Зашифровать', width=16, height=5, command=shifrator)
button2 = Button(text='Расшифровать', width=16, height=5, command=rasshifrator)

# Упаковка
label1.pack()
label2.place(x=40, y=70)
label3.place(x=180, y=70)
label4.place(x=240, y=70)
windowPassword.place(x=40, y=100)
windowKey.place(x=195, y=100)
windowSecretPass.place(x=240, y=100)
button1.place(x=40, y=150)
button2.place(x=240, y=150)
window.mainloop()