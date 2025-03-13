# make a list for numbers input

numbers = []

# loop until invalid

while True:
    try:
        number = int(input("Please enter a number: "))
# append input to number list
        numbers.append(number)
# check if input is invalid
    except ValueError:
        break

print(numbers)
# make dictionary for counting numbers
# find the most repeated number
# print result