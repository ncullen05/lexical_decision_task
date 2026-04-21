from participant import TrialParticipant
from filereader import WordFileReader
import tkinter as tk
from tkinter import messagebox

# An instance of WordFileReader is instantiated
file_1 = WordFileReader("words.txt")
words_dict = file_1.all_rounds()
shuffle_dict = file_1.shuffle_rounds()

# An instance of TrialParticipant is instantiated
trial_participant = TrialParticipant("John", "Doe")
trial_participant.set_words(words_dict)

class LexicalDecisionGUI:
    def __init__(self, root, participant):
        self.root = root
        self.participant = participant
        self.root.title("Lexical Decision Task")
        self.root.geometry("400x300")

        # Additional variables for features
        self.consecutive_correct = 0
        self.round_counter = 0
        self.dictionary_shuffled = False
        self.difficulty_switch = False
        self.waiting_for_response = False

        # Bind key presses
        self.root.bind('<Key>', self.key_press)

        # Welcome message
        self.label = tk.Label(root, text=f"Welcome to the Lexical Decision Task, {participant.firstname} {participant.lastname}!\n"
                                         "In this task, you will be presented with four words.\n"
                                         "Your task is to select whether all four words are of the English language!",
                              wraplength=350)
        self.label.pack(pady=10)

        # Consent
        self.consent_label = tk.Label(root, text="Do you wish to continue with the experiment? (y/n)")
        self.consent_label.pack()

        self.game_started = False

    def key_press(self, event):
        key = event.char.lower()
        if not self.game_started:
            if key == 'y':
                self.start_game()
            elif key == 'n':
                self.quit_game()
        else:
            if self.waiting_for_response:
                if not self.difficulty_switch:
                    if key == 'y':
                        self.respond('y')
                    elif key == 'n':
                        self.respond('n')
                else:
                    if key == 'z':
                        self.respond('z')
                    elif key == 'm':
                        self.respond('m')

    def start_game(self):
        self.game_started = True
        self.consent_label.destroy()
        self.label.config(text="The word position is now at: " + str(self.participant.get_position()))
        self.show_words()

    def quit_game(self):
        self.root.quit()

    def show_words(self):
        if not self.game_started:
            return
        words = self.participant.select_words()
        self.words_label = tk.Label(self.root, text="Words: " + ", ".join(words), font=("Arial", 14))
        self.words_label.pack(pady=10)

        instruction = "Press 'y' for Yes, 'n' for No" if not self.difficulty_switch else "Press 'z' for Yes, 'm' for No"
        self.question_label = tk.Label(self.root, text=f"Are all these words English?\n{instruction}")
        self.question_label.pack()
        
        self.waiting_for_response = True

    def respond(self, response):
        self.waiting_for_response = False
        self.participant.response(response)
        self.participant.increment_choice(self.participant.answer)
        
        if self.participant.answer:
            self.consecutive_correct += 1
        else:
            self.consecutive_correct = 0
        
        if self.consecutive_correct == 3 and not self.difficulty_switch:
            self.difficulty_switch = True
            messagebox.showinfo("Difficulty Increased", "You're doing great! Increasing difficulty...\nFrom now on select 'z' for Yes and 'm' for No")
            self.participant.change_response_keys()
            # Buttons will be updated in show_words
        
        next_round = self.participant.increment_position()
        self.words_label.destroy()
        self.question_label.destroy()
        if next_round:
            self.round_counter += 1
            if self.round_counter == 2 and not self.dictionary_shuffled:
                shuffle = messagebox.askyesno("Shuffle Dictionary", "Two rounds have passed. Do you want to shuffle the dictionary?")
                if shuffle:
                    shuffle_dict = file_1.shuffle_rounds()
                    self.participant.set_words(shuffle_dict)
                    messagebox.showinfo("Shuffled", "Dictionary has been shuffled!")
                else:
                    messagebox.showinfo("No Shuffle", "Dictionary remains the same.")
                self.dictionary_shuffled = True
            self.label.config(text="The word position is now at: " + str(self.participant.get_position()))
            self.show_words()
        else:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Correct: {self.participant.get_correct()}\nIncorrect: {self.participant.get_incorrect()}")
        self.root.quit()

# Run the GUI
root = tk.Tk()
gui = LexicalDecisionGUI(root, trial_participant)
root.mainloop()