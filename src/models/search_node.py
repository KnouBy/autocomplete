class SearchNode:
    def __init__(self):
        """
        A search node is constituted of :
        - children that are a dictionary in the form {"<letter>" : SearchNode}
        - words that are the recolted words for the path from the root
        """
        self.children: dict[str, SearchNode] = {}
        self.words = []

    def add_word(self, word: str) -> None:
        """
        Called to add a word in the word list of the SearchNode.
        """
        self.words.append(word)
