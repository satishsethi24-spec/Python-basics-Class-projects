# Write a python program using OR operator to find the day is weekday or weekend

day = input("Enter the day : ")

day = day.lower()

if day == 'saturday' or day == 'sunday':

    print("Weekend")

else:

    print("Weekday")