import json
import re

from models.search_node import SearchNode


class SearchDatabase:
    __root_node: SearchNode

    def __init__(self):
        """
        The search database is made of search nodes to accelerate the search time.
        See https://en.wikipedia.org/wiki/Trie for more information
        """
        self.__root_node = SearchNode()

    def index_word_list(self, word_list: list[str]) -> None:
        """
        Index a complete list of words in the database
        """
        for word in word_list:
            search_key = SearchDatabase.sanitize_search_key(word)
            self.index_word(word, search_key)

    def index_word(self, word: str, search_key: str) -> None:
        """
        Index one word in the database
        """
        node = self.__root_node
        for letter in search_key:
            if not node.children.get(letter):
                node.children[letter] = SearchNode()
            node = node.children[letter]
            node.add_word(word.lower())

    def search(self, word: str) -> str:
        """
        Search a word in the database
        """
        search_key = SearchDatabase.sanitize_search_key(word)
        node = self.__root_node
        for letter in search_key:
            if not node.children.get(letter):
                return []
            node = node.children.get(letter)
        return node.get_words()

    def to_dict(self) -> dict:
        """
        Export the database into a dictionary
        """
        return SearchDatabase.node_to_dict(self.__root_node, {})

    def to_file(self, file_path: str) -> None:
        """
        Export the database into a file
        """
        db_dict = self.to_dict()
        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(db_dict, fp)

    def from_txt_file(self, file_path: str):
        """
        Index a database from a txt file containing a list of word separated by a \n
        """
        with open(file_path, "r", encoding="utf-8") as fp:
            word_list = fp.read().splitlines()
        self.index_word_list(word_list)
        return self

    @staticmethod
    def node_to_dict(node: SearchNode, node_dict: dict) -> dict:
        """
        Export a search node to a dictionary
        """
        for letter in node.children:
            node_dict[letter] = SearchDatabase.node_to_dict(
                node.children.get(letter), {})
        node_dict["words"] = node.get_words()
        return node_dict

    @staticmethod
    def sanitize_search_key(word: str) -> str:
        """
        Sanitize the search key. It is used before indexing a 
        word in the database or before searching a word into the database
        """
        return re.sub(r'(\W|\d)+', '_', word).lower()
