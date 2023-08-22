
from controllers.auto_complete_controller import AutoCompleteController
from models.search_database import SearchDatabase


def test_only_4_results_returned_in_response():
    db = SearchDatabase().from_txt_file("../data/words_alpha.txt")
    controller = AutoCompleteController()
    response = controller.get({} , {"query": "a"})
    assert len(response.to_list()) == 4