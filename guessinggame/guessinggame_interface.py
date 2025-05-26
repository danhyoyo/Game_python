import tkinter as tk
from tkinter import messagebox
import random

# Khởi tạo số cần đoán và khoảng đoán
number = random.randint(0, 100)
bot, top = 0, 100

# Hàm xử lý khi nhấn nút "Guess"
def check_guess():
    global bot, top, number
    try:
        your_guess = int(entry.get())
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid number!")
        return

    if your_guess < bot or your_guess > top:
        result_label.config(text=f"⚠️ Number must be in range ({bot}; {top})")
        return

    if your_guess > number:
        top = your_guess
        result_label.config(text=f"🔻 Too high! Range: ({bot}; {top})")
    elif your_guess < number:
        bot = your_guess
        result_label.config(text=f"🔺 Too low! Range: ({bot}; {top})")
    else:
        messagebox.showinfo("🎉 Congratulations!", f"You guessed it! The number was {number}")
        reset_game()

    entry.delete(0, tk.END)

# Hàm đặt lại trò chơi
def reset_game():
    global number, bot, top
    number = random.randint(0, 100)
    bot, top = 0, 100
    result_label.config(text="✅ Game reset! Guess a number between 0 and 100.")

# Giao diện chính
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x250")
root.resizable(False, False)

# Tiêu đề
title_label = tk.Label(root, text="🎯 Guess the Number (0 - 100)", font=("Arial", 16))
title_label.pack(pady=10)

# Ô nhập số
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Nút đoán
guess_button = tk.Button(root, text="Guess", font=("Arial", 14), command=check_guess)
guess_button.pack(pady=5)

# Kết quả
result_label = tk.Label(root, text="Enter your guess above.", font=("Arial", 12))
result_label.pack(pady=10)

# Nút reset
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.pack()

# Bắt đầu vòng lặp giao diện
root.mainloop()
