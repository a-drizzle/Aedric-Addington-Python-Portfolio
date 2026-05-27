#dinosaurs
#The purpose of the program is so that a user can sort and look through a dataset of 300~ Dinosaurs, whether it’s to find a new favorite, or to find out a certain Dinosaur’s taxonomy, length, etc.

#imported items (Pandas for the data, time to make the program look good)
import pandas as pd
import time

data=pd.read_csv('Dinosaurs.csv') #names data

#sorts the elements of the csv file into an array
name=data["name"].tolist()#names are stored in an array
diet=data["diet"].tolist()#diet is stored in an array, etc.
period=data["period"].tolist()
lived_in=data["lived_in"].tolist()
type=data["type"].tolist()
length=data["length"].tolist()
taxonomy=data["taxonomy"].tolist()
named_by=data["named_by"].tolist()
species=data["species"].tolist()
results=[]#results are where the different data matching different criteria are temporarily placed into, which are then pulled from


#functions
print("Welcome to the Dinosaur finder. You can search through different criteria to learn about over 300 mezozoic animals.")
def main_menu():
    while True:
        print("\nMain Menu:")#Main menu with options
        print("1. Search by name")
        print("2. Search by diet")
        print("3. Search by period")
        print("4. Search by country discovered")
        print("5. Search by type")
        print("6. Search by length")
        print("7. Search by taxonomy")
        print("8. Search by species")
        print("9. Exit Program")
        print("10. Who the Dinosaur was named by, is performed through a function.")
        choice = input("Enter your choice (1-10): ").strip()#removes trailing spaces, collects the input
        if choice == '1':
            namefinder()
        elif choice == '2':
            dietfinder()
        elif choice == '3':
            periodfinder()
        elif choice == '4':
            country()
        elif choice == '5':
            typefinder()
        elif choice == '6':
            lengthfinder()
        elif choice == '7':
            taxonomyfinder()
        elif choice == '8':
            speciesfinder()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        elif choice == '10':
            named_byfinder("Stromer")#name searched of someone who named a Dinosaur, this runs the function that is near the bottom of this function

        else:
            print("Error: Invalid choice. Please enter a number between 1 and 9.")

def namefinder():
    namesearch=input("What name are you looking for? (eg. tyrannosaurus, velociraptor, etc.): ").strip().casefold()#removes hanging spaces and decapitalizes
    found=False
    for i in range(len(data)):
        if namesearch in str(name[i]):#makes sure it is in string form
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])
            #I removed the print(results) line as it provided no information to the user
            found=True #confirms the input is valid
    if not found: #if input is not an option, it makes you go back and re-enter a valid option
        print("Oops, looks like that name can't be found. Please try again!")
    results.clear()
    time.sleep(2.5) #adds some delay so that user has time to read and understand what is going on

def dietfinder():
    dietsearch=input("What diet do you want to sort by? (eg., carnivorous, herbivorous, omnivorous): ").strip().casefold()
    found=False
    for i in range(len(data)):
        if dietsearch in str(diet[i]):
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])

            found=True
    if not found:
        print("Oops, looks like that diet can't be found. Please try again!")
    results.clear()
    time.sleep(2.5)

def periodfinder():
    periodsearch=input("What period do you want to sort by? (eg., Triassic, Jurassic, Cretaceous): ").strip().capitalize()#removes the excess spaces and capitalizes first letter
    found=False
    for i in range(len(data)):
        if periodsearch in str(period[i]):
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])

            found=True
    if not found:
        print("Oops, looks like that period can't be found. Please try again!")
    results.clear()
    time.sleep(2.5)

def country():
    countrysearch=input("What country do you want the Dinosaur to be discovered in? (eg., USA, Argentina, etc.): ").strip().lower()
    found=False
    for i in range(len(data)):
        if countrysearch in str(lived_in[i]).lower():
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])

            found=True
    if not found:
        print("Oops, looks like that country can't be found. Please try again!")
    results.clear()
    time.sleep(2.5)

def typefinder():
    typesearch=input("What type do you want to sort by? (eg., theropod, sauropod, euornithopod, etc.): ").strip()
    found=False
    for i in range(len(data)):
        if typesearch in type[i]:
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])

            found=True
    if not found:
        print("Oops, looks like that is an invalid type. Please try again with a valid type!")
    results.clear()
    time.sleep(2.5)

def lengthfinder():
    while True: #in case of non numeral input
        try:
            lengthsearch = float(input("What range in meters? First value: ").strip())
            lengthsearch2 = float(input("Second value: ").strip())
        except ValueError:
            print("Uh-oh, invalid input... Please enter only numbers (e.g., 5, 8.5)")
            continue #stops program from stopping
        for i in range(len(data)):
            current_val = str(length[i]).replace('m', '').strip()#removes the m, as the values stored are in the form 5m, 1.3m, etc.
            current_length = float(current_val) #makes sure the value is treated as a number
            if lengthsearch<=current_length<=lengthsearch2:
                results.append([i])
                print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])

                results.clear()
        break
    time.sleep(2.5)

def taxonomyfinder():
    taxonomysearch=input("What is the taxonomy of the Dinosaur? It can be as broad as (Ornithischia) or specific as (Lambeosaurinae): ").strip().lower()
    found=False
    for i in range(len(data)):
        if taxonomysearch in str(taxonomy[i]).lower():
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])
            found=True
    if not found:
        print("Oops, looks like that taxonomy can't be found. (Likely a misspelling). Please try again!")
    results.clear()
    time.sleep(2.5)

def speciesfinder():
    speciessearch=input("What is the species of the Dinosaur? (eg., homeri, ajax, major): ").strip().lower()
    found=False
    for i in range(len(data)):
        if speciessearch in str(species[i]).lower():
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])
            found=True
    if not found:
        print("Oops, looks like that species can't be found. (Likely a misspelling). Please try again!")
    results.clear()
    time.sleep(2.5)

def named_byfinder(search_name): #this serves as the function with a parameter, if statement, and loop.
    found=False
    search_term = search_name.lower() #converts input to lowercase so it can be searched
    for i in range(len(data)):
        if search_term in str(named_by[i]).lower():
            results.append([i])
            print(data.loc[[i], ["name", "species", "diet", "period", "type", "length", "lived_in", "named_by", "taxonomy"]])
            found=True
    if not found:
        print("Oops, looks like that name can't be found. Please try again!")
    results.clear()
    time.sleep(2.5)


#main
main_menu() #runs it!



#Sources
#Dinosaur Dataset
#Website Name: kaggle.com
#URL: https://www.kaggle.com/datasets/smruthiiii/dinosaur-dataset
