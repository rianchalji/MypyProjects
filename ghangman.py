import random as rd
import tkinter as tk
from tkinter import messagebox

# Word list
words = [
    "apple", "grape", "mango", "peach", "melon", "plum", "cherry", "berry", "lemon", "olive", 
    "onion", "bread", "toast", "honey", "sugar", "beans", "tomato", "carrot", "orange", "radish", 
    "cocoa", "cream", "butter", "cookie", "bacon", "salmon", "spice", "shrimp", "yogurt", "cheese",
    "basil", "chilli", "garlic", "steak", "oyster", "pepper", "bison", "quinoa", "bagels", "dates", 
    "figs", "guava", "kiwi", "nacho", "pizza", "tacos", "pasta", "risotto", "grains", "wheat", 
    "beans", "squash", "broth", "kebab", "fries", "cakes", "candy", "chips", "donut", "wafer", 
    "fudge", "pesto", "salsa", "ramen", "prawn", "trout", "tuna", "duck", "corn", "cilantro", 
    "thyme", "roast", "pesto", "salad", "falcon", "bagels", "scones", "tart", "juice", "water", 
    "mocha", "latte", "drink", "soup", "gravy"
]

class GhangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ghangman")
        self.root.geometry("500x400")  # Initial window size
        
        # Colors and styling
        self.bg_color = "#282c34"  # Dark background
        self.text_color = "#61dafb"  # Bright blue text
        self.correct_color = "#98c379"  # Green for correct guesses
        self.wrong_color = "#e06c75"  # Red for wrong guesses
        
        self.root.configure(bg=self.bg_color)

        # Game variables
        self.chosen_word = rd.choice(words)
        self.letters_in_word = set(self.chosen_word)
        self.guessed_letters = set()
        self.attempts = 6

        # Create UI elements
        self.label = tk.Label(root, text="Welcome to Ghangman!", font=('Arial', 20, 'bold'), 
                              fg=self.text_color, bg=self.bg_color)
        self.label.pack(pady=20)

        self.word_display = tk.Label(root, text=self.display_word(), font=('Arial', 24), 
                                     fg=self.text_color, bg=self.bg_color)
        self.word_display.pack(pady=20)

        self.entry = tk.Entry(root, font=('Arial', 18), width=5, justify='center')
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess, font=('Arial', 14),
                                      bg="#61dafb", fg=self.bg_color, activebackground=self.text_color, 
                                      activeforeground=self.bg_color, width=10)
        self.guess_button.pack(pady=20)

        self.status_label = tk.Label(root, text=f"Attempts remaining: {self.attempts}", font=('Arial', 14),
                                     fg=self.text_color, bg=self.bg_color)
        self.status_label.pack(pady=10)

    def display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.chosen_word])

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)  # Clear the input field

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Already guessed", "You already guessed that letter!")
            return

        self.guessed_letters.add(guess)

        if guess in self.letters_in_word:
            self.status_label.config(text="Correct guess!", fg=self.correct_color)
        else:
            self.attempts -= 1
            self.status_label.config(text=f"Wrong guess! Attempts remaining: {self.attempts}", fg=self.wrong_color)

        self.word_display.config(text=self.display_word())

        if self.letters_in_word == self.guessed_letters:
            messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.chosen_word}")
            self.reset_game()
        elif self.attempts == 0:
            messagebox.showinfo("Game Over", f"The word was: {self.chosen_word}")
            self.reset_game()

    def reset_game(self):
        self.chosen_word = rd.choice(words)
        self.letters_in_word = set(self.chosen_word)
        self.guessed_letters.clear()
        self.attempts = 6
        self.word_display.config(text=self.display_word())
        self.status_label.config(text=f"Attempts remaining: {self.attempts}", fg=self.text_color)

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    game = GhangmanGame(root)
    root.mainloop()
