eng_rus_dict = {
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


word = "water"
translation = eng_rus_dict.get(word, "Перевод не найден")
print(f"Перевод слова '{word}': {translation}")
