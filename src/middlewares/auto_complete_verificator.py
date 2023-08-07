from exceptions.api_validation_exception import APIValidationException
from services.sanitize_service import SanitizeService


class AutoCompleteVerificator:
    """
    Verifies the request, params for the /autocomplete endpoint 
    """
    @staticmethod
    def verify(request, params : dict):
        if not params or not params.get("query"):
            raise APIValidationException("Query not present in the params...\
                                          Please retry with a query param")
        query = params.get("query")
        sanitized_params = {"query": SanitizeService.sanitize_query(query)}
        return request, sanitized_params
