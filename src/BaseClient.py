import requests

class BaseClient(object):
    def __init__(self, base_url: str, headers: dict = {}):
        self.base_url = base_url
        self.headers = headers

    def http_request(self, method: str, params: dict = {}):
        try:
            response = None
            if method == 'GET':
                response = requests.get(url=self.base_url, headers=self.headers, params=params)
                response.raise_for_status()
            return response
        except requests.exceptions.RequestException as exception_instance:
            print(f"BaseClient request error: {exception_instance}")
            raise
        except Exception as exception_instance:
            print(f"BaseClient error: {exception_instance}")
            raise

