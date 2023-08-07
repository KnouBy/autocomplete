from models.search_database import SearchDatabase
from providers.provider_injector import inject
from providers.search_database_provider import SearchDatabaseProvider
from responses.auto_complete_response import AutoCompleteResponse


class AutoCompleteController:
    """
    Controller for the autocomplete service
    """
    @staticmethod
    @inject(SearchDatabaseProvider)  # Injects the SearchDatabase
    def get(search_db: SearchDatabase, request, params: dict):
        query = params.get("query")
        matched = search_db.search(query)
        response = AutoCompleteResponse(matched)
        return response
