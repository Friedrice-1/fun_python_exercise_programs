# initialize number variable

current_number = 0

# loop 100 times

while True:
    current_number += 1
    if current_number == 101:
        break
# check if the current number is odd
    if current_number % 2 != 0:
# print number
        print(current_number)