#aedric
#hogwarts
#assigns user to harrypotter house

#init
import time
import random
#functions
def main():
    print("Welcome to Hogwarts bro")
    name=input("What's your name? Bro: ")
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print( house(name) )

    #ts function checks a name and returns a harry potter house
def house(name):
    house_list = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    random_item = random.choice(house_list)
    if name=="Harry" or name=="Hermoine" or name=="Ron":
        return "Gryffindor"
    elif name=="Newt" or name=="Nymphadora" or name=="Pomona":
        return "Hufflepuff"
    elif name=="Luna" or name=="Cho" or name=="Filius":
        return "Ravenclaw"
    elif name=="Voldemort" or name=="Draco" or name=="Severus":
        return "Slytherin"
    else:
        return (f"{random_item}")

#main
while True:
    main()
    restart_choice = input("Do you want to start over? (yes/no): ").lower()

    if restart_choice == 'no':
        print("Exiting the program. Bye bro!")
        break
    elif restart_choice == 'yes':
        print("Yes!!! Starting over...")
