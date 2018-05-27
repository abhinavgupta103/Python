import random 
print ("lest play")
Options = ["r", "p", "s"]
computer_choice = random.choice(Options)

user_choice = input(" You Options Are (r)ock)(p)aper,(s)cissors")

if (user_choice == "r" and computer_choice == "p"):
    print("You chose rock, I chose paper - you lost!")

elif (user_choice == "r" and computer_choice == "s"):
    print("You chose rock, I chose scissor - you lost!")

elif (user_choice == "r" and computer_choice == "r"):
    print("You chose rock, I chose rock - you WIN!")

elif (user_choice == "p" and computer_choice == "r"):
    print ("You chose paper, I chose rock - you lose!")

elif (user_choice == "p" and computer_choice == "s"):
    print ("You chose paper, I chose scissor - you lose!")

elif (user_choice == "p" and computer_choice == "p"):
    print ("You chose paper, I chose paper - you WIN!")

elif (user_choice == "s" and computer_choice == "s"):
    print ("You chose scissor, I chose siccor - you WIN!")
elif (user_choice == "s" and computer_choice == "r"):
    print ("You chose scissor, I chose rock - you lose!")
elif (user_choice == "s" and computer_choice == "p"):
    print ("You chose scissor, I chose paper - you lose!")


    
        


