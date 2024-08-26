class CustomErrorGateway(Exception):
    @staticmethod
    def default_process_error(e: Exception) -> dict:
        raise NotImplementedError
