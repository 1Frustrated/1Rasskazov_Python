d = {
    "apple": "яблоко",
    "pear": "груша",
    "carrot": "морковь",
    "water": "вода",
    "book": "книга",
    "sun": "солнце",
    "moon": "луна",
    "cat": "кот",
    "dog": "собака",
    "house": "дом"
}

w = input()
r = d.get(w, "Нет")
print(r)

