# 26. В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.
import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'Достоевск[а-я]+'
matches = set(re.findall(pattern, text, re.I))

for match in matches:
    print(match)
