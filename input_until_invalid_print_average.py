# initialize input count
# initialize sum variable

input_count = 0
total_sum = 0

# loop inputs until invalid

while True:
    try:
        number = int(input("Please enter a number: "))
        total_sum += number
        input_count += 1
    except ValueError:
        break
# print average
print(f"The average is: {total_sum / input_count}")