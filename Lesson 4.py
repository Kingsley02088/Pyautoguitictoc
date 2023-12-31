#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

# Defining two variables to None.
largest = None
smallest = None
# starting an infinite loop
while True:
    num = input("Enter a number: ")
# try block to capture ValueError
    try:
        if num == "done":
            break
# assign the values of largest and smallest to num if its None ( on first iteration)
        if largest is None:
            largest = (num)
        if smallest is None:
            smallest = int(num)
# changing the values of it greater or smaller
        if int(num) > largest:
            largest = int(num)
        if int(num) < smallest:
            smallest = int(num)
# capture the type error and ignores.
    except ValueError:
        print("Invalid input")
        continue
print("Maximum " 'is' ,str(largest))
print("Minimum " 'is' , str(smallest))