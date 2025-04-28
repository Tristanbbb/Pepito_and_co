import config
import Levenshtein
from src.AbuseIPDBClient import AbuseIPDBClient

class DomainAnalysis:
    # my_domain is the domain we are trying to safeguard. domains_list is the list of domains to compare to my_domain, and analyse
    def __init__(self,my_domain: str,domains_list: list, levenshtein_distance: int):
        self.my_domain = my_domain # The domain we are trying to safeguard
        self.all_domains = domains_list # All domains passed as argument, including non-suspicious ones
        self.levenshtein_distance = levenshtein_distance # The levenshtein distance used to consider if a domain is suspiciously close to ours
        self.suspicious_domains_list = self.get_suspicious_domains() # We retrieve only the domains that are suspicious, to avoid unnecessary analysis
        self.suspicious_domains_and_scores_dict = {} # We call match_scores_to_suspicious_domains to fill this dict, when necessary (suspicious domains are found)

    # Uses levenshtein distance to return a list of suspicious domains
    def get_suspicious_domains(self):
        suspicious_domains = []
        for domain in self.all_domains:
            # We split the domains and analyse each part of the domain individually.
            # For instance mail.toto.com gets split in ['mail,'toto','com'] and each word is compared to our domain
            # There are probably better ways to do the analysis but it's a good simple way to do it for a start.
            parts = domain.split(".")
            for part in parts:
                if Levenshtein.distance(self.my_domain, part) <= self.levenshtein_distance:
                    suspicious_domains.append(domain)
        return suspicious_domains

    # Fills the suspicious_domains_and_scores_dict dictionary with domain and score : {"toto.com": 42 ...}
    # This method is the one that makes calls to the AbuseIPDB API
    # Use it only when necessary (suspicious domains found) to reduce API calls
    def match_scores_to_suspicious_domains(self):
        try:
            abuse_ipdb_client = AbuseIPDBClient(api_key_id=config.API_KEY_ID)
        except Exception as exception_instance:
            # If we can't initialize the AbuseIPDB Client, we still want to record the log
            # Info about scores will be missing but it's better than not recording the info at all
            print("DomainAnalysis Error: couldn't initialize AbuseIPDBClient.")
            for domain in self.suspicious_domains_list:
                self.suspicious_domains_and_scores_dict[domain] = "SCORE_ERROR"
        else:
            # Only if we successfully instanciate abuse_ipdb_client do we then try to retrieve the scores
            for domain in self.suspicious_domains_list:
                abuse_confidence_score = abuse_ipdb_client.get_abuse_confidence_score(domain_param=domain)
                self.suspicious_domains_and_scores_dict[domain] = abuse_confidence_score

    # Passed to the Logger for logging
    def get_domains_and_scores_as_string(self):
        res = ''
        for element in self.suspicious_domains_and_scores_dict:
            res += f"{element}({self.suspicious_domains_and_scores_dict[element]})"
        return res