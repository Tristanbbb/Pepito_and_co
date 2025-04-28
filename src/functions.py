import subprocess
from subprocess import DEVNULL

import src.config

# File containing functions that I didn't think needed to be in a class

# To run the server locally
def run_server():
    try:
        # Whether we want to see the server logs in the terminal or not, we have to pass different arguments to subprocess.Popen()
        if src.config.PRINT_SERVER_LOGS:
            server_proc = subprocess.Popen([f'{src.config.SERVER_NAME}'],cwd=src.config.PATH_TO_SERVER)
        else:
            server_proc = subprocess.Popen([f'{src.config.SERVER_NAME}'], cwd=src.config.PATH_TO_SERVER, stdout=DEVNULL, stderr=DEVNULL)
        return server_proc
    except FileNotFoundError as exception_instance:
        print("Error trying to run the server: file not found. Double check config.PATH_TO_SERVER and config.SERVER_NAME")
        print(exception_instance)
        raise FileNotFoundError

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
    if abuse_confidence_scores and max(abuse_confidence_scores) >= src.config.INCREASED_RISK_SCORE_THRESHOLD:
        current_risk_rank += 1
    if cert_provider in src.config.SUSPICIOUS_CERT_PROVIDERS:
        current_risk_rank += 1
    return risk_ranks[current_risk_rank]
