# create a list for numbers input
numbers = []
# create an empty set to store the numbers
seen_numbers = set()

# loop input 10 times

for inputs in range(10):
    number = int(input(f"Number {inputs + 1}: "))
    numbers.append(number)

# check if inputs numbers have occured
for number in numbers:
    if number not in seen_numbers:
        seen_numbers.add(number)
# print output
        print(number, end=" ")