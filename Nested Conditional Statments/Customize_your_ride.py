print("Select your ride \n 1. Bike \n 2. Car ")

choiceVehicle = int(input("Enter your choice : "))

if choiceVehicle == 1:

    print("You have selected Bike Ride")

    print("Enter the type of bike \n B1. Hero Splendor \n B2. Honda Shine ")

    choiceBike = input("Enter the type of Vehicle : ")

    if choiceBike == 'B1':

        print("You have selected Hero Splendor")

    else:

        print("You have selected Honda Shine")

elif choiceVehicle == 2:

    print("You have selected Car Drive")

    print("Enter the type of car \n C1. Indica \n C2. Xylo ")

    choiceCar = input("Enter the type of Vehicle : ")

    if choiceCar == 'C1':

        print("You have selected Indica")

    else:

        print("You have selected Xylo")

else:

    print("Invalid input")