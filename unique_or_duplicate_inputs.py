# initialize number list

numbers = []

# loop inputs until invalid

while True:
    try:
        number = int(input("Please enter a number: "))
# append input to the number list
        numbers.append(number)
# check if input is a duplicate or unique
        if numbers.count(number) == 1:
            print("Unique")
        else:
            print("Duplicate")
# if input is invalid the loop stops
    except:
        ValueError
        break