import random
from tkinter import ttk, Tk, Label, Entry, CENTER, END
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

word_letters = random.choice(animals_word_list)
guessed_letters = set()
tries = 7

# Интерфейс
word = Label(root, text="", font=("Bahnschrift", 24))
word.pack(pady=20)

tries_label = Label(root, text=f"Осталось попыток: {tries}", font=("Bahnschrift", 14))
tries_label.pack()

hangman_display = Label(root, text="", font=("Courier", 18), justify=CENTER)
hangman_display.pack(pady=10)

entry = Entry(root, font=("Bahnschrift", 18), width=3, justify="center")
entry.pack(pady=10)
entry.focus()

message = Label(root, text="", font=("Bahnschrift", 12))
message.pack()

def update_hangman_display(tries):
    stages = [
        "             \n             \n             \n             \n             \n             ",
        "________      \n|      |      \n|             \n|             \n|             \n|             ",
        "________      \n|      |      \n|      0      \n|             \n|             \n|             ",
        "________      \n|      |      \n|      0      \n|      |      \n|             \n|             ",
        "________      \n|      |      \n|      0      \n|     /|      \n|             \n|             ",
        "________      \n|      |      \n|      0      \n|     /|\\    \n|             \n|             ",
        "________      \n|      |      \n|      0      \n|     /|\\    \n|     /       \n|             ",
        "________      \n|      |      \n|      0      \n|     /|\\    \n|     / \\    \n|             "
    ]
    index = 7 - tries
    if index >= len(stages):
        index = len(stages) - 1
    hangman_display.config(text=stages[index])


def update_display():
    display_word = ""
    for letter in word_letters:
        display_word += letter + " " if letter in guessed_letters else "_ "
    word.config(text=display_word.strip())
    tries_label.config(text=f"Осталось попыток: {tries}")
    update_hangman_display(tries)


def button_clicked():
    global tries
    guess = entry.get().lower()
    entry.delete(0, END)
    message.config(text="", fg="black")

    if len(guess) != 1:
        message.config(text="Введите одну букву.", fg="red")
        return

    if not re.fullmatch(r'[а-яё]', guess):
        message.config(text="Введите букву русского алфавита.", fg="red")
        return

    if guess in guessed_letters:
        message.config(text="Эта буква уже была.", fg="red")
        return

    guessed_letters.add(guess)

    if guess in word_letters:
        message.config(text="Верно!", fg="green")
    else:
        tries -= 1
        message.config(text=f"Неверно! Осталось попыток: {tries}", fg="red")

    update_display()

    if all(letter in guessed_letters for letter in word_letters):
        message.config(text=f"Вы угадали слово: {word_letters}", fg="green")
        guess_btn.config(state="disabled")
        entry.config(state="disabled")
    elif tries == 0:
        message.config(text=f"Вы не угадали слово: {word_letters}", fg="red")
        guess_btn.config(state="disabled")
        entry.config(state="disabled")


guess_btn = ttk.Button(root, text='Угадать букву', command=button_clicked)
guess_btn.pack(pady=10)

update_display()
root.mainloop()
