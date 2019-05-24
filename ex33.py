from sys import argv
script, the_value, incrementer= argv
def while_fun(the_value, incrementer):
    i=0
    numbers = []
    while i < int(the_value):
        print(f"At the top i is {i}")
        numbers.append(i)

        i+=int(incrementer)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers
numbers = while_fun(the_value, incrementer)
print("The Numbers: ")

for num in numbers:
    print(num)
