from models.search_database import SearchDatabase
from providers.provider import Provider


class SearchDatabaseProvider(Provider):
    """
    Provides the search database
    """
    @staticmethod
    def provide():
        return SearchDatabase().from_txt_file("../data/word_list.txt")
