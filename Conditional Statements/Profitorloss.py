# Check for profit or loss
cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))
if sp>cp:
    print("profit")
elif cp>sp:
    print("Loss")
else:
    print("No profit or loss")