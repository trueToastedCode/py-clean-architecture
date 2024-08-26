from src.interface_adapters.gateways.custom_error.custom_error_gateway import CustomErrorGateway

class MyCustomError(CustomErrorGateway):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.__code = code

    @property
    def code(self) -> int:
        return self.__code

    @staticmethod
    def default_process_error(e: Exception) -> dict:
        if isinstance(e, MyCustomError):
            return {'status': e.code, 'result': str(e)}
        return {'status': 500, 'result': 'Unknown error'}
