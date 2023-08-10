from models.search_database import SearchDatabase


def test_add_word():
    db = SearchDatabase()
    db.index_word("toto", "toto")
    assert db.search("t")[0] == "toto"


def test_add_word_with_different_key():
    db = SearchDatabase()
    db.index_word("TOTO", "tata")
    assert db.search("ta")[0] == "TOTO"


def test_search_longer_word():
    db = SearchDatabase()
    db.index_word("tata", "tata")
    assert db.search("tataio") == []


def test_add_multiple_words():
    db = SearchDatabase()
    db.index_word_list(["toto", "tata", "tutu", "foo", "bar"])
    autocomplete_propositions = db.search("t")
    autocomplete_propositions.sort()
    assert autocomplete_propositions == ["tata", "toto", "tutu"]


def test_db_from_txt():
    db = SearchDatabase().from_txt_file("../data/word_list.txt")
    autocomplete_propositions = db.search("c")
    autocomplete_propositions.sort()
    assert autocomplete_propositions[0:4] == [
        "cloud computing",
        "computer network defense analysis",
        "computer network defense infrastructure support",
        "computer security incident"
    ]


def test_index_large_db():
    db = SearchDatabase().from_txt_file("../data/words_alpha.txt")
    autocomplete_propositions = db.search("parti")
    autocomplete_propositions.sort()
    assert autocomplete_propositions[0] == "parti"
