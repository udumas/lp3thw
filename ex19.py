# define cheese_and_crackers function that takes two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print amount of cheeses
    print(f"You have {cheese_count} cheeses!")
    #print number of boxes of boxes_of_crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #print anecdote
    print("Man that's enough for a party")
    #print another anecdote
    print("Get a blanket\n")

print("We can just give the function numbers directly:")
#call the cheese_and _crackers function with the constant parameters 20 and 30
cheese_and_crackers(20,30)

print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# call the cheese and crackers function with variables as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
#call the cheese and crackers function with parameters that are the result of equations
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 10000)
