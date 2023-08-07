from models.search_database import SearchDatabase
from providers.provider import Provider


class SearchDatabaseProvider(Provider):
    """
    Provides the search database
    """
    @staticmethod
    def provide() -> SearchDatabase:
        return SearchDatabase().from_txt_file("../data/word_list.txt")
