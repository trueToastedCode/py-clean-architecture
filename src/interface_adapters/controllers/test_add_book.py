from src.interface_adapters.gateways.custom_error.custom_error import CustomError

from src.interface_adapters.controllers.add_book import make_c_add_book

def test_c_add_book():
    book_info = {'title': 'Dummy title'}

    validate_uc_add_book = None
    def uc_add_book(*args, **kwargs):
        validate_uc_add_book(*args, **kwargs)
    c_add_book = make_c_add_book(CustomError, uc_add_book)

    def validate_uc_add_book(_book_info: dict):
        assert _book_info == book_info
        raise Exception('Dummy message')
    validate_uc_add_book = validate_uc_add_book
    result = c_add_book(book_info)
    assert isinstance(result, dict)
    assert result.get('status') == 500
    assert result.get('result') == 'Unknown error'

    def validate_uc_add_book(_book_info: dict):
        assert _book_info == book_info
        raise CustomError('Dummy message', 400)
    validate_uc_add_book = validate_uc_add_book
    result = c_add_book(book_info)
    assert isinstance(result, dict)
    assert result.get('status') == 400
    assert result.get('result') == 'Dummy message'

    def validate_uc_add_book(_book_info: dict):
        assert _book_info == book_info
    validate_uc_add_book = validate_uc_add_book
    result = c_add_book(book_info)
    assert isinstance(result, dict)
    assert result.get('status') == 201
    assert result.get('result') is None

if __name__ == '__main__':
    test_c_add_book()
