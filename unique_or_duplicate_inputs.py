# initialize number list

numbers = []

# loop inputs until invalid

while True:
    try:
        number = int(input("Please enter a number: "))
# append input to the number list
        numbers.append(number)
    except:
        ValueError
        break

print(numbers)
# check if input is a duplicate or unique
# if input is invalid the loop stops