import tkinter as tk
from tkinter import ttk, messagebox


def send_email():
    messagebox.showinfo("Отправка", "Форма отправлена")


def clear_form():
    for e in [name_entry, email_entry, subject_entry, file1_entry, file2_entry, file3_entry]:
        e.delete(0, tk.END)
    message_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("Форма заявки")
root.geometry("530x460")


# заголовок
header = tk.Label(root, text="Форма заявки", font=("Arial", 14, "bold"), bg="#0CA28B", fg="white", pady=5)
header.pack(fill=tk.X)

# рамка
frame = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=8, pady=8)
frame.pack(fill=tk.BOTH, expand=True)

# информация
info = tk.Label(frame, text="Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
                            "Макс. размер каждого файла: 1024kb.\n"
                            "Макс. общий размер файла: 2048kb.",
                font=("Arial", 9, "bold"), anchor="w", justify="left")
info.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

# имя
tk.Label(frame, text="Ваше имя:").grid(row=1, column=0, sticky="w")
name_entry = tk.Entry(frame, width=35)
name_entry.grid(row=1, column=1, sticky="we")
tk.Label(frame, text="*", fg="red").grid(row=1, column=2, sticky="w")

# email
tk.Label(frame, text="Ваш Email:").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(frame, width=35)
email_entry.grid(row=2, column=1, sticky="we")
tk.Label(frame, text="*", fg="red").grid(row=2, column=2, sticky="w")

# тема
tk.Label(frame, text="Тема письма:").grid(row=3, column=0, sticky="w")
subject_entry = tk.Entry(frame, width=35)
subject_entry.grid(row=3, column=1, sticky="we")

# файл 1
tk.Label(frame, text="Прикрепить файл:").grid(row=4, column=0, sticky="w")
file1_entry = tk.Entry(frame, width=25)
file1_entry.grid(row=4, column=1, sticky="w")
ttk.Button(frame, text="Обзор...").grid(row=4, column=2, sticky="w")

# файл 2
tk.Label(frame, text="Прикрепить файл:").grid(row=5, column=0, sticky="w")
file2_entry = tk.Entry(frame, width=25)
file2_entry.grid(row=5, column=1, sticky="w")
ttk.Button(frame, text="Обзор...").grid(row=5, column=2, sticky="w")

# файл 3
tk.Label(frame, text="Прикрепить файл:").grid(row=6, column=0, sticky="w")
file3_entry = tk.Entry(frame, width=25)
file3_entry.grid(row=6, column=1, sticky="w")
ttk.Button(frame, text="Обзор...").grid(row=6, column=2, sticky="w")

# сообщение
tk.Label(frame, text="Ваше сообщение:").grid(row=7, column=0, sticky="nw", pady=8)
message_text = tk.Text(frame, width=45, height=6)
message_text.grid(row=7, column=1, columnspan=2, sticky="we", pady=8)
tk.Label(frame, text="*", fg="red").grid(row=7, column=2, sticky="ne", pady=8)

# кнопки
btn_frame = tk.Frame(root, bg="#0CA28B")
btn_frame.pack(fill=tk.X, pady=5)

send_btn = ttk.Button(btn_frame, text="Отправить Email", command=send_email)
send_btn.pack(side=tk.LEFT, padx=60, pady=6)

clear_btn = ttk.Button(btn_frame, text="Очистить", command=clear_form)
clear_btn.pack(side=tk.RIGHT, padx=60, pady=6)

root.mainloop()
