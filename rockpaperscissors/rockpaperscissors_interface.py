import tkinter as tk
import random

# Danh sách lựa chọn
options = ["paper", "rock", "scissors"]

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

# Hàm xử lý lựa chọn của người chơi
def play(player_choose):
    bot_choose = random.randint(0, 2)
    player_option_index = options.index(player_choose)

    if (player_option_index == bot_choose + 1) or (player_option_index == 0 and bot_choose == 2):
        result = "You lose"
    elif (player_option_index == bot_choose - 1) or (player_option_index == 2 and bot_choose == 0):
        result = "You win"
    else:
        result = "Tie"

    result_label.config(
        text=f"You chose {player_choose.upper()} | Bot chose {options[bot_choose].upper()}\n➡️ {result}",
        fg="blue"
    )

# Hàm thoát game
def quit_game():
    root.destroy()

# Tiêu đề
title = tk.Label(root, text="🎮 Rock Paper Scissors", font=("Arial", 18))
title.pack(pady=20)

# Nút chọn lựa
button_frame = tk.Frame(root)
button_frame.pack()

for option in options:
    btn = tk.Button(button_frame, text=option.capitalize(), font=("Arial", 14), width=10,
                    command=lambda opt=option: play(opt))
    btn.pack(side=tk.LEFT, padx=10)

# Kết quả
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
result_label.pack(pady=30)

# Nút thoát
quit_btn = tk.Button(root, text="Quit", font=("Arial", 12), command=quit_game)
quit_btn.pack()

# Vòng lặp giao diện
root.mainloop()
