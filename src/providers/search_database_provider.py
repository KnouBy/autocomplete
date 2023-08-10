import logging
from models.search_database import SearchDatabase
from providers.provider import Provider


class SearchDatabaseProvider(Provider):
    """
    Provides the search database
    """
    @staticmethod
    def provide() -> SearchDatabase:
        logging.info("Loading database...")
        search_database = SearchDatabase().from_txt_file("../data/word_list.txt")
        logging.info("Database loaded !")
        return search_database
