# Lexical Decision Task

A graphical word recognition task that evaluates participants' ability to determine whether presented word sets are valid English words. This is a psychology experiment task built with Python and Tkinter.

## Overview

The Lexical Decision Task is an interactive GUI-based psychological experiment where participants are presented with sets of words and must decide whether all words in each set are valid English words or not. The task includes progressive difficulty levels and optional word list shuffling.

## Features

- **Graphical User Interface (GUI)** - Built with Tkinter for easy interaction
- **Keyboard-Only Input** - Press 'y' for yes and 'n' for no to respond
- **Progressive Difficulty** - After 3 consecutive correct answers, keys change to 'z' and 'm'
- **Dictionary Shuffling** - Option to shuffle word sets after 2 rounds
- **Performance Tracking** - Tracks correct and incorrect responses
- **Dynamic Feedback** - Real-time scoring and difficulty progression alerts

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/lexical_decision_task.git
cd lexical_decision_task
```

## How to Run

```bash
python main.py
```

The GUI window will open, presenting the task interface.

## How to Play

1. **Start Screen**: Press 'y' to continue with the experiment or 'n' to quit
2. **Word Presentation**: Four words will be displayed on the screen
3. **Response**: 
   - Press **'y'** if you think all words are English words
   - Press **'n'** if you think at least one word is not an English word
4. **Difficulty Increase**: After 3 consecutive correct responses, the key requirements change:
   - Press **'z'** for yes
   - Press **'m'** for no
5. **Dictionary Shuffle**: After 2 rounds, you'll be asked if you want to shuffle the word dictionary
6. **End**: The game ends after all rounds are completed, displaying your final score

## Project Structure

```
lexical_decision_task/
├── main.py              # Main GUI application and task controller
├── participant.py       # Participant class for tracking responses
├── filereader.py        # File I/O for reading word lists
├── words.txt            # Word data file with English and non-English words
└── README.md            # This file
```

## File Descriptions

- **main.py** - Contains the `LexicalDecisionGUI` class that manages the task interface and game flow
- **participant.py** - Defines the `TrialParticipant` class that tracks participant data, responses, and scores
- **filereader.py** - Defines `FileReader` and `WordFileReader` classes for reading and processing word data
- **words.txt** - CSV format file containing word sets (English and non-English variants)

## Word Data Format

The `words.txt` file uses CSV format with the following structure:
```
round,type,word1,word2,word3,word4
1,correct,girl,panda,tree,dog
1,incorrect,gyrl,panda,trop,dog
```

Where:
- **round** - Round number
- **type** - Either "correct" (all English words) or "incorrect" (contains non-English words)
- **words** - The set of words to display

## License

This project is open source and available under the MIT License.
