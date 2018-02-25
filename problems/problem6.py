# Problem 6:
# Points: 8
# Bonus Objective: Include comments within your code. Points: 1
# Consider a number n is backwards if it is written in reverse order.
# 34 written backwards is 43 and 103 written backwards is 301. Using positive
# integers, find the total number of backwards numbers less than one-million
# where the sum of the number forwards and backwards contains only
# odd digits (34+43=77). 
# Write your code and return the answer.
def problem6():
    list_of_numbers = [1, 2, 3, 4, 5]
    backwards = []
    backwards = (list_of_numbers[::-1])
    print(backwards)
    

problem6()