# initialize list

numbers = []

# loop inputs until invalid

while True:
    try:
        number = int(input("Please enter a number: "))
# append input to the list
# check if input is invalid
    except ValueError:
        break
# print lowest number in the inputs