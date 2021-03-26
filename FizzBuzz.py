
def fizzbuzz():
    i = 1
    itterations = 1000
    while i <= itterations:
        if i % 3 == 0 and i % 5==0:
            print("Fizz Buzz")
            i += 1

        elif i % 5 ==0:
            print("Buzz")
            i += 1

        elif i % 3 ==0:
            print("Fizz")
            i += 1

        else:
            print(i)
            i += 1

fizzbuzz()
