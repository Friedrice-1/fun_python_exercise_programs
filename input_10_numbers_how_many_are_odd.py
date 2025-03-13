# initialize odd number count variable

odd_number = 0

# loop inputs 10 times

for i in range(10):
    numbers = int(input(f"Please enter number {i + 1}: "))
# increment the input to the odd number count variable if the input is odd
    if numbers % 2 != 0:
        odd_number += 1
# print result
print(f"There are {odd_number} odd numbers.")