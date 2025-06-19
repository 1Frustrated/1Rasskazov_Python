import random
from tkinter import *
import re

root = Tk()
root.title("Игра Hangman на тему: Животные")
root.geometry('500x500+700+300')

animals_word_list = ["кот", "собака", "осел", "козел", "лошадь", "свинья", "кролик", "трубкозуб", "альбатрос",
    "аллигатор", "альпака", "амфибия", "анаконда", "удильщик", "муравьед", "антилопа",
    "лев", "тигр", "медведь", "волк", "лиса", "заяц", "олень", "кабан", "белка", "бегемот", "слон",
    "жираф", "обезьяна", "кенгуру", "енот", "барсук", "дельфин", "кит", "корова", "ёж", "орёл", "сова",
    "воробей", "голубь", "ворона", "фламинго", "пеликан", "пингвин", "аист", "соловей", "кукушка", "попугай",
    "лебедь", "утка", "журавль", "крокодил", "ящерица", "черепаха", "игуана", "хамелеон", "лягушка", "жаба",
    "саламандра", "тритон", "акула", "скат", "карп", "форель", "тунец", "золотая рыбка", "морской конёк", "сельдь",
    "сом", "муравей", "пчела", "бабочка", "комар", "жук", "кузнечик", "таракана", "стрекоза", "божья коровка", "мотылёк",
    "паук", "скорпион", "клещ", "осьминог", "кальмар", "улитка", "мидия", "устрица", "медуза", "морская звезда", "краб", "лангуст", "морской ёж"]


# глобальные переменные
word_letters = ""
guessed_letters = set()
tries = 7

# интерфейс
word = Label(root, text="", font=("Bahnschrift", 24))  # метка для отображения текущего состояния слова
word.pack(pady=20)  # размещаем метку с отступом сверху и снизу

tries_lft = Label(root, text="", font=("Bahnschrift", 14))  # метка для отображения количества оставшихся попыток
tries_lft.pack()  # размещаем метку

hangman = Label(root, text="", font=("Courier", 18), justify=CENTER)  # метка для отображения виселицы
hangman.pack(pady=10)  # размещаем с отступом

entry = Entry(root, font=("Bahnschrift", 18), width=3, justify="center")  # поле ввода для буквы
entry.pack(pady=10)  # размещаем поле ввода
entry.focus()  # устанавливаем фокус ввода на это поле

message = Label(root, text="", font=("Bahnschrift", 12))  # метка для вывода сообщений игроку
message.pack(pady=10)  # размещаем метку

guess_btn = Button(root, text='Угадать букву')  # кнопка для подтверждения ввода буквы
guess_btn.pack(pady=10)  # размещаем кнопку

ng_btn = Button(root, text='Новая игра')  # кнопка для начала новой игры


def update_hangman_display(tries):
    stages = [
        # состояния виселицы от 7 попыток (пусто) до 0 (полный рисунок)
        "             \n"
        "             \n"
        "             \n"
        "             \n"
        "             \n"
        "             ",
        "________      \n"
        "|      |      \n"
        "|             \n"
        "|             \n"
        "|             \n"
        "|             ",
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|             \n"
        "|             \n"
        "|             ",
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|      |      \n"
        "|             \n"
        "|             ",
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|     /|      \n"
        "|             \n"
        "|             ",
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|    /|\\    \n"
        "|             \n"
        "|             ",
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|    /|\\    \n"
        "|    /       \n"
        "|             ",
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|    /|\\    \n"
        "|    / \\    \n"
        "|             "
    ]
    index = 7 - tries  # вычисляем индекс текущего состояния виселицы
    hangman.config(text=stages[index])  # обновляем текст метки виселицы


def button_click():
    global tries  # объявляем глобальную переменную для изменения
    guess = entry.get().lower()  # получаем введённую букву и переводим в нижний регистр
    entry.delete(0, END)  # очищаем поле ввода

    if len(guess) != 1:  # проверяем, что введена ровно одна буква
        message.config(text="Введите одну букву.", fg="red")
        return

    if not re.fullmatch(r'[а-яё]', guess):  # проверяем, что буква из русского алфавита
        message.config(text="Введите букву русского алфавита.", fg="red")
        return

    if guess in guessed_letters:  # проверяем, что буква ещё не была угадана
        message.config(text="Эта буква уже была.", fg="red")
        return

    guessed_letters.add(guess)  # добавляем букву в множество угаданных

    if guess in word_letters:  # если буква есть в слове
        message.config(text="Верно!", fg="green")
    else:
        tries -= 1  # уменьшаем количество попыток
        message.config(text=f"Неверно! Осталось попыток: {tries}", fg="red")

    update_display()  # обновляем отображение слова и попыток

    if all(letter in guessed_letters for letter in word_letters):  # если все буквы угаданы
        message.config(text=f"Вы угадали слово: {word_letters}", fg="green")
        guess_btn.config(state="disabled")  # отключаем кнопку угадывания
        entry.config(state="disabled")  # отключаем поле ввода
        ng_btn.pack(pady=10)  # показываем кнопку новой игры
    elif tries == 0:  # если попытки закончились
        message.config(text=f"Вы не угадали слово: {word_letters}", fg="red")
        guess_btn.config(state="disabled")  # отключаем кнопку угадывания
        entry.config(state="disabled")  # отключаем поле ввода
        ng_btn.pack(pady=10)  # показываем кнопку новой игры


guess_btn.config(command=button_click)  # связываем кнопку угадывания с функцией обработки нажатия


def update_display():
    display_word = ""  # строка для отображения слова с угаданными буквами и подчёркиваниями
    for letter in word_letters:
        display_word += letter + " " if letter in guessed_letters else "_ "  # показываем букву, если угадана, иначе _
    word.config(text=display_word.strip())  # обновляем метку с текущим состоянием слова
    tries_lft.config(text=f"Осталось попыток: {tries}")  # обновляем метку с количеством попыток
    update_hangman_display(tries)  # обновляем виселицу


def start_new_game():
    global word_letters, guessed_letters, tries  # объявляем глобальные переменные для изменения
    word_letters = random.choice(animals_word_list)  # выбираем случайное слово из списка
    guessed_letters = set()  # очищаем множество угаданных букв
    tries = 7  # сбрасываем количество попыток
    message.config(text="", fg="black")  # очищаем сообщение игроку
    entry.config(state="normal")  # активируем поле ввода
    guess_btn.config(state="normal")  # активируем кнопку угадывания
    entry.delete(0, END)  # очищаем поле ввода
    update_display()  # обновляем отображение слова и попыток
    ng_btn.pack_forget()  # скрываем кнопку новой игры
    entry.focus()  # устанавливаем фокус на поле ввода


ng_btn.config(command=start_new_game)  # связываем кнопку новой игры с функцией начала новой игры

start_new_game()  # запускаем новую игру при старте программы

root.mainloop()  # запускаем цикл обработки
