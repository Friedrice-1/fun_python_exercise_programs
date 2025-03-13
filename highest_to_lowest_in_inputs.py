# initialize list

numbers = []

# loop inputs until invalid

while True:
    try:
        number =  int(input("Please enter a number: "))
# append input to the list
        numbers.append(number)
# check if input is invalid
    except ValueError:
        break

# print list from highest to lowest
numbers.sort(reverse=True)
print(numbers)