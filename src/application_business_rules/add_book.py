from src.enterprise_business_rules.enterprise_business_rules import Book

def build_uc_add_book(book_repository):
    def uc_add_book(book_info: dict):
        book = Book(**book_info)
        book_repository.add({
            'title': book.title
        })

    return uc_add_book
