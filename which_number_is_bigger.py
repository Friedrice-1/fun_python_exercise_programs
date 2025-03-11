# input 2 numbers

num_1 = int(input("Please enter the first  number: "))
num_2 = int(input("Please enter the second  number: "))

# check which number is bigger
# print the bigger number

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_2 > num_1:
    print(f"{num_2} is greater than {num_1}")
else:
    print("Numbers are equal.")