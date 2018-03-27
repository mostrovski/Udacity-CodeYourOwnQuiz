'''
Code a fill-in-the-blanks quiz. Task: the quiz should prompt a user with a 
sentence containing several blanks. The user should then be asked to fill in 
each blank appropriately to complete the sentence. When player guesses 
correctly, new prompt shows with correct answer in the previous blank and a new 
prompt for the next blank. When player guesses incorrectly, they are prompted to
try again. Game has 3 or more levels and each level contains 4 or more blanks to
fill in.

My code starts with four imports. The first (sys) is a result of my intention 
to stop the execution of the code when a user runs out of attempts giving no 
correct answer. Examining the sample provided by Udacity, I noticed that it 
closes the window in such a situation. I wanted to avoid it somehow, and thus 
googled a bit and found this (import sys + sys.exit) solution that worked just 
how I wanted in Git Bash. The second import (textwrap) was added at the very end
of the project when I decided to do something with ugly looking output 
paragraphs. Just like with (sys), I googled and found this (import textwrap + 
textwrap.fill) solution. 'quiz_data' imports my file with lots of important 
variables defined. Finally, I decided to import (randint) to diversify some 
prompts. 
'''
import sys
import textwrap
import quiz_data
from random import randint 

# Here comes the block of initial variables. 

'''
A user can choose from three levels (level_options = ['easy', 'medium', 'hard'])
and from 1 to 5 attempts per problem (min_attempts = 1; max_attempts = 5). 
'''  
level_options = ['easy', 'medium', 'hard']

min_attempts = 1

max_attempts = 5 

output_line_len = 75 
'''
Sets the lenght of the output line; used by textwrap.fill in 'quiz_game' 
function below.
'''

# Here comes the block of functions.

def input_check(s,options):
	'''
	Takes two arguments as input: the string 's' and the list 'options'. Returns
	True if the string is in the list. Otherwise, returns False. It is used to  
	analyze the user's input during the game.   
	'''
	return s in options

def level_chosen(level_input, level_options):
	'''
	Takes the string 'level_input' and compares it to the elements of the list 
	'level_options'. Returns the element from 'level_options' if the input 
	equals to the element of that list or the first character of that element. 
	Otherwise, returns None. It is used only to control the input of the user 
	related to the choice of the level and help set this level for the game. 
	I decided to give the user an option to choose the level by typing only the 
	first character of the level's name. Since the input_check function isn't 
	helpful in this particular case, I defined this one.      
	'''
	result = None
	for i in level_options:
		if level_input == i or level_input == i[0]:
			result = i
	return result 

def random_correct():
	'''
	Takes no input. Uses the randint function (must return either 0 or 1 or 2) 
	to return one of three possible strings randomly. It is used to diversify 
	motivational notifications after correct answers.
	'''  
	random_num = randint(0,2)
	if random_num == 0:
		return 'Yes, you are right!'
	elif random_num == 1:
		return 'That is correct!'
	else:
		return 'Exactly! You are great!'

def random_wrong():
	'''
	Takes no input. Uses the randint function (must return either 0 or 1 or 2) 
	to return one of three possible strings randomly. It is used to diversify 
	motivational notifications after wrong answers.
	'''
	random_num = randint(0,2)
	if random_num == 0:
		return 'Nope, try again!'
	elif random_num == 1:
		return 'It was wrong! Try something else!'
	else:
		return 'Wrong! Come on, I believe you know this!'

def quiz_problem(problem,correct_answer):
	'''
	The heart of the code! 
	This function manages every separate problem of the quiz. Takes two 
	arguments as input: the string 'problem' and the list 'correct_answer'. 
	Checks if the user gave the correct answer using no more attempts than it 
	was allowed. In this case, it returns the correct answer of the user 
	('user_input'). Otherwise, it stops the execution of the code ('sys.exit'). 
	Here is how:
	'''
	user_input = raw_input(problem)
	''' 
	1) sets the problem and saves the answer (input of the user) in the 
	user_input variable. 
	''' 
	attempts_counter = 1 # 2) it counts as the first attempt.
	'''
	3) now, it analyzes the user's answer taking into account the number of 
	attempts used. In case the answer is correct (input_check returns True), 
	the loop stops or never starts. Otherwise, the loop keeps running repeating 
	the problem until the number of attempts used equals the one that is allowed 
	(the user defines this number at the beginning of the game):
	'''
	while input_check(user_input, correct_answer) != True\
	    and attempts_counter < attempts:
		user_input = raw_input('\n' + random_wrong() + '\n' + problem)
		# 4) notifies the user and repeats the first step.	
		attempts_counter += 1 # 5) it counts as the next attempt.
	'''
	6) at this point, the if-statement checks if the user's answer is correct. 
	If it is still not (input_check doesn't return True), it means the loop was 
	finished after all the allowed attempts were used. Otherwise, it means the 
	loop was finished before the number of attempts equaled the one that was 
	allowed or never started - in both cases, because of the correct answer:
	'''
	if input_check(user_input, correct_answer) != True:
		print '\n' + textwrap.fill(quiz_data.you_lost, output_line_len) 
		# 7) notifies the user. 
		sys.exit() # 8) stops the programme since the user's lost. 
	else:
		print '\n' + random_correct() 
		# 9) notifies the user about the correct answer.
		return user_input # 10) returns the correct answer.

