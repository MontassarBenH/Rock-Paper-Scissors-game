import random
import tkinter as tk

# Create the GUI
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Define the game function
def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = user_input.get().lower()

    user_choice_label.config(text=f"You chose {user_choice.capitalize()}.")
    computer_choice_label.config(text=f"The computer chose {computer_choice.capitalize()}.")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_label.config(text="You win!")
    else:
        result_label.config(text="The computer wins!")

    # Clear the user input field
    user_input.delete(0, tk.END)

# Create the GUI elements
instructions_label = tk.Label(root, text="Enter 'rock', 'paper', or 'scissors':")
instructions_label.pack()

user_input = tk.Entry(root, width=30)
user_input.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

user_choice_label = tk.Label(root, text="")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI
root.mainloop()
