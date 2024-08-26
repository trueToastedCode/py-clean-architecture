from src.interface_adapters.gateways.custom_error.custom_error import CustomError

from src.enterprise_business_rules.book import build_book

Book = build_book(CustomError)
