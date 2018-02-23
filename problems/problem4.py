# Problem 4:
# Points: 3
# Bonus Objective: Use a while loop. Points: 1
# Using the given string, calculate the sum of the ord() value of each character. The ord() function returns
# the numerical value of a single character.
# Write your code and return the sum.
def problem4():
	string = "How much is this string of characters, '!#)!^$!', actually worth?"
        list_string = list(string)
        print (list_string)
        num_holder = 0
        final_answer = 0
        while num_holder < len(list_string):
            final_answer += (ord(list_string[num_holder]))
            num_holder += 1
            print(final_answer)

problem4()