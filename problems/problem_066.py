# Write a class that meets these requirements.
#
# Name:       Book
#
# Required state:
#    * author name, a string
#    * title, a string
#
# Behavior:
#    * get_author: should return "Author: «author name»"
#    * get_title:  should return "Title: «title»"
#
# Example:
#    book = Book("Natalie Zina Walschots", "Hench")
#
#    print(book.get_author())  # prints "Author: Natalie Zina Walschots"
#    print(book.get_title())   # prints "Title: Hench"
#
# There is pseudocode availabe for you to guide you


class Book
    # method initializer method with required state
    def __init__(self, author, title):
        self.author = author
        self.title = title
        # parameters author and title
        # set self.author = author
        # set self.title = title

    # method get_author(self)
    def get_author(self):
        # returns "Author: " + self.author
        return "Author: " + self.author

    # method get_title(self)
    def get_title(self):
        return "Title: " + self.title
        # returns "Title: " + self.title

book1 = Book("Natalie Zina Walschots", "Hench")

print(book1.get_author())  # prints "Author: Natalie Zina Walschots"
print(book1.get_title())   # prints "Title: Hench"
