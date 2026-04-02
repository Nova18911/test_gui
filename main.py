# main.py - tkinter версия (не требует pygame)
import tkinter as tk
from tkinter import ttk
import random


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI App")
        self.root.geometry("400x300")
        self.root.configure(bg='#2c3e50')

        self.counter = 0

        # Заголовок
        label = tk.Label(
            root,
            text="Simple GUI Application",
            font=("Arial", 16, "bold"),
            bg='#2c3e50',
            fg='white'
        )
        label.pack(pady=20)

        # Счетчик
        self.counter_label = tk.Label(
            root,
            text="0",
            font=("Arial", 48, "bold"),
            bg='#2c3e50',
            fg='#e74c3c'
        )
        self.counter_label.pack(pady=20)

        # Кнопка
        button = tk.Button(
            root,
            text="Click Me!",
            font=("Arial", 14),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            command=self.increment
        )
        button.pack(pady=10)

        # Кнопка выхода
        exit_button = tk.Button(
            root,
            text="Exit",
            font=("Arial", 12),
            bg='#e74c3c',
            fg='white',
            command=root.quit
        )
        exit_button.pack(pady=10)

        print("GUI Application initialized")

    def increment(self):
        self.counter += 1
        self.counter_label.config(text=str(self.counter))
        print(f"Button clicked! Counter: {self.counter}")


if __name__ == "__main__":
    print("Starting GUI Application...")
    root = tk.Tk()
    app = SimpleApp(root)
    print("Application running...")
    root.mainloop()
    print("Application closed")