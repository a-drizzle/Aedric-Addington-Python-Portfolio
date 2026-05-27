#aedric
#to-do list
#List user can manipulate, contains books to read
import os
preexistingdata='book_list.txt'
reading_list = []
read_list = []

def save_reading_log():
    with open(preexistingdata, 'w') as file:
        # Saves read books
        for book in read_list:
            file.write(f"Read: {book}\n")
        # Saves books on reading list
        for book in reading_list:
            file.write(f"To read: {book}\n")

def display_lists():
    print("\n" * 5)
    print(f"You have {len(reading_list)} book(s) on the reading list.")
    for index, task in enumerate(reading_list):
        print(f"  {index + 1}. {task}")
    print(f"Read books:")
    if not read_list:
        print("No books read yet.")
    for task in read_list:
        print(f"     {task}")

def add_item():
    item = input("What book do you want to add to the list: ").strip()
    if item:
        reading_list.append(item)
        print(f"'{item}' added.")
        save_reading_log()
    else:
        print("Oops. I don't understand.")

def mark_done():
    display_lists()
    if not reading_list:
        print("There aren't any books to mark as read.")
        return
    try:
        item_index = int(input("Enter the number of the book you read (or 0 to cancel): "))
        if item_index == 0:
            return
        item_index -= 1

        if 0 <= item_index < len(reading_list):
            completed_item = reading_list.pop(item_index)
            read_list.append(completed_item)
            print(f" '{completed_item}' was marked as done! Hope it was good.")
            save_reading_log()
        else:
            print("Invalid item number. Oops.")
        if len(read_list)==1:
            print("Groovy man! Thats the first book! Lets keep reading!")
        if len(read_list)==3:
            print("Alright bookworm! Keep reading!")
        if len(read_list)==5:
            print("Five books down! Great job! Keep reading!")
        if len(read_list)==10:
            print("Ten books down! Great job! Keep reading!")
    except ValueError:
        print("Oops. This index is a number only establishment, your words are no good here. Try again ")

def remove_clear():
    while True:
        choice = input("Do you want to remove an item (R), or clear the list (c)? (0 to cancel): ").lower().strip()
        if choice == '0':
            return
        elif choice == 'c':
            confirm = input("Are you super sure you want to clear the entire reading list? (yes/no): ").lower().strip()
            if confirm == 'yes':
                reading_list.clear()
                print("List cleared.")
                save_reading_log()
            break
        elif choice == 'r':
            display_lists()
            if not reading_list:
                print("No books to remove.")
                break
            try:
                item_index = int(input("Enter the number of the book to remove (or 0 to cancel): "))
                if item_index == 0:
                    break
                item_index -= 1
                if 0 <= item_index < len(reading_list):
                    removed_item = reading_list.pop(item_index)
                    print(f"'{removed_item}' was removed.")
                    save_reading_log()
                else:
                    print("Invalid number. Gulp. ")
            except ValueError:
                print("This is a number only establishment, your words are no good here. Try again ")
            break
        else:
            print("Whoops, invalid choice. Please enter 'R' to remove, 'C' to clear, or '0' to cancel.")

def main_menu():
    while True:
        display_lists()
        print("\nMain Menu:")
        print("1. Add a new item")
        print("2. Mark an item as done")
        print("3. Remove an item or Clear the List")
        print("4. Exit the program")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            mark_done()
        elif choice == '3':
            remove_clear()
        elif choice == '4':
            print("Exiting application. Goodbye!")
            save_reading_log()
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")
def load_reading_log():
    global reading_list
    global read_list
    if os.path.exists(preexistingdata):
        with open(preexistingdata, 'r') as file:
             for line in file:
                line = line.rstrip('\n')
                if line.startswith("Read: "):
                    read_list.append(line[6:]) # Changes title
                elif line.startswith("To read: "):
                    reading_list.append(line[9:])
        print(f"Loaded booklist from {preexistingdata}")


load_reading_log()
main_menu()
