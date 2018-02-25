# Problem 5:
# Points: 4
# Find the smallest positive integer number that has 50 divisors.
# Write your code and return the number.
def problem5():
    divide = 2
    divisor = 1
    number_of_divisors = 0
    while number_of_divisors < 50:
        divisor = divide
        divide / divisor
        divide += 2
        divisor -= 1

    

problem5()