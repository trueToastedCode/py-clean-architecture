def build_book(CustomError):
    class Book:
        def __init__(self, title: str):
            if not (isinstance(title, str) and title):
                raise CustomError('Invalid book title', 400)
            self.__title = title

        @property
        def title(self):
            return self.__title

    return Book
