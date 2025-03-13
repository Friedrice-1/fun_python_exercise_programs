# ask user to input initial number

init_number = int(input("Please enter the first number: "))

# loop inputs 9 times then subtract the inputs from the initial number

for number in range(1,10):
    numbers = float(input(f"Please enter number {number + 1}: "))
    init_number -= numbers

print(f"The remaining number is: {init_number}")