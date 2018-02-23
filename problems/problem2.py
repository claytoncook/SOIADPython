# PROBLEM 2:
# Points: 3
# Find the sum of the positive, even numbers between 0 and 100. 
# Write your code and return the sum.
def problem2():
    num_holder = 0
    final_answer = 0
    while num_holder < 100:
        num_holder += 2
        final_answer += num_holder
        print(num_holder)

    print(final_answer)

problem2()