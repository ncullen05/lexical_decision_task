import random

class FileReader: #Parent Class

    def __init__(self, filename):
        self.__filename = None
        self.set_filename(filename)
        print("Instance of FileReader class created!")
    
    #Method to read all contents of the file
    def read_all(self):
        try:
            file_1 = open(self.__filename)
            lines = file_1.readlines()
            file_1.close()
            return lines
        except:
            print("File not opened. Terminating method")
            return False

    #Method to count the number of lines in the file
    def line_count(self):
        lines = self.read_all()
        line_amount = len(lines)
        return line_amount   

    #Getter method to access the private filename attribute
    def get_filename(self):
        return self.__filename
    
    #Setter method to validate and set the filename
    def set_filename(self, new_filename):
        if type(new_filename) == str:
            self.__filename = new_filename  

#Child Class: WordFileReader (inherits from FileReader)
class WordFileReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)  #Call the parent class's __init__ method to initialize filename
        #Optionally call other parent methods here if needed
        self.display_filename() #Example of explicitly calling a parent method

        self.w = {} #Dictionary to hold all rounds and corresponding words
        self.intkeys = [] #List to hold all the keys in the correct form as integers
        self.wordtype = ["english", "non-english"]  #Word categories
        self.english = []  #List to hold English words
        self.nonenglish = []  #List to hold Non-English words
        self.newkeys = []  #List to store changed keys

    def display_filename(self):
        print("The filename is: %s" % self.get_filename()) #Displays the filename to the output
        
    def all_rounds(self):
        #The "read_all" method is inherited from the parent class "FileReader". 
        #This demonstrates the principle of inheritance, where the child class reuses and extends functionality from the parent class.
        contents = self.read_all()
        identify_round = [] #Temporary list to hold round numbers
        wordlist = [] #Temporary list to hold all words in the file
        strkeys = [] #Temporary list to hold the keys, as strings
        num = 0

        #Process each line in contents
        for item in contents:
            item = item.strip() #Removes extra whitespaces and specified characters
            lists = item.split(',') #Seperates the contents into lists seperated at the comma
            integers = lists[0].split(',') #Seperates the lists at the first index to retrieve all the integers (rounds)
            identify_round.append(integers[0]) #Appends the round identifiers
            words = lists[2:len(lists)] 
            wordlist.append(words) #Append only the relevant words        
        
        #Appends only one instance of each integer contained in identify_round
        for i in range(0, len(identify_round), 2): 
            strkeys.append(identify_round[i])  
            self.intkeys = [int(x) for x in strkeys]          
        
        #Appends just english words to a list
        for evennumber in range(0, len(wordlist), 2):
            self.english.append(wordlist[evennumber])
        
        #Appends just non-english words to a list
        for oddnumber in range(1, len(wordlist), 2):
            self.nonenglish.append(wordlist[oddnumber])
        
        #Puts all the information into a nested dictionary
        for num in range(0, len(self.intkeys)):
            self.w[self.intkeys[num]] = {self.wordtype[0] : None, self.wordtype[1] : None}
            self.w[self.intkeys[num]][self.wordtype[0]] = self.english[num]
            self.w[self.intkeys[num]][self.wordtype[1]] = self.nonenglish[num]
        
        #Returns the dictionary by rounds
        return self.w
    
    #Helper method to get the total number of rounds
    def get_rounds_length(self):
        length = len(self.intkeys)
        return length 
    
    #Retrieves specific rounds based on a list of round numbers
    def get_rounds_at(self, round_num_list):
        key_counter = 1 #Initializes counter for keys
        counter = 0 #Initializes counter for indexing
        length = len(round_num_list) 
        newdict = {} #New dictionary for output
        new_rounds = [] #List to hold new round numbers
        numvalue = []  #List of numbers to access 'self.w'
        
        #Append 'new_rounds' with consecutive numbers starting at 1
        while key_counter <= length:
            new_rounds.append(key_counter)
            key_counter = key_counter + 1
        
        #Initialize 'newdict' with empty dictionaries for each key in 'new_rounds'  
        for key_counter in range(0, length):
            newdict[new_rounds[key_counter]] = {}
         
        #Assigns data from 'self.w' to 'newdict'
        for counter in range(0, length):
            listvalues = round_num_list[counter]
            listvalues1 = listvalues - 1 #Converts number to a zero-based index
            numvalue.append(listvalues1)
            data = self.w[self.intkeys[numvalue[counter]]]
            newdict[new_rounds[counter]] = data
        
        #Returns a new dictionary with the specified rounds
        return newdict
    
    #Retrieves rounds within a specified range
    def get_round_range(self, ran_rounds): 
        contents = self.read_all() #Read the entire file contents 
        filelength = self.line_count() #Count the total number of lines in the file
        
        #Initialize variables to store range dictionary, key counter, and lists for round numbers and words
        range_dict = {}
        keycounter = 1
        newrounds = []
        words = []

        #Calculate the total number of rounds, assuming each round takes 2 lines
        totalrounds = int(filelength / 2)

        #Read and process the file contents
        for item in contents:
            strip_item = item.strip() #Remove any surrounding whitespace
            lists = strip_item.split(',') #Split line by commas
            words.append(lists[2:len(lists)]) #Append only the relevant words

        # Validation: check ran_rounds for format and range compliance
        if len(ran_rounds) != 2:
            print("The parameter should have two items in a list.")
            return
        elif ran_rounds[0] >= ran_rounds[1]:
            print("The first value should not be higher than the second value.")
            return
        elif ran_rounds[0] <= 0 or ran_rounds[1] <= 0:
            print("Both values should be positive integers.") 
            return
        elif ran_rounds[0] > totalrounds or ran_rounds[1] > totalrounds:
            print("The range provided is outside the range of the dictionary.")
            return
        
        #Define range within wordlist
        key1, key2 = (ran_rounds[0] * 2) - 2, ran_rounds[1] * 2
        round_range = words[key1:key2]  #Extracting specified round range
        length = int(len(round_range) / 2) #Adjust length for new round range

        #Setting up new round keys from 1 to length
        while keycounter <= length:
            newrounds.append(keycounter)
            keycounter += 1

        #Populating the range_dict with adjusted keys and correct round data
        index = ran_rounds[0] - 1  #Adjust the index to match the round offset
        for num in range(0, length):
            range_dict[newrounds[num]] = {self.wordtype[0]: None, self.wordtype[1]: None}
            range_dict[newrounds[num]][self.wordtype[0]] = self.english[index]
            range_dict[newrounds[num]][self.wordtype[1]] = self.nonenglish[index]
            index += 1 #Move to the next round's words in the lists
        
        #Return the dictionary containing the specified range of rounds
        return range_dict

    def random_rounds(self):
        filelength = self.line_count() #Count the total number of lines in the file
        range_dict = {}

        # Calculate total rounds, assuming each round takes 2 lines
        total_rounds = filelength // 2
        
        # Define start and stop values within the range
        start_value = random.randint(1, total_rounds)
        stop_value = random.randint(start_value, total_rounds)

        num_rounds = (stop_value - start_value) + 1
        new_rounds = list(range(1, num_rounds + 1))

        # Start the index at the beginning of the selected range
        index = start_value - 1  # Adjust index to match round offset
        for num in range(num_rounds):
            range_dict[new_rounds[num]] = {self.wordtype[0]: None, self.wordtype[1]: None}
            range_dict[new_rounds[num]][self.wordtype[0]] = self.english[index]
            range_dict[new_rounds[num]][self.wordtype[1]] = self.nonenglish[index]
            index += 1  # Move to the next round's words in the lists

        return range_dict

    #Retrieves rounds at all the numbers not provided by the user
    def exclude_rounds_at(self, round_nums_list):
        newrounds = [] #Initialize a list to store rounds that are not in round_nums_list
        keycounter = 1 #Initialize a counter to assign keys in sequential order
        
        #Calculate the total number of rounds by dividing the file length by 2
        filelength = self.line_count()
        length = int(filelength) / 2
        
        #Populate self.newkeys with round numbers from 1 up to the total number of rounds
        while keycounter <= length:
            self.newkeys.append(keycounter)
            keycounter += 1

        #Append to newrounds any keys not found in round_nums_list (rounds to be excluded)
        for key in self.newkeys:
            if key not in round_nums_list:
                newrounds.append(key)
        
        excluded_rounds = self.get_rounds_at(newrounds) #Use get_rounds_at to retrieve the dictionary of rounds, excluding specified rounds
        
        # Return the dictionary with excluded rounds
        return excluded_rounds
    
    def exclude_round_range(self, ran_rounds):        
        filelength = self.line_count() #Count the total number of lines in the file
        totalrounds = int(filelength / 2) #Calculate the total number of rounds, assuming each round spans 2 lines
        new_go = [] #Initialize a list to store rounds that are outside the specified range
        
        # Validation: check ran_rounds for format and range compliance
        if type(ran_rounds) != list:
            print("The parameter should be a list.")
        elif len(ran_rounds) != 2:
            print("The parameter should have two items in a list.")
            return
        elif ran_rounds[0] >= ran_rounds[1]:
            print("The first value should not be higher than the second value.")
            return
        elif ran_rounds[0] <= 0 or ran_rounds[1] <= 0:
            print("Both values should be positive integers.") 
            return
        elif ran_rounds[0] > totalrounds or ran_rounds[1] > totalrounds:
            print("The range provided is outside the range of the dictionary.")
            return
        
        # Extract the range of rounds to be excluded based on ran_rounds list
        # Slice the list from ran_rounds[0] to ran_rounds[1] (both inclusive)
        excludedkeys = self.newkeys[ran_rounds[0]:ran_rounds[1]]

        # Loop through all keys in newkeys and add to new_go only if not in excludedkeys
        for key in self.newkeys:
            if key not in excludedkeys:
                new_go.append(key)

        # Use get_rounds_at to fetch all rounds outside the excluded range
        excluded_round_range = self.get_rounds_at(new_go)
        
        # Return the dictionary with the rounds that are not in the excluded range
        return excluded_round_range
    
    def shuffle_rounds(self):
        original_dict = self.all_rounds()
        newgood = []
        newbad = []
        shuffledict = {}

        for good in self.english:
            shuffled_good = good.copy() #List is copied before shuffling
            random.shuffle(shuffled_good)
            newgood.append(shuffled_good)
        for bad in self.nonenglish:
            shuffled_bad = bad.copy() #List is copied before shuffling
            random.shuffle(shuffled_bad)
            newbad.append(shuffled_bad)

        for num in range(0, len(self.intkeys)):
            shuffledict[self.intkeys[num]] = {self.wordtype[0] : None, self.wordtype[1] : None}
            shuffledict[self.intkeys[num]][self.wordtype[0]] = newgood[num]
            shuffledict[self.intkeys[num]][self.wordtype[1]] = newbad[num]

        return shuffledict
        #return new_rounds

    def __str__(self):
        # String representation of the WordFileReader object summarizing main attributes
        return ("WordFileReader for file '%s':\n"
                "Rounds loaded: %d\n"
                "Total words in English: %d\n"
                "Total words in Non-English: %d" % 
                (self.get_filename(), len(self.intkeys), len(self.english), len(self.nonenglish)))

