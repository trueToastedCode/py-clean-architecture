from src.interface_adapters.gateways.custom_error.custom_error import CustomError

from src.enterprise_business_rules.book import build_book

def test_e_book():
    Book = build_book(CustomError)

    def make_catch_book(*args, **kwargs):
        try:
            return Book(*args, **kwargs)
        except Exception as e:
            return e

    result = make_catch_book(None)
    assert isinstance(result, CustomError)
    assert str(result) == 'Invalid book title'
    assert result.code == 400

    result = make_catch_book('')
    assert isinstance(result, CustomError)
    assert str(result) == 'Invalid book title'
    assert result.code == 400

    result = make_catch_book(123)
    assert isinstance(result, CustomError)
    assert str(result) == 'Invalid book title'
    assert result.code == 400

    result = make_catch_book('Dummy title')
    assert isinstance(result, Book)
    assert result.title == 'Dummy title'

if __name__ == '__main__':
    test_e_book()
