#Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.

for c in range(10):
    if c%20==0:
        print("twist")
    elif c%15==0:
        pass
    elif c%5==0:
        print("fizz")
    elif c%3==0:
        print("buzz")

    else:
        print(c)                