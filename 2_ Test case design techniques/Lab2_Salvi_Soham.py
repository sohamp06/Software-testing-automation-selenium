#: Name: Salvi Patel
#: Name: Soham Patel
#: Date: June 4, 2023
#: Program name: book_finder
#: Description: This program allows users to add books to their reading list, store the information in a CSV file.


#: Importing csv file
import csv


def adding_book():
    #: Prompting the user to enter the title of the book they want to add
    book = input("Please enter a title of the book: ")
    #: Prompting the user to enter the author of the book
    author = input("Please enter the author's name of the book: ")
    #: Prompting the user to enter the date of publication of the book
    year_of_publication = input("Please enter a publication date of the book: ")
    #: Append the details of book to the .csv file
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book, author, year_of_publication])
    #:  Print the message to verify the book is added to the csv file
    print("Book added successfully!")


def all_books():
    #: Print the books which are in the .csv file
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Book: {}, Author: {}, Date of Publish: {}\n".format(row[0], row[1], row[2]))


def book_search():
    #: Prompt the user to enter the title of book they want to find
    title = input("Enter the book title to search: ")
    found = False
    #: Search for the book which the user entered title
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3 and row[0].lower() == title.lower():
                print("Book: {}, Author: {}, Date of Publish: {}".format(row[0], row[1], row[2]))
                found = True
                break
    #: If the book does not found in the list print an error message
    if not found:
        print("The book you are trying to find is not in the list!")


def main():
    while True:
        #: Print 4 choices to the user which they want to perform
        print("Menu:\n")
        print("1. Add a book")
        print("2. View the list of books")
        print("3. Find a book")
        print("4. Exit")
        #: Ask the user to enter a number between 1 - 4 (Choices)
        choice = input("Please enter a number between 1 to 4: ")

        if choice == '1':
            adding_book()
        elif choice == '2':
            all_books()
        elif choice == '3':
            book_search()
        elif choice == '4':
            print("Program executed successfully.")
            break
        else:
            #: If a user enters a number out of the range then print an error message
            print("ERROR! You must select a number between 1 to 4.")


main()
