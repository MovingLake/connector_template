import requests
import datetime
import os
import structlog

from BaseClient import BaseClient

logger = structlog.get_logger()


class Connector(BaseClient):
    def auth_is_connection_test(self):
        """
        Whether the authentication is a connection test.
        """
        return True

    def auth(self, params: dict) -> dict:
        """
        Implement special auth scheme.
        :param params: Parameters to authenticate from the connector configuration form.
        :return True if the authentication was successful, False otherwise.
        """
        api_key: str = params["api_key"]

        headers = {"X-Api-Key": f"{api_key}"}
        # Try to get units just to test the connection.
        url = "https://newsapi.org/v2/everything?q=movinglake"
        r = requests.get(url, headers=headers)
        if r.status_code > 399:
            raise Exception(
                f"Invalid credentials using url {url} headers {headers}. Status code: {r.status_code}"
            )
        self._cv.http.set_header(headers)
        # Needed if using the url from the configuration JSON.
        self._cv.http.URL_BASE = self._cv.http.URL_BASE_INIT
        
        # Return the headers! For any subsequent call to this API.
        return headers
