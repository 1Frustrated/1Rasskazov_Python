import tkinter as tk
from tkinter import filedialog, messagebox

class ApplicationForm(tk.Tk):
    def setup_ui(self):
        self.title("Форма заявки")
        self.configure(bg="white")
        self.geometry("520x480")
        self.resizable(False, False)
        self.files = ["", "", ""]

        # Верхняя рамка с заголовком
        tk.Label(self, text="Форма заявки", bg="#009878", fg="white",
                 font=("Arial", 14, "bold"), height=2).pack(fill="x")

        main_frame = tk.Frame(self, bd=2, relief="groove", bg="white")
        main_frame.place(x=10, y=50, width=500, height=380)

        info_text = (
            "Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
            "Макс. размер каждого файла: 1024kb.\n"
            "Макс. общий размер файла: 2048kb."
        )
        tk.Label(main_frame, text=info_text, anchor="w", justify="left",
                 bg="white", font=("Arial", 9, "bold")).place(x=10, y=5)

        tk.Label(main_frame, text="Ваше имя:", bg="white", anchor="w").place(x=10, y=55)
        self.name_entry = tk.Entry(main_frame, width=36)
        self.name_entry.place(x=110, y=55)
        tk.Label(main_frame, text="*", fg="red", bg="white").place(x=390, y=55)

        tk.Label(main_frame, text="Ваш Email:", bg="white", anchor="w").place(x=10, y=80)
        self.email_entry = tk.Entry(main_frame, width=36)
        self.email_entry.place(x=110, y=80)
        tk.Label(main_frame, text="*", fg="red", bg="white").place(x=390, y=80)

        tk.Label(main_frame, text="Тема письма:", bg="white", anchor="w").place(x=10, y=105)
        self.subject_entry = tk.Entry(main_frame, width=36)
        self.subject_entry.place(x=110, y=105)

        self.file_labels = []
        for i in range(3):
            tk.Label(main_frame, text=f"Прикрепить файл:", bg="white", anchor="w").place(x=10, y=135+25*i)
            file_label = tk.Label(main_frame, text="", bg="white", anchor="w", width=25, relief="sunken", bd=1)
            file_label.place(x=110, y=135+25*i)
            self.file_labels.append(file_label)
            tk.Button(main_frame, text="Обзор...", width=10,
                      command=lambda idx=i: self.browse_file(idx)).place(x=340, y=135+25*i)

        tk.Label(main_frame, text="Ваше сообщение:", bg="white", anchor="nw").place(x=10, y=210)
        tk.Label(main_frame, text="*", fg="red", bg="white").place(x=390, y=210)
        self.message_text = tk.Text(main_frame, width=56, height=7, wrap="word")
        self.message_text.place(x=10, y=230)

        tk.Button(main_frame, text="Отправить Email", width=18, bg="#e6f6f1",
                  command=self.send_email).place(x=80, y=340)
        tk.Button(main_frame, text="Очистить", width=18, bg="#e6f6f1",
                  command=self.clear_form).place(x=260, y=340)

    def browse_file(self, idx):
        filename = filedialog.askopenfilename(
            filetypes=[("Все файлы", "*.*"), ("Документы", "*.zip;*.rar;*.txt;*.doc;*.jpg;*.png;*.gif;*.odt;*.xml")])
        if filename:
            self.files[idx] = filename
            self.file_labels[idx].config(text=filename.split("/")[-1])

    def send_email(self):
        if not self.name_entry.get().strip():
            messagebox.showwarning("Ошибка", "Пожалуйста, введите имя.")
            return
        if not self.email_entry.get().strip():
            messagebox.showwarning("Ошибка", "Пожалуйста, введите Email.")
            return
        if not self.message_text.get("1.0", "end").strip():
            messagebox.showwarning("Ошибка", "Пожалуйста, введите сообщение.")
            return
        messagebox.showinfo("Успех", "Заявка отправлена (симуляция).")

    def clear_form(self):
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.subject_entry.delete(0, "end")
        for i in range(3):
            self.files[i] = ""
            self.file_labels[i].config(text="")
        self.message_text.delete("1.0", "end")


if __name__ == "__main__":
    app = ApplicationForm()
    app.setup_ui()  # вызываем метод для создания интерфейса
    app.mainloop()
