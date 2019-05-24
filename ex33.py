from sys import argv
script, the_value = argv
def while_fun(the_value):
    i=0
    numbers = []
    while i < the_value:
        print(f"At the top i is {i}")
        numbers.append(i)

        i+=1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers
numbers = while_fun(the_value)
print("The Numbers: ")

for num in numbers:
    print(num)
