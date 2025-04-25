d1 = {
    "мышь": "mousse",
    "клавиатура": "keyboard",
    "монитор": "monitor",
    "вода": "water",
    "цвет": "color",
    "глаз": "eye",
    "звук": "sound",
    "книга": "book",
    "автобус": "bus"
}

w = input()
tr = d1.get(w, "НЕ найдено")
print(f"Перевод слова '{w}': {tr}")