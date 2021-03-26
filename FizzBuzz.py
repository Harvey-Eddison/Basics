# Basic Fizz Buzz program

# declaring my function fizzbuzz
def fizzbuzz():
    # creating 2 variables to use in the function
    # i is starting number for the sequence and itterations is how many you want to print
    i = 1
    itterations = 1000
    while i <= itterations: # setting an upper limit for the while loop to run.
        # first if statement to check if i is divisable by 3 AND 5 with NO remainder.
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
# calling the function to run
fizzbuzz()
