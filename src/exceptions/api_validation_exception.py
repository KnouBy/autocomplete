class APIValidationException(Exception):
    """
    Raised in case of an error in the validation of the request
    """
    def __init__(self, message: str):
        super().__init__(message)
