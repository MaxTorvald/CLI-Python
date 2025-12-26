# Rebuilding a Simple CLI Bookstore in Python

import os
from datetime import datetime
import sqlite3

def load_booklist():
    booklist = []
    try:
        with open("TheBookList.txt", "r") as infile:
            for line in infile:
                booklist.append(line.strip().split(","))
    except FileNotFoundError:
        print("TheBookList.txt not found. Starting a new book list.")
    return booklist

def save_booklist_to_desktop(booklist):
    print("Saving your booklist to your desktop...")

    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"TheBookList_{timestamp}.txt"
    file_path = os.path.join(desktop_dir, filename)

    if not os.path.exists(desktop_dir):
        print("Desktop folder not found. Saving to current directory instead.")
        file_path = filename

    try:
        with open(file_path, "w") as outfile:
            for book in booklist:
                outfile.write(",".join(map(str, book)) + '\n')
        print(f"Booklist saved successfully to: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    booklist = load_booklist()

    print("Welcome to the Bookstore! Please choose from the following options:")

    while True:
        print("\nMenu:")
        print(" 1. Add a Book")
        print(" 2. Lookup a Book")
        print(" 3. Display All Books")
        print(" 4. Exit")
        print(" 5. Buy a Book")
        print(" 6. Rent a Book")
        print(" 7. Save as Text File")

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            confirm = input("Would you like to add a book? (Yes/No): ").strip().lower()
            if confirm == "yes":
                nBook = input("Enter the book's name: ")
                nAuthor = input("Enter the author's name: ")
                nDate = input("Enter the date of publication: ")
                nPage = input("Enter the number of pages: ")
                try:
                    nPrice = float(input("Enter the price of the book: "))
                except ValueError:
                    print("Invalid price. Returning to main menu...")
                    continue
                booklist.append([nBook, nAuthor, nDate, nPage, nPrice])
                print("Book added successfully.")
            else:
                print("Returning to main menu...")

        elif choice == 2:
            keyword = input("Enter a search term: ").strip().lower()
            found = False
            for book in booklist:
                if keyword in [field.lower() for field in map(str, book)]:
                    print(f"Found: {book}")
                    found = True
            if not found:
                print("No matching book found.")

        elif choice == 3:
            if not booklist:
                print("No books in the list.")
            else:
                print("\n{:<30} {:<20} {:<15} {:<10} {:<10}".format("Title", "Author", "Date", "Pages", "Price"))
                print("-" * 90)
                for book in booklist:
                    print("{:<30} {:<20} {:<15} {:<10} ${:<10.2f}".format(book[0], book[1], book[2], book[3], float(book[4])))

        elif choice == 4:
            confirm = input("Are you sure you want to exit? (Yes/No): ").strip().lower()
            if confirm == "yes":
                save_booklist_to_desktop(booklist)
                print("Thanks for using the Bookstore app. Goodbye!")
                break
            elif confirm == "no":
                print("Returning to main menu...")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        elif choice == 5:
            confirm = input("Would you like to buy a book? (Yes/No): ").strip().lower()
            if confirm == "yes":
                keyword = input("Enter the name of the book you want to buy: ").strip().lower()
                found = False
                for book in booklist:
                    if keyword == book[0].strip().lower():
                        print(f"You selected: {book[0]} by {book[1]}")
                        print(f"Price: ${float(book[4]):.2f}")
                        found = True
                        break
                if not found:
                    print("Sorry, that book is not available.")
            elif confirm == "no":
                print("Returning to main menu...")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        elif choice == 6:
            confirm = input("Would you like to rent a book? (Yes/No): ").strip().lower()
            if confirm == "yes":
                keyword = input("Enter the name of the book you want to rent: ").strip().lower()
                found = False
                for book in booklist:
                    if keyword == book[0].strip().lower():
                        try:
                            duration = int(input("Enter the number of days to rent: "))
                            daily_price = float(book[4]) * 0.25
                            total = daily_price * duration
                            print(f"You selected: {book[0]} by {book[1]}")
                            print(f"Rental duration: {duration} days")
                            print(f"Daily rental price: ${daily_price:.2f}")
                            print(f"Total rental cost: ${total:.2f}")
                            found = True
                            break
                        except ValueError:
                            print("Invalid duration. Please enter a number.")
                            found = True
                            break
                if not found:
                    print("Sorry, that book is not available.")
            elif confirm == "no":
                print("Returning to main menu...")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        elif choice == 7:
            save_booklist_to_desktop(booklist)

if __name__ == "__main__":
    main()