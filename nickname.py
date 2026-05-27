#aedric
#superhero nickname
#generate a nickname for someone

#fncts
def generate():
        print("Hey, you need a nickname, superhero. ")
        first= input("are you the chillest? (yes/no): ").lower()
        #chillest route
        if first == "yes":
            second = input("do you stay the flyest? (yes/no): ").lower()
            if second == "yes":
                third = input("chill and fly... okay. Are you more hopeful, or fearless? " ).lower()
                if third == "hopeful":
                    print("You are the Man of Steel")
                elif third == "fearless":
                    print("You are the Emerald Knight")
                else:
                    print("Invalid input... read what is asked carefully")
            elif second == "no":
                third = input("Thats dope... run the streets, or jump across buildings? (run/jump): ").lower()
            else:
                print("Invalid input... read what is asked carefully")
                if third == "run":
                    print("You are the Fastest Man Alive")
                elif third == "jump":
                    print("You are the Emerald Archer")
                else:
                    print("Invalid input... read what is asked carefully")
        #not chill plays
        elif first == "no":
            second = input("all good, sometimes you gotta be chalant. Are you a regal person? (yes/no): ").lower()
        else:
            print("Invalid input... read what is asked carefully")
            if second == "yes":
                third = input(" Take to the skies, or go for a dip? (skies/water): ").lower()
                if third == "skies":
                    print("You are the Warrior Princess of Themyscira")
                elif third == "water":
                    print("You are the King of the Seven Seas")
                else:
                    print("Invalid input... read what is asked carefully")
            elif second == "no":
                third = input("Do you fight crime in the streets, or beyond the stars? (streets/stars): ").lower()
            else:
                print("Invalid input... read what is asked carefully")
                if third == "streets":
                    print("You are the Caped Crusader")
                elif third == "stars":
                    print("You are the Martian Manhunter")
                else:
                    print("Invalid input... read what is asked carefully")

while True:
    generate()
    restart_choice = input("Do you want to start over? (yes/no): ").lower()

    if restart_choice == 'no':
        print("Exiting the program. Bye bro!")
        break
    elif restart_choice == 'yes':
        print("Yes!!! Starting over...")



