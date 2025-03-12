# initialize total sum variable

total_sum = 0

# loop inputs 10 times

for inputs in range(10):
    numbers = int(input(f"Please enter number {inputs+1}: "))
# increment the inputs to the total sum variable
    total_sum += numbers

# print result
print(f"The sum of 10 numbers are {total_sum}")