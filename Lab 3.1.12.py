year = int(input("Enter a year: "))
# Make the question a loop
while year >= 1581:
    if year < 1582:
	    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common Year")
    elif year % 100 != 0:
        print("Leap Year")
    elif year % 400 != 0:
        print("Common Year")
    else:
        print("Leap Year")
year = int(input("Enter a year: "))
