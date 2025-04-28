
import unittest
from src.BaseClient import BaseClient
# To run : python3 -m unittest test_api_key_manager.py

class BaseClientTests(unittest.TestCase):

    def setUp(self):
        # Testing with another API so that we don't burn AbuseIPDB credits.
        self.my_BaseClient = BaseClient("https://api.thecatapi.com/v1/images/search")

    def test_http_request(self):
        res = self.my_BaseClient.http_request(method='GET')
        res_json = res.json()
        # We check if there is a 'url' key in the result. If yes, the call worked properly.
        self.assertTrue(res_json[0]['url'])


