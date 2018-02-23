import math

name = "Clayton"

print("Working...")

print("Hello " + name)

print("What fromula will it be today?")

print("1: Pythagorean Theorem")
print("2: Quadratic Formula")

formula = input()

if formula == 1:
    print("Pythagorean Theorem")
    def Pythagorean_Theorem(a, b, c):
        # a^2 + b^2 = c^2
        if a == "?": 
            print("A is not defined")   
    
    print("If length is unknown insert, ?")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    Pythagorean_Theorem(a, b, c)
elif formula == 2:
    print("Quadratic Formula")
        