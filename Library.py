class Library:
    """Class Library"""
    books = {}
    __count = 0

    def __init__(self, book=None):
        if 'Book' in str(type(book)):
            self.books[self.__count] = book
            self.__count += 1

    def __str__(self):
        """Return jbfect in string"""
        text = ''

        for k, v in self.books.items():
            text += str(k) + ': \n'
            text += '\t' + v.autor + '\n'
            text += '\t' + v.name + '\n'
            text += '\t' + v.edition + '\n'
            text += '\t' + v.genr + '\n'
            text += '\t' + v.year + '\n'

        return text

    def get_book(self, index):
        """Return object book"""
        try:
            return self.books[index]
        except KeyError:
            return None

    def get_size(self):
        """Return size library"""
        return self.__count

    def add_book(self, book):
        """Add a book to library"""
        self.books[self.__count] = book
        self.__count += 1

    def remove_book(self, index):
        """Remove the book from the library"""
        del self.books[index]
        self.__count -= 1
        try:
            self.books[index] = self.books[self.__count]
        except KeyError:
            pass
        else:
            del self.books[self.__count]

    def search_book(self, element):
        """Searcing book in library"""
        for key, book in self.books.items():
            if element in book.name or book.edition or book.autor:
                return self.books[key]

        return None
