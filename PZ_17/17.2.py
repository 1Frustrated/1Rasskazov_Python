#Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и B (не включая числа A и B), а также количество N этих чисел.
import tkinter as tk


def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        if a >= b:
            result_text.set("Ошибка: A должно быть меньше B")
            output_text.delete("1.0", tk.END)
            return
        numbers = list(range(a + 1, b))
        reversed_numbers = list(reversed(numbers))
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, " ".join(map(str, reversed_numbers)) + "\n")
        output_text.insert(tk.END, f"Количество чисел: {len(numbers)}")
        result_text.set("")
    except ValueError:
        result_text.set("Ошибка: введите два целых числа")

root = tk.Tk()
root.title("Обратный вывод чисел между A и B")
root.geometry("400x300")

tk.Label(root, text="Введите целое число A:").pack(pady=(10,0))
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Введите целое число B:").pack(pady=(10,0))
entry_b = tk.Entry(root)
entry_b.pack()

btn = tk.Button(root, text="Вычислить", command=calculate)
btn.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, fg="red")
result_label.pack()

output_text = tk.Text(root, height=6, width=40)
output_text.pack(pady=10)

root.mainloop()
