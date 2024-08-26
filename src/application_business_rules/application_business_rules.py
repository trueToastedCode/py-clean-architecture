from src.interface_adapters.gateways.book_respository.book_respository import book_repository

from src.application_business_rules.add_book import build_uc_add_book

uc_add_book = build_uc_add_book(book_repository)
