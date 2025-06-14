import random
from tkinter import ttk
from tkinter import *
import re
root = Tk()
root.title("Игра Hangman на тему: Животные")
root.geometry('500x500+700+300')

# Список слов
animals_word_list = ["кот", "собака", "осел", "козел", "лошадь", "свинья", "кролик", "трубкозуб", "альбатрос",
    "аллигатор", "альпака", "амфибия", "анаконда", "удильщик", "муравьед", "антилопа",
    "лев", "тигр", "медведь", "волк", "лиса", "заяц", "олень", "кабан", "белка", "бегемот", "слон",
    "жираф", "обезьяна", "кенгуру", "енот", "барсук", "дельфин", "кит", "корова", "ёж", "орёл", "сова",
    "воробей", "голубь", "ворона", "фламинго", "пеликан", "пингвин", "аист", "соловей", "кукушка", "попугай",
    "лебедь", "утка", "журавль", "крокодил", "ящерица", "черепаха", "игуана", "хамелеон", "лягушка", "жаба",
    "саламандра", "тритон", "акула", "скат", "карп", "форель", "тунец", "золотая рыбка", "морской конёк", "сельдь",
    "сом", "муравей", "пчела", "бабочка", "комар", "жук", "кузнечик", "таракана", "стрекоза", "божья коровка", "мотылёк",
    "паук", "скорпион", "клещ", "осьминог", "кальмар", "улитка", "мидия", "устрица", "медуза", "морская звезда", "краб", "лангуст", "морской ёж"]

#Переменные
word_letters = random.choice(animals_word_list)
guessed_letters = set()
tries = 7

#Интерфейс
# Метка для отображения слова
word = Label(root, text="", font=("Bahnschrift", 24))
word.pack(pady=20)

# Метка для попыток
tries_label = Label(root, text=f"Осталось попыток: {tries}", font=("Bahnschrift", 14))
tries_label.pack()

# Метка для отображения рисунка
hangman_display = Label(root, text="", font=("Courier", 18), justify=CENTER)
hangman_display.pack(pady=10)

# Поле ввода буквы
entry = Entry(root, font=("Bahnschrift", 18), width=3, justify="center")
entry.pack(pady=10)
entry.focus()

# Метка для сообщений
message = Label(root, text="", font=("Bahnschrift", 12), fg="red")
message.pack()


# Функция для обновления рисунка виселицы в зависимости от оставшихся попыток
def update_hangman_display(tries):
    stages = [
        # 7 попыток - пусто (начальное состояние)
        "             \n"
        "             \n"
        "             \n"
        "             \n"
        "             \n"
        "             ",
        # 6 попыток - только каркас
        "________      \n"
        "|      |      \n"
        "|             \n"
        "|             \n"
        "|             \n"
        "|             ",
        # 5 попыток
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|             \n"
        "|             \n"
        "|             ",
        # 4 попытки
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|      |      \n"
        "|             \n"
        "|             ",
        # 3 попытки
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|     /|      \n"
        "|             \n"
        "|             ",
        # 2 попытки
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|     /|\\    \n"
        "|             \n"
        "|             ",
        # 1 попытка
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|     /|\\    \n"
        "|     /       \n"
        "|             ",
        # 0 попыток — полный рисунок
        "________      \n"
        "|      |      \n"
        "|      0      \n"
        "|     /|\\    \n"
        "|     / \\    \n"
        "|             "
    ]
    index = 7 - tries
    if index >= len(stages):
        index = len(stages) - 1
    hangman_display.config(text=stages[index])


def update_display():
    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word.config(text=display_word)
    tries_label.config(text=f"Осталось попыток: {tries}")
    update_hangman_display(tries)


def button_clicked():
    global tries
    guess = entry.get().lower()
    entry.delete(0, END)

    if len(guess) != 1:
        message.config(text="Введите одну букву.")
        return

    if not guess.isalpha():
        message.config(text="Введите букву русского алфавита.")
        return

    pattern = r'[а-яА-ЯёЁ]'
    if not re.fullmatch(pattern, guess):
        message.config(text="Введите букву русского алфавита.")
        return

    if guess in guessed_letters:
        message.config(text="Эта буква уже была.")
        return

    guessed_letters.add(guess)

    if guess in word_letters:
        message.config(text="Верно!")
    else:
        tries -= 1
        message.config(text=f"Неверно! Осталось попыток: {tries}")

    update_display()

    if all(letter in guessed_letters for letter in word_letters):
        message.config(text=f"Вы угадали слово: {word_letters}")
        guess_btn.config(state=DISABLED)
        entry.config(state=DISABLED)

    elif tries == 0:
        message.config(text=f"Вы не угадали слово: {word_letters}")
        guess_btn.config(state=DISABLED)
        entry.config(state=DISABLED)


guess_btn = ttk.Button(root, text='Угадать букву', command=button_clicked)
guess_btn.pack(pady=10)

update_display()
root.mainloop()
