import json
from exceptions.api_response_exception import APIResponseException


class AutoCompleteResponse:
    data: list[str]

    def __init__(self, data: list[str]):
        if not isinstance(data, list):
            raise APIResponseException(
                "Response of autocomplete should have been a list.")
        self.data = data

    def to_bytes(self):
        """
        Transforms the response into bytes
        """
        return json.dumps(self.data).encode("utf-8")
