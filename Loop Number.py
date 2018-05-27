#ask user the number wish to be played
user_play = "y"
while user_play == "y":
    user_number = input("Whats your number to play?? ")

for x in range(int(user_number) +1):
    print (x)

user_play = input("want to play more (y)es or (no)")
