# The parameter is the name of the data here it is name
# The argument is the actual value of the data
def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"How is the weather {name}?")


greet('Adam')


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# This is positional arguments
greet_with('Adam', 'Spain')

# These are keyword arguments with this you can modify the order of the arguments
greet_with(location='Hungary', name='Adam')


def prime_checker(number):
    flag = False
    if number == 1:
        print(number, "is not a prime number")
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break

        if flag:
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")
