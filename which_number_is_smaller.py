# input 2 numbers

num_1 = int(input("Please enter the first  number: "))
num_2 = int(input("Please enter the second  number: "))

# check which number is smaller
# print the smaller number

if num_1 < num_2:
    print(f"{num_1} is smaller than {num_2}")
elif num_2 < num_1:
    print(f"{num_2} is smaller than {num_1}")
else:
    print("Numbers are equal.")