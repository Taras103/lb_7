class Book:
    """Class book"""

    def __init__(self, autor, name, edition, genr, year):
        self.autor = autor
        self.name = name
        self.edition = edition
        self.genr = genr
        self.year = year

    def get_list(self):
        """Return list of values"""
        return [
            self.autor,
            self.name,
            self.edition,
            self.genr,
            self.year
        ]

    def __str__(self):
        """Return object in string"""
        return f'{self.autor}\n{self.name}\n{self.edition}\n{self.genr}\n{self.year}'
