# create a list for numbers input
numbers = []
# create an empty set to store the numbers
seen_numbers = set()

# loop input 10 times

for inputs in range(10):
    number = int(input(f"Number {inputs + 1}: "))
    numbers.append(number)

print(numbers)
# check if inputs numbers have occured
# print output