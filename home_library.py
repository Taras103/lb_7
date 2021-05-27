class HomeLibrary:
    books = {}
    __count = 0

    def __init__(self, info_book={'autor': '',
                                  'name': '',
                                  'edition': '',
                                  'genr': '',
                                  'year': ''}):
        self.books[self.__count] = info_book
        self.__count += 1

    def __str__(self):
        return str(self.books)

    def get_book(self, index):
        try:
            return self.books[index]
        except KeyError:
            return None

    def get_size(self):
        return self.__count

    def add_book(self, book={'autor': '',
                             'name': '',
                             'edition': '',
                             'genr': '',
                             'year': ''}):
        self.books[self.__count] = book
        self.__count += 1

    def remove_book(self, index):
        del self.books[index]
        self.__count -= 1
        self.books[index] = self.books[self.__count]
        del self.books[self.__count]


book_1 = {
    'autor': 'autor 1',
    'name': 'name 1',
    'edition': 'edition 1',
    'genr': 'genr 1',
    'year': 'year 1',
}
book_2 = {
    'autor': 'autor 2',
    'name': 'name 2',
    'edition': 'edition 2',
    'genr': 'genr 2',
    'year': 'year 2',
}
book_3 = {
    'autor': 'autor 3',
    'name': 'name 3',
    'edition': 'edition 3',
    'genr': 'genr 3',
    'year': 'year 3',
}
book_4 = {
    'autor': 'autor 4',
    'name': 'name 4',
    'edition': 'edition 4',
    'genr': 'genr 4',
    'year': 'year 4',
}

books_h = HomeLibrary(info_book=book_1)
books_h.add_book(book_2)
books_h.add_book(book_3)
books_h.add_book(book_4)
print(books_h)
books_h.remove_book(index=1)
print(books_h)
print(books_h.get_size())
