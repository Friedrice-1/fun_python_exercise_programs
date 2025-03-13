# create a list for user input and duplicate numbers

numbers =  []
duplicate_numbers = []

# loop input 10 times and list them

for inputs in range(10):
    number = int(input(f"Please enter number {inputs + 1}: "))
    numbers.append(number)

# count how many numbers are in the list
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicate_numbers:
# store duplicate numbers in user input list to the duplicate number list
        duplicate_numbers.append(number)
# print duplicate numbers
print(f"The numbers that are duplicate/s are: {duplicate_numbers}")