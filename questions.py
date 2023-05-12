def three_five(n):
    x = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            x = x + i
    print(x)


three_five(1000)
