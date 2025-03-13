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

# make dictionary for counting numbers
count_dict = {}

# find the most repeated number
for number in numbers:
        count_dict[number] = count_dict.get(number, 0) + 1
most_frequent = max(count_dict, key=count_dict.get)

# print result
print(most_frequent)