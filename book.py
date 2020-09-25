class Book:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def set_book(self):
        pass

    def get_book(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self):
        self.__name = name

    @property
    def author(self):
        return self.author

    @author.setter
    def author(self):
        self.__author = author

    @property
    def year(self):
        return self.__year

    @year.setter
    def name(self):
        self.__year = year
