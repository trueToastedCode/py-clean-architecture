from src.interface_adapters.gateways.book_respository.book_repository_gateway import BookRepositoryGateway

from src.application_business_rules.add_book import build_uc_add_book

def test_uc_add_book():
    class DummyBookRepository(BookRepositoryGateway):
        def __init__(self):
            self.__validate_add = None

        def set_validate_add(self, validate_add):
            self.__validate_add = validate_add

        def add(self, book_info: dict):
            self.__validate_add(book_info)

    dummy_book_repository = DummyBookRepository()
    book_info = {'title': 'Dummy title'}

    def validate_add(_book_info: dict):
        assert _book_info == book_info
    dummy_book_repository.set_validate_add(validate_add)
    uc_add_book = build_uc_add_book(dummy_book_repository)
    uc_add_book(book_info)

if __name__ == '__main__':
    test_uc_add_book()
