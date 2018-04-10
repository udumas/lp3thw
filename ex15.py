# Import the argv component from the sys package
from sys import argv

# save the values from the argv list into the variables script and filename
script, filename = argv

# create a file named txt using the filename entered at the command line
txt = open(filename)

# Print the name of the file 
print(f"Here is your file {filename}:")
# Print the contents of the file
print(txt.read())

# Print a prompt to the user 
print("Type the filename again:")
# get the name of a new file to be printed
file_again = input("> ")
# Create a file from the filename entered by the user
txt_again = open(file_again)

# Print out the contents of the filen
print(txt_again.read())


