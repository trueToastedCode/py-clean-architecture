from src.interface_adapters.gateways.book_respository.book_repository_gateway import BookRepositoryGateway

def make_memory_book_repository(CustomError):
    class MemoryBookRepository(BookRepositoryGateway):
        def __init__(self):
            self.__books = []

        def add(self, book_info: dict):
            if book_info['title'] in self.__books:
                raise CustomError('Book already exists in repository', 409)
            self.__books.append(book_info)

    return MemoryBookRepository
