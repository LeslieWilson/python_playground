# Final Python Project

# For my final python project, I made a flashcard app that quizzes you on stored flashcards or allows you to create new flashcards, and uses regex to approximate how well you answered. The command prompt interface will ask a user if they want to make a new flashcard or go through saved flashcards

# If the user makes a new flash card - it asks for the question - saves it to a text file - then it asks for the answer and saves it to the same text file, with a comma or a new line after the question.

# If the user asks to go through the flashcards, the program will prompt with a question and the user will type in as close an answer as they can. if the answers match closely enough (using regex) it will show you the answer and move on to the next card. If the users answer does not match the real answer closely enough, it tells you to try again or offers to show you the answer.
#
# So somewhere in the object there will be a method that reads the first line of the text file for the question, then read the next line for the answer and keep looping through the file. This will show the question and answer successively.
