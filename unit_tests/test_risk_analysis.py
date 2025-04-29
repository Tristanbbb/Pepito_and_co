
import unittest

import app_config
from src.functions import get_risk_level

class BaseClientTests(unittest.TestCase):

    def setUp(self):
        app_config.INCREASED_RISK_SCORE_THRESHOLD = 50
        app_config.SUSPICIOUS_CERT_PROVIDERS = ["Let's Encrypt"]

    def test_risk_level_low(self):
        risk = get_risk_level(abuse_confidence_scores=[20],cert_provider='Google Trust Services')
        self.assertEqual("LOW",risk)

    def test_risk_level_medium(self):
        risk = get_risk_level(abuse_confidence_scores=[20], cert_provider="Let's Encrypt")
        self.assertEqual("MEDIUM", risk)

    def test_risk_level_high(self):
        risk = get_risk_level(abuse_confidence_scores=[100], cert_provider="Let's Encrypt")
        self.assertEqual("HIGH", risk)

    # SCORE_ERROR is the value returned by AbuseIPDBClient.get_abuse_confidence_score when there is any issue.
    # Checking if it doesn't make get_risk_level fail
    def test_risk_level_score_error(self):
        risk = get_risk_level(abuse_confidence_scores=[60,20,"SCORE_ERROR"], cert_provider='Google Trust Services')
        self.assertEqual("MEDIUM", risk)

    # SCORE_ERROR is the value returned by AbuseIPDBClient.get_abuse_confidence_score when there is any issue.
    # Checking if it doesn't make get_risk_level fail
    def test_risk_level_only_score_error(self):
        risk = get_risk_level(abuse_confidence_scores=["SCORE_ERROR","SCORE_ERROR"], cert_provider='Google Trust Services')
        self.assertEqual("LOW", risk)
