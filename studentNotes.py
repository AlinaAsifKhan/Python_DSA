import os

file = "notes.txt"

def add_note():
    new_note = input("Enter the notes")

    with open(file, 'a') as f:
        f.write(new_note)
        print("Note added succesfully!")

def view_note():
    if not os.path.exists(file):
        print("No file exists.")
        return
    print("---Your Notes---")
    with open(file, 'r') as f:
        notes = f.readlines()
        if notes:
            for line in notes:
                print(line.strip())
        else:
            print("No notes yet.")

def main():
    while True:
        print("----Student Notes Logger---")
        print("1. Add notes")
        print("2. view All notes")
        print("3. Exit")

        choice = input("Enter your choice from the menu:")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_note()
        elif choice == "3":
            print("Logging out..")
            break
        else:
            print("Invalid choice, Try Again.")
        

if __name__ == '__main__':
    main()
