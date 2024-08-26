def make_c_add_book(CustomError, _add_book):
    def c_add_book(book_info: dict) -> dict:
        try:
            _add_book(book_info)
        except Exception as e:
            return CustomError.default_process_error(e)
        return {'status': 201, 'result': None}

    return c_add_book
