import json
from exceptions.api_response_exception import APIResponseException


class AutoCompleteResponse:
    data: list[str]

    def __init__(self, data: list[str]):
        if not isinstance(data, list):
            raise APIResponseException(
                "Response of autocomplete should have been a list.")
        self.data = data[0:4] # Response only returns 4 words
        self.data.sort() # The response returns sorted items

    def to_bytes(self) -> bytes:
        """
        Transforms the response into bytes
        """
        return json.dumps(self.data).encode("utf-8")
    
    def to_list(self) -> list:
        """
        Returns the response as a list
        """
        return self.data
