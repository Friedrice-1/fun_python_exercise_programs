# initialize odd count variable

odd_count = 0

# loop inputs 10 times

for inputs in range(10):
    numbers = int(input(f"Please enter number {inputs+1}: "))
# count how many are odd
    if numbers % 2 != 0:
            odd_count += 1

# print result
print(f"There are {odd_count} odd numbers.")