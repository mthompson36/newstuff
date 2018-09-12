#This program will return in your number is odd or even.

number = int(input("Please enter a number:"))
if (number % 2) == 0:
	print(str(number) +" Can be divided by 2")
else:
	print("This is an odd number")