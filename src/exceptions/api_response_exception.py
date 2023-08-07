class APIResponseException(Exception):
    """
    Raised when an API exception occurs
    """
    def __init__(self, message: str):
        super().__init__(message)
