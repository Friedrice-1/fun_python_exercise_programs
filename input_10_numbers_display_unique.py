# create a list for user input and unique numbers

numbers =  []
unique_numbers = []

# loop input 10 times and list them

for inputs in range(10):
    number = int(input(f"Please enter number {inputs + 1}: "))
    numbers.append(number)

print(numbers)

# count how many numbers are in the list
# store unique numbers in user input list to the unique number list
# print unique numbers