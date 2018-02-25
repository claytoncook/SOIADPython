def app():
    x = 2
    solutions = []
    while x < 1000:
        a = list(str(x))
        b = int(''.join(str(num) for num in a[::-1]))
        a = int(''.join(str(num) for num in list(str(x))))
        c = a + b
        even = c % 2
        if even != 0:
            print(a, b, c)
        x += 2
app()