class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The books present in the library are: ")
        index = 1
        for books in self.books:
            print(f"\t {index}. " + books)
            index += 1

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(
                f"You have issued {bookname}. Please return it before within 30 days.")
            self.books.remove(bookname)
        else:
            print(f"Sorry! {bookname} is not available at this moment.")

    def returnBook(self, bookname):
        print(
            f"Thank you for returning{bookname}. If you want to borrow other books please check the our Book list.")
        self.books.append(bookname)


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithms", "Django", "Clrs", "PythonNotes", "Physics", "Mathematics"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while True:
        welcomeMsg = '''===Welcome to Central Library===
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit a library'''

        print(welcomeMsg)

        a = int(input("Please input the corresponding number to choose the option: "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
            print("\n")

        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())

        elif a == 3:
            centralLibrary.returnBook(student.returnBook())

        elif a == 4:
            print("Thank you for visiting us. Hope you have a great day!!!")
            exit()
        else:
            print("Please enter a valid input")


