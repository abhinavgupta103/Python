listofpie = ["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko","Burek", "Tamale", "Steak"]

choice = input("Do you want more Pie: ")  

while (choice == "Yes"):
    order = input("Which Pie do you want to order? ")
    print("Superb your " + order + " will be ready")
    choice = input("Do you want more? ")
    