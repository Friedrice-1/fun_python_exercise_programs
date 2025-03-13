# create a list for user input and unique numbers

numbers =  []
unique_numbers = []

# loop input 10 times and list them

for inputs in range(10):
    number = int(input(f"Please enter number {inputs + 1}: "))
    numbers.append(number)

# count how many numbers are in the list
for number in numbers:
    if numbers.count(number) == 1:
# store unique numbers in user input list to the unique number list
        unique_numbers.append(number)
# print unique numbers
print(f"The numbers that dont have duplicate/s are: {unique_numbers}")