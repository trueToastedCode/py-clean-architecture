from src.interface_adapters.gateways.custom_error.custom_error import CustomError

from src.application_business_rules.application_business_rules import uc_add_book

from src.interface_adapters.controllers.add_book import make_c_add_book

c_add_book = make_c_add_book(CustomError, uc_add_book)
