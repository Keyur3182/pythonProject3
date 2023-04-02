Sum = 0
print("Shri Ram Genral Store")
while True:
 Userinput = input("Enter the price of items: \n")
 if (Userinput!= "Enter"):
     Sum = Sum + int(Userinput)
     print(f"order total so is: {Sum}")

 else:
     print(f"Your bill total is {Sum}.thanks for shopping with us")
     break

