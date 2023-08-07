import re

from exceptions.api_validation_exception import APIValidationException


class SanitizeService:
    @staticmethod
    def sanitize_path(url_path):
        """
        Sanitize the path of a request arriving to the server
        """
        parsed_url = {}
        match = re.fullmatch(
            r"^((?P<path>\/[^\?\#\n]*)(\?(?P<params>(?P<first_param>[^\#\?\&\=\n]+(=[^\#\?\&\=\n]*)*)(\&(?P<param_more>[^\#\?\&\=\n]+(=[^\#\?\&\=\n]*)*))*))?(\#(?P<tag>[^\#\?\n]+)?)?)?$",
            url_path)
        if not match:
            raise APIValidationException("Invalid path pattern")
        if match.group('path'):
            parsed_url['path'] = match.group('path')
        if match.group('params'):
            params = {}
            # WARN : we parse until 10 params in the request
            splitted_params = match.group('params').split("&", 10)
            for splitted_param in splitted_params:
                key, value = splitted_param.split("=", 1)
                params[key] = value
            parsed_url['params'] = params
        return parsed_url

    @staticmethod
    def sanitize_query(query):
        """
        Sanitize the query sent to the server (allowing only alpha chars)
        """
        return re.sub(r'(\W|\d)+', '_', query).lower()
