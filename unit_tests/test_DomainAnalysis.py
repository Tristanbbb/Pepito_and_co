
import unittest
from src.DomainAnalysis import DomainAnalysis

class DomainAnalysisTest(unittest.TestCase):
    def setUp(self):
        self.my_domain_analysis = DomainAnalysis(my_domain="pepito",domains_list=['papito.com','rienavoir', 'pepita'],levenshtein_distance=1)

    def test_get_suspicious_domains(self):
        res = self.my_domain_analysis.get_suspicious_domains()
        # This test should return 2 suspicious domains : papito.com and pepita
        self.assertEqual(2,len(self.my_domain_analysis.suspicious_domains_list))
        self.assertIn("papito.com", self.my_domain_analysis.suspicious_domains_list)
        self.assertIn("pepita", self.my_domain_analysis.suspicious_domains_list)

    # Testing that an empty domain list doesn't cause a fatal error.
    def test_empty_domain_list(self):
        empty = DomainAnalysis(my_domain="pepito",domains_list=[],levenshtein_distance=1)
