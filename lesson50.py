#Write a program to display 1 to 10 numbers in reverse order and skip the number 5.

range=10

while range  > 0:
    range=range-1
    if range==5:
        continue
    print("\n Current variable value is :", range)
print("\n good bye")   