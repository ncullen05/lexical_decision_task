import random

class TrialParticipant: 
    #Class variable being incremented whenever a new instance of the class is created
    #This variable tracks the total number of participants across all instances. 
    #It needs to be shared among all instances to reflect a cumulative count.
    #This is why it is a class variable
    instances_of_participants = 0 

    #This dictionary contains the word dictionary shared among all participants. 
    #Since the word set is not specific to any individual participant and remains constant across all instances.
    #This is why it is defined as a class variable.
    words = { 
        1: {'english': ['girl', 'panda', 'tree', 'dog'], 'non-english': ['gyrl', 'panda', 'trop', 'dog']},     
        2: {'english': ['tram', 'farm', 'help', 'shop'], 'non-english': ['terg', 'farm', 'hilp', 'shyp']}, 
        3: {'english': ['jump', 'rain', 'worm', 'dark'], 'non-english': ['jump', 'roim', 'warm', 'durh']}, 
        4: {'english': ['pull', 'draw', 'fork', 'kick'], 'non-english': ['pull', 'yruw', 'fjrc', 'kick']},  
        5: {'english': ['harsh', 'storm', 'spoon', 'light'], 'non-english': ['hyrth', 'storm', 'spuun', 'light']}, 
        6: {'english': ['green', 'viola', 'flour', 'drain'], 'non-english': ['green', 'vaeph', 'flour', 'dyyyn']}
    }

    #Class variables (instances_of_participants, words) are for shared, static data across instances.

    def __init__(self, firstname, lastname):
        #The first two variables are personal attributes unique to each participant.
        #This is why they are defined as instance variables
        self._first_name = firstname #Stores participant's first name
        self._last_name = lastname #Stores participant's last name

        #These two lines increment the number of participant instances and assign the participant a number
        #As the number is unique to the person it is defined as an instance variable
        TrialParticipant.instances_of_participants += 1 
        self.participant_num = TrialParticipant.instances_of_participants 

        #These variables represent the participant’s current progress and performance, unique to each instance
        self.position = 1 #Current word position
        self.correct_choices = 0 #No. of correct selections
        self.incorrect_choices = 0 #No. of incorrect selections
        self.random_word = 0 #Randomly selected word type
        self.total_rounds = len(self.words) 

        #These variables store user-specific interactions and are not shared across participants
        self.possible_selections = {"english": "y", "non-english": "n"} #Dictionary holding word types and responses
        self.word_type = ["english", "non-english"] #Types of words to choose from
        self.answer = None #Stores the participant's responses

    #Instance variables are for tracking the unique state of each participant

    #Methods below demonstrate encapsulation (private data like `_first_name`) and controlled access through getters/setters.
    
    def get_firstname(self): #Encapsulation: Provides controlled access to `_first_name`
        return self._first_name 

    def set_firstname(self, new_firstname): #Encapsulation: Updates `_first_name` in a controlled manner
        self._first_name = new_firstname
    
    def get_lastname(self): #Encapsulation: Provides controlled access to `_last_name`
        return self._last_name
    
    def set_lastname(self, new_lastname): #Encapsulation: Updates `_last_name` in a controlled manner
        self._last_name = new_lastname
        
    def get_correct(self): #Encapsulation: Access correct responses count
        return self.correct_choices

    def get_incorrect(self): #Encapsulation: Access incorrect responses count
        return self.incorrect_choices
    
    def increment_choice(self, is_correct): #Updates choices based on input
        #Updates either correct or incorrect choices based on a boolean argument
        if is_correct:
            self.correct_choices += 1
        else:
            self.incorrect_choices += 1

    def increment_position(self):
        self.position += 1 #Increments the current word position
        if self.position > self.total_rounds: #Checks for remaining rounds
            return False #Signals no more rounds left
        return True #Signals that there are remaining rounds

    def get_position(self): #Encapsulation: Access current position
        return self.position
     
    def select_words(self): #Selects a random word list
        self.random_word = random.randint(0,1) #Assigns a 0 or 1 randomly to an instance variable
        words_at_type = self.words[self.position][self.word_type[self.random_word]] #Selects the words at the position 0 or 1
        print(words_at_type) #Displays selected words

    def response(self, selection): #Checks if the response matches the current word type
        key_association = self.possible_selections[self.word_type[self.random_word]] #The expected/correct response
        print("The participant selected: %s" % selection)
        print("the current word type is: %s" % self.word_type[self.random_word])
        print("The correct response for this was: %s" % key_association)
        if key_association == selection: #Compares if the expected response is the same as the actual response
            self.answer = True #Is true when the response is correct
        else:
            self.answer = False #Is false when the response is incorrect

    def reset(self): #Resets the current word position to 1
        self.position = 1
    
    def set_words(self, new_words): #Sets a new selection of words for the participant ensuring their format is valid
        if isinstance(new_words, dict): #Checks if the new words are in a dicitonary
            for key in new_words.keys():
                if isinstance(key, int) and isinstance(new_words[key], dict): #Validates that the keys are integers and the values are dictionaries
                    for nested_key in new_words[key].keys():
                        if isinstance(nested_key, str) and isinstance(new_words[key][nested_key], list) and len(new_words[key][nested_key]) >= 2: #Validate nested dictionary keys and values
                            print("This is a valid dictionary")  #Indicates valid format
                            self.words = new_words #Sets new words
                            self.total_rounds = len(new_words)
                            return True
                        else:
                            print("This is not a valid dictionary") #Invalid format
                            return False          
                else:
                    print("This is not a valid dictionary") #Invalid format
                    return False
        else:
            print("This is not a valid dictionary") #Invalid format
            return False
        
    def change_response_keys(self):  #Updates the key mappings for user responses
        responses = self.possible_selections
        responses["english"] = "z"  #Updates "english" response key
        responses["non-english"] = "m"  #Updates "non-english" response key
        return responses

    def __str__(self): #String representation of the participants details
        return ("Participant: %s %s\n"
                "Participant Number: %d\n"
                "Correct Selections: %d\n"
                "Incorrect Selections: %d" % 
                (self._first_name, self._last_name, self.participant_num, 
                self.correct_choices, self.incorrect_choices))
        
    #Properties for accessing first and last names    
    firstname = property(get_firstname, set_firstname)
    lastname = property(get_lastname, set_lastname)

