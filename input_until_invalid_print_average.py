# initialize input count
# initialize sum variable

input_count = 0
total_sum = 0

# loop inputs until invalid

while True:
    try:
        number = int(input("Please enter a number: "))
    except ValueError:
        break
# print average