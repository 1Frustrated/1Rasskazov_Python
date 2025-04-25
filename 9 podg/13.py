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

word = 'глаз'
tr = d1.get(word, "НЕ найдено")
print(f"Перевод слова '{word}': {tr}")