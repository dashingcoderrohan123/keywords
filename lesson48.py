#Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”

string=input("Enter the word")


 
for u in string:
    if u=="A":
        print("A is found")
        break
    else:
        print("A is not found")