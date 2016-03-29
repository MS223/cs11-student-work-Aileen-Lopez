number = input("enter number")
while number in range(1, number+1):
    print number
    number = number - 1
print "BOOM!"

# missing number in between "while" and "in"
# Had to count down had to switch number = number + 1 to number = number - 1. 
