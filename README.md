# Collection-Game-python-Projects

 To complete this assignment, you should first write a 'recipe' that describes the components of the game and submit this file separately from the Python code. Next, you are to write a Python program that allows users to input basic demographic information (minimum of three pieces of demographic information) and then to create a collection of three items, with each item having at least two pieces of metadata attached to them. After this initial phase of the game, each user is allowed to try and guess an item from the other's collection. Each user can only have X guesses (you define X, e.g., you could allow a user guess a maximum of 10 times) before the game ends. You can alternate guessing or have one user guess all their guesses at one time. 

Output a welcome message describing the application for the user and any/all instructions
At each step, give them the option to quit the game (i.e. In instructions, inform the players they may quit at any time by typing "Q" or something similar)
If a player quits, thank them for playing in a professional manner
Output score (if they've started guessing)
Ask the first player to input their demographic information (min of 3 pieces of info and you must include first name as one of the pieces of demographic information) and store the data
Validate data where applicable; e.g., if you ask for age, verify that they've given you an integer and not a string
Output blank lines (as you did in the previous assignment) and then ask for the second player's information.
Once demographic information is stored for both players, first ask the second player to hide their eyes and then ask the first player to input information for each item (minimum of three) in their collection. 
Ask them by their first name (from the data you gathered in step #2)
This should include the item itself and the two pieces of metadata about the item (e.g. item=book; title=Neuromancer; author=William Gibson; year=1984)
Remember that the other player will try to guess the item, so please choose to store different items in your collection -- or, for example, if you have three books in your collection, you need to allow the other player to search by title or some other piece of metadata! Otherwise, they can easily guess correctly by just entering 'book'.
Repeat #4 for second player (don't forget to ask player one to hide their eyes). 
Once demographic information and the items are all entered, output blank lines to hide previous input from the screen
Allow each player to guess the items in the other player's collection
Keep score by adding one point for each correct guess to a counter for each player
Keep a count of total guesses by adding one to a counter for each guess a player makes
Finish the round after X guesses or when a player guesses all the items in the other's collection
Present the option of playing again to the players at the end of the round
