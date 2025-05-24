import tkinter as tk
from tkinter import messagebox
import random

# Đọc danh sách từ
with open('list_of_words.txt', 'r') as f:
    words = [word.strip() for word in f.readlines() if word.strip()]

word = random.choice(words).lower()
guesses = set()
allow_errors = 7

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_label = tk.Label(root, text=self.display_word(), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(root, font=("Arial", 18), width=5, justify='center')
        self.guess_entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.guess_letter)
        self.guess_button.pack(pady=10)

        self.status_label = tk.Label(root, text=f"Remaining guesses: {allow_errors}", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.guessed_label = tk.Label(root, text="Guessed: ", font=("Arial", 14))
        self.guessed_label.pack(pady=10)

    def display_word(self):
        return " ".join([letter if letter in guesses else "_" for letter in word])

    def guess_letter(self):
        global allow_errors
        letter = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showinfo("Invalid", "Please enter a single alphabet letter.")
            return

        if letter in guesses:
            messagebox.showinfo("Already guessed", f"You already guessed '{letter}'")
            return

        guesses.add(letter)

        if letter not in word:
            allow_errors -= 1

        self.word_label.config(text=self.display_word())
        self.status_label.config(text=f"Remaining guesses: {allow_errors}")
        self.guessed_label.config(text=f"Guessed: {', '.join(sorted(guesses))}")

        if all(l in guesses for l in word):
            messagebox.showinfo("You win!", f"Congratulations! You guessed the word: {word}")
            self.root.quit()
        elif allow_errors == 0:
            messagebox.showinfo("Game Over", f"You lose! The word was: {word}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
