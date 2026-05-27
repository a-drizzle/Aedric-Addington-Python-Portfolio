#aedric
#madlibs
#User input makes a story
import random
import time
#main
def madlibs():
    print("Hello brochaco. Lets make a story!")
    time.sleep(1)
    #pt1
    names = ["LEBRON", "BARTHOLOMEW", "MICHAEL JORDAN", "A GOAT"]
    name=input("Give me a name: ").upper()
    if name == "RANDOM":
        selected_name = random.choice(names)
    else:
        selected_name = name
    verb=input("Give me a verb (Past tense): ").upper()
    adjective=input("Give me an adjective!: ").upper()
    place=input("Give me a place: ").upper()
    noun=input("And a noun!: ").upper()
    noun2=input("And a noun!: ").upper()
    names2 = ["CHARLIE", "LINUS", "SNOOPY", "SALLY"]
    name2=input("Give me a name: ").upper()
    if name2 == "RANDOM":
        selected_name2 = random.choice(names2)
    else:
        selected_name2 = name2
    print(f"""Part I:
It was a dark and \033[1m{adjective}\033[0m night. Suddenly, a shot rang out! A \033[1m{noun}\033[0m slammed. \033[1m{selected_name}\033[0m screamed.
Suddenly, a \033[1m{noun2}\033[0m appeared on the horizon! While millions of people were \033[1m{verb}\033[0m, the king lived in luxury.
Meanwhile, in \033[1m{place}\033[0m, \033[1m{selected_name2}\033[0m was growing up.""")
    cont=input("wanna write part 2? (yes/no): ")
    if cont == "yes":
        names3=["BATMAN, SUPERMAN, WONDERWOMAN, FLASH"]
        name3=input("Give me a name: ").upper()
        if name3 == "RANDOM":
            selected_name3 = random.choice(names3)
        else:
            selected_name3 = name3
        verb2=input("Give me a verb (Past tense): ").upper()
        adjective2=input("Give me an adjective!: ").upper()
        place2=input("Give me a place: ").upper()
        noun=input("And a noun!: ").upper()
        noun2=input("And a noun!: ").upper()
        names4=["CALEB WILLIAMS, COLSTON LOVELAND, DJ MOORE, ROME ODUNZE"]
        name4=input("Give me a name: ").upper()
        if name4 == "RANDOM":
            selected_name4 = random.choice(names4)
        else:
            selected_name4 = name4
        name5=input("Give me a name: ").upper()
        number=input("Give me a number: ").upper()
        print(f"""Part I:
It was a dark and \033[1m{adjective}\033[0m night. Suddenly, a shot rang out! A \033[1m{noun}\033[0m slammed. \033[1m{selected_name}\033[0m screamed.

Suddenly, a \033[1m{noun2}\033[0m appeared on the horizon! While millions of people were \033[1m{verb}\033[0m, the king lived in luxury.

Meanwhile, in \033[1m{place}\033[0m, \033[1m{selected_name2}\033[0m was growing up.

Part II:
A light snow was falling, and \033[1m{selected_name3}\033[0m with the \033[1m{adjective2}\033[0m shawl had not sold a violet all day.

At that very moment, a young \033[1m{selected_name4}\033[0m at \033[1m{place2}\033[0m Hospital was \033[1m{verb2}\033[0m an important discovery.

The mysterious patient \033[1m{name5}\033[0m in Room \033[1m{number}\033[0m had finally awakened. They moaned softly.

Could it be that they were the sister of the \033[1m{selected_name2}\033[0m in \033[1m{place}\033[0m who loved \033[1m{selected_name3}\033[0m with the \033[1m{adjective2}\033[0m shawl who was the daughter of \033[1m{selected_name}\033[0m who had escaped from the \033[1m{noun2}\033[0m?

And so the ranch was saved.
\033[3mTHE END\033[0m
-By Aedric, Snoopy, and you""")
    else:
        print("The story ends here...")


madlibs()
