from participant import TrialParticipant
from filereader import WordFileReader

#An instance of WordFileReader is instantiated
file_1 = WordFileReader("words.txt")
words_dict = file_1.all_rounds()
shuffle_dict = file_1.shuffle_rounds()

#An instance of TrialParticipant is instantiated
trial_participant = TrialParticipant("John", "Doe") 
trial_participant.set_words(words_dict)

#Welcome message is printed to the user
print("\n")
print("Welcome, to the Lexical Decision Task, %s %s!" % (trial_participant.firstname, trial_participant.lastname))
print("In this task, you will be presented with four words.")
print("Your task is to select whether all four words are of the English language!")
consent = input("Do you wish to continue with the experiment? Select 'y' for yes and 'n' for no. ")
while consent.lower() not in ["y", "n"]: #Validates the users input
    consent = input("Please select a valid response: ")

if consent.lower() == "n":
    run_game = False
elif consent.lower() == "y":
    run_game = True

print("---")
print("\n")

run_game = True #Initialises a flag to keep the game running
consecutive_correct = 0
difficulty_switch = False
round_counter = 0  #Counter to track the number of rounds
dictionary_shuffled = False  #Tracks if the dictionary has been shuffled   

while run_game: #Game loop commences

    print("The word position is now at: %s" % trial_participant.get_position()) #Displays the current word position to the user
    trial_participant.select_words() #Selects and displays the words for the current position
    participant_selection = input("Select 'y' or 'n' to move to the next position ") #Prompts the participant to make a selection either 'y' or 'n'
    
    if participant_selection.lower() not in ["y", "n"]: #Validates the users input
        print("\n"*2) #Spacing
        print("Please select a valid response...") #Asks for another input if the input is invalid
    else:
        trial_participant.response(participant_selection) #Records the participant's response
        trial_participant.increment_choice(trial_participant.answer) #Increments correct/incorrect choice based on the response
        next = trial_participant.increment_position() #Attempts to increment the position
        print("\n"*2) #Spacing

        #Increment round counter
        round_counter += 1

        #After two rounds, ask the user if they want to shuffle the dictionary
        if round_counter == 2 and not dictionary_shuffled:
            choose_dict = input("Two rounds have passed. Select 'y' to shuffle the dictionary or 'n' to keep it the same: ")
            while choose_dict.lower() not in ["y", "n"]:  #Validates the users input
                choose_dict = input("Please select a valid response: ")

            if choose_dict.lower() == "y":
                shuffle_dict = file_1.shuffle_rounds()
                trial_participant.set_words(shuffle_dict)
                print("Dictionary has been shuffled!")
            else:
                print("Dictionary remains the same.")
            
            dictionary_shuffled = True  
       
        if next == False: #Checks if there is more rounds left
            run_game = False #Ends the game if theres no rounds left
            print("\n"*2) #Spacing
            print("You got %s correct and you got %s wrong" % (trial_participant.get_correct(), trial_participant.get_incorrect())) #Prints final score
            print(trial_participant) #Prints the participant's details 
            print("There are no more selections available. The experiment has ended.") #End message
        else:
            pass

        if trial_participant.answer == True:  
            consecutive_correct += 1  #Increment consecutive correct counter
        else:
            consecutive_correct = 0  #Reset counter if incorrect
        
        if consecutive_correct == 3 and not difficulty_switch:
            print("You're doing great! Increasing difficulty...")
            print("From now on select 'z' for Yes and 'm' for No\n")
        else:
            pass

        #Check if it's time to change the responses required
        while consecutive_correct == 3 and not difficulty_switch:
            print("The word position is now at: %s" % trial_participant.get_position()) #Displays the current word position to the user
            trial_participant.select_words() #Selects and displays the words for the current position
            participant_selection = input("Select 'z' for Yes and 'm' for No... ") #Prompts the participant to make a selection either 'y' or 'n'
            trial_participant.change_response_keys()
            if participant_selection.lower() not in ["z", "m"]: #Validates the users input
                print("\n"*2) #Spacing
                print("Please select a valid response...") #Asks for another input if the input is invalid
            else:
                trial_participant.response(participant_selection) #Records the participant's response
                trial_participant.increment_choice(trial_participant.answer) #Increments correct/incorrect choice based on the response
                next = trial_participant.increment_position() #Attempts to increment the position
                print("\n"*2) #Spacing
            
            if next == False: #Checks if there is more rounds left
                difficulty_switch = True
                run_game = False #Ends the game if theres no rounds left
                print("\n"*2) #Spacing
                print("You got %s correct and you got %s wrong" % (trial_participant.get_correct(), trial_participant.get_incorrect())) #Prints final score
                print(trial_participant) #Prints the participant's details 
                print("There are no more selections available. The experiment has ended.") #End message
            else:
                pass