# API Documentation : https://docs.abuseipdb.com/#check-endpoint

import unittest
from src.AbuseIPDBClient import AbuseIPDBClient
# To run : python3 -m unittest test_api_key_manager.py

class AbuseIPDBClientTest(unittest.TestCase):

    def setUp(self):
        self.my_abuseIPDBClient = AbuseIPDBClient(api_key_id='API_KEY_ABUSEIPDB')

    # Warning: this test consumes AbuseIPDB API calls
    def test_get_abuse_confidence_score(self):
        abuse_confidence_score = self.my_abuseIPDBClient.get_abuse_confidence_score(ip_param='118.25.6.39')
        self.assertEqual(0,abuse_confidence_score)

    # Problem with IP. We catch the exception and return "SCORE_ERROR"
    def test_get_abuse_confidence_score_ip_problem(self):
        abuse_confidence_score = self.my_abuseIPDBClient.get_abuse_confidence_score(ip_param='118..6.39')
        self.assertEqual("SCORE_ERROR", abuse_confidence_score)