def paragraph_changer(paragraph,blank,replacement):
	'''
	This function takes three strings as input and replaces a 'blank' in the 
	'paragraph' with the 'replacement'. It is based on the Mad-Libs-game 
	presented during work sessions. It starts with defining an empty list 
	'replaced'. The 'paragraph' string transforms into the list, whereafter all 
	the elements of the list are checked for containing the 'blank' as a 
	substring. Those containing are modified the way only the 'blank' # part is 
	replaced. All the elements are appended to the 'replaced'. In the end, 
	'replaced' contains all the original and replaced elements of the 
	'paragraph'. It transforms into the string, which the function returns.        
	'''
	replaced = [] 
	paragraph = paragraph.split()
	for word in paragraph:
		if blank in word:
			word = word.replace(blank, replacement)
		replaced.append(word)
	replaced = ' '.join(replaced)
	return replaced

def quiz_game(level,quiz_blanks_level,correct_answers_level):
	'''
	This function manages the game using the variables and functions defined 
	above. It takes three arguments as input: the string 'level', the list 
	'quiz_blanks_level', and the list 'correct_answers_level'. They are to be 
	replaced with '..._level', 'quiz_blanks_...', and 'correct_answers_...' 
	variables (see variables block above) depending on the level the user 
	chooses during the game. It doesn't return anything itself, it is basically 
	used to call other functions in the right order. Here is the logic:     
	'''
	index = 0 
	'''
	'index' is needed for the loop through the correct_answers list inside of 
	the loop through the quiz_blanks list.
	'''
	for blank in quiz_blanks_level: 
	# goes through all the blanks in the quiz_blanks list.
		'''
		During each iteration, the problem is set as the current version of the 
		string 'level' (paragraph with blanks, which features all the blanks at 
		the beginning; these blanks are being replaced with user's correct 
		answers one iteration after another) + prompt to fill in the current 
		'blank': 
		'''
		problem = '\n' + textwrap.fill(level, output_line_len) + '\n''\n'\
		    'How would you fill in this ' + blank + ' ? >>> '
		'''
		The next line of code calls the 'quiz-problem' with the current problem 
		and the element of the correct_answers list (corresponds to the current 
		blank)as arguments. The variable 'answer' saves what 'quiz_problem' 
		returns. As we know, it can happen if and only if the user's answer was 
		correct: 
		'''
		answer = quiz_problem(problem,correct_answers_level[index]) 
		# here is this second loop inside of the main loop.
		level = paragraph_changer(level,blank,answer) 
		'''
		modifies the 'level' by replacing the current 'blank' with the correct 
		'answer'. 
		'''
		index += 1 # changes the 'index' to be used during the next iteration. 
	print '\n' + textwrap.fill(level, output_line_len) + '\n\nWell done!'

def quiz_game_start():
	'''
	The user is notified of the level and the number of attempts per problem
	chosen:
	'''
	print '\nYou have chosen the ' + current_level + ' level and '\
	    + str(attempts) + ' attempts per problem.\nLet us start!'
	'''
	Depending of the value of the 'current_level' the 'guiz_game' gets relevant 
	arguments. 
	'''
	if current_level == 'easy':	
		quiz_game(quiz_data.easy_paragraph,quiz_data.easy_blanks,\
			quiz_data.easy_answers)
	elif current_level == 'medium':
		quiz_game(quiz_data.medium_paragraph,quiz_data.medium_blanks,\
			quiz_data.medium_answers)
	else:
		quiz_game(quiz_data.hard_paragraph,quiz_data.hard_blanks,\
			quiz_data.hard_answers)

 
# Here comes the stage of collecting initial input. 

# The first task is to find out which level the user prefers:
current_level = level_chosen(raw_input(quiz_data.welcome),level_options)
while level_chosen(current_level,level_options) == None: 
	current_level = level_chosen(raw_input(quiz_data.wrong_level),level_options)
'''
checks the correctness of the user's input; if it is incorrect, the prompt is 
repeated. 
	
The next task is to find out how many attempts per problem the user wants to
have. User's input is saved in the variable 'attempts' as integer to be usable 
in the 'quiz_problem': 
'''
attempts = int(raw_input(quiz_data.attempts_num))
while attempts < min_attempts or attempts > max_attempts:
	attempts = int(raw_input(quiz_data.wrong_attempts))
	'''
	checks the correctness of the user's input; if it is incorrect, the prompt 
	is repeated.
	'''

quiz_game_start() # Let the Game Begin :)