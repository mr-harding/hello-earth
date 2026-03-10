"""How could this code be improved? Is there any repetitive code?"""

"Test Comment"

from tkinter import *
from tkinter import messagebox
import random

class GameOfRiskGUI:
    def __init__(self, parent):
        # Set up initial variables to track game state
        self.p1_score = 0
        self.p2_score = 0
        self.turn_score = 0
        self.current_player = 1  # Player 1 starts
        
        # Total Scores
        self.lbl_p1 = Label(parent, text="Player 1: 0", font=("Arial", 14))
        self.lbl_p1.grid(row=0, column=0, padx=20, pady=10)

        self.lbl_p2 = Label(parent, text="Player 2: 0", font=("Arial", 14))
        self.lbl_p2.grid(row=0, column=1, padx=20, pady=10)

        # Turn Indicator
        self.lbl_turn = Label(parent, text="Player 1's Turn", font=("Arial", 14, "bold"), fg="blue")
        self.lbl_turn.grid(row=1, column=0, columnspan=2, pady=10)

        # Dice Roll Result
        self.lbl_dice = Label(parent, text="Rolled: -", font=("Arial", 12))
        self.lbl_dice.grid(row=2, column=0, columnspan=2)

        # Current Banked Points
        self.lbl_bank = Label(parent, text="Banked Points: 0", font=("Arial", 12))
        self.lbl_bank.grid(row=3, column=0, columnspan=2, pady=10)

        # Action Buttons
        self.btn_roll = Button(parent, text="Roll Dice", command=self.roll_dice, width=12, bg="lightgreen")
        self.btn_roll.grid(row=4, column=0, pady=15)

        self.btn_lock = Button(parent, text="Lock In", command=self.lock_in, width=12, bg="lightblue")
        self.btn_lock.grid(row=4, column=1, pady=15)
        

    def roll_dice(self):
        """Simulates dice roll and updates banked points."""
        roll = random.randint(1, 6)
        self.lbl_dice.config(text=f"Rolled: {roll}")

        if roll == 1 or roll == 6:
            messagebox.showwarning("Bust!", f"You rolled a {roll}. You lose your banked points!")
            self.switch_turn()
        else:
            self.turn_score += roll
            self.lbl_bank.config(text=f"Banked Points: {self.turn_score}")

    def lock_in(self):
        """Adds banked points to the current player's total and checks for a win."""
        if self.turn_score > 0: # Only lock in if there are points to add
            if self.current_player == 1:
                self.p1_score += self.turn_score
                self.lbl_p1.config(text=f"Player 1: {self.p1_score}")
            else:
                self.p2_score += self.turn_score
                self.lbl_p2.config(text=f"Player 2: {self.p2_score}")

            self.check_win()

    def switch_turn(self):
        """Resets the banked points and passes play to the other player."""
        self.turn_score = 0
        self.lbl_bank.config(text="Banked Points: 0")

        if self.current_player == 1:
            self.current_player = 2
            self.lbl_turn.config(text="Player 2's Turn", fg="red")
        else:
            self.current_player = 1
            self.lbl_turn.config(text="Player 1's Turn", fg="blue")

    def check_win(self):
        """Checks if a player has reached the winning threshold of 20 points."""
        if self.p1_score >= 20:
            messagebox.showinfo("Game Over", "Player 1 Wins!")
            self.reset_game()
        elif self.p2_score >= 20:
            messagebox.showinfo("Game Over", "Player 2 Wins!")
            self.reset_game()
        else:
            # If no one has won yet, just switch turns
            self.switch_turn()

    def reset_game(self):
        """Resets all interface values and variables for a new game."""
        self.p1_score = 0
        self.p2_score = 0
        self.turn_score = 0
        self.current_player = 1

        self.lbl_p1.config(text="Player 1: 0")
        self.lbl_p2.config(text="Player 2: 0")
        self.lbl_turn.config(text="Player 1's Turn", fg="blue")
        self.lbl_dice.config(text="Rolled: -")
        self.lbl_bank.config(text="Banked Points: 0")

# --- Main Routine ---
if __name__ == "__main__":
    root = Tk()
    gui = GameOfRiskGUI(root)
    root.mainloop()