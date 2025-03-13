# initialize even number count variable

even_number = 0

# loop inputs 10 times

for i in range(10):
    numbers = int(input(f"Please enter number {i + 1}: "))
# increment the input to the even number count variable if the input is even
    if numbers % 2 == 0:
        even_number += 1

# print result
print(f"There are {even_number} even numbers.")