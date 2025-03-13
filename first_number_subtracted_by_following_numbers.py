# ask user to input initial number

init_number = int(input("Please enter the first number: "))

# loop inputs 9 times then subtract the inputs from the initial number

for number in range(1,9):
    numbers = float(input(f"Please enter number {number + 1}: "))