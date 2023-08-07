class SearchNode:
    children: dict
    __words: list[str]

    def __init__(self):
        """
        A search node is constituted of :
        - children that are a dictionary in the form {"<letter>" : SearchNode}
        - words that are the recolted words for the path from the root
        """
        self.children: dict[str, SearchNode] = {}
        self.__words = []

    def add_word(self, word: str) -> None:
        """
        Called to add a word in the word list of the SearchNode.
        """
        self.__words.append(word)

    def get_words(self) -> list[str]:
        """
        Gets the word_list associated with the node
        """
        return self.__words
