import logging
from models.search_database import SearchDatabase
from providers.provider import Provider

WORD_LIST_FILE="../data/word_list.txt"

class SearchDatabaseProvider(Provider):
    """
    Provides the search database
    """
    @staticmethod
    def provide() -> SearchDatabase:
        logging.info("Loading database...")
        search_database = SearchDatabase().from_txt_file(WORD_LIST_FILE)
        logging.info("Database loaded !")
        return search_database
