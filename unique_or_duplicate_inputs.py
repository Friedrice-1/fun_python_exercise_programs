# initialize number list

number = []

# loop inputs until invalid

while True:
    try:
        num = int(input("Please enter a number: "))
    except:
        ValueError
        break

# append input to the number list
# check if input is a duplicate or unique
# if input is invalid the loop stops