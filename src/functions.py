

import app_config

# File containing functions that I didn't think needed to be in a class


# See README.md to see the risk analysis policy
def get_risk_level(abuse_confidence_scores, cert_provider):
    # We need to sanitize the list, keeping only integers, because sometimes we have "SCORE_ERROR" values
    abuse_confidence_scores = [element for element in abuse_confidence_scores if isinstance(element,int)]
    risk_ranks = {
        0: "LOW",
        1: "MEDIUM",
        2: "HIGH"
    }
    current_risk_rank = 0
    # "if abuse_confidence_score", because it can be empty (in case we only have "SCORE_ERRORS"
    if abuse_confidence_scores and max(abuse_confidence_scores) >= app_config.INCREASED_RISK_SCORE_THRESHOLD:
        current_risk_rank += 1
    if cert_provider in app_config.SUSPICIOUS_CERT_PROVIDERS:
        current_risk_rank += 1
    return risk_ranks[current_risk_rank]
