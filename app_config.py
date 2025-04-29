import os

# Configuration variables

# Server configuration
USING_LOCAL_SERVER = True # If True, then you need to configure PATH_TO_SERVER and SERVER_NAME below
PATH_TO_SERVER = "{}/certstream-server-go_1.7.0_linux_amd64".format(os.path.join(os.path.dirname(os.path.abspath(__file__)),'certstream_server')) # If Windows, escape backlslash (\\) and add ".exe"
PRINT_SERVER_LOGS = True # Will or will not print the server logs on the standard output

# Domain configuration
MY_DOMAIN = 'www' # The name of the domain to which potentially suspicious copycats will be compared.

# Abuse IPDB configuration
ABUSEIPDB_API_BASE_URL = 'https://api.abuseipdb.com/api/v2/check'
API_KEY_ID = 'API_KEY_ABUSEIPDB' # ID of the API Key stored in the .env file (needs the Python dotenv library, simulating environment variable locally)

# Risk analysis configuration
LEVENSHTEIN_DISTANCE = 1 # Domains are flagged as suspicious if the Levenshtein distance if part of their name is distant by LEVENSHTEIN_DISTANCE from ours.
SUSPICIOUS_CERT_PROVIDERS = ["Let's Encrypt"] # List of TLS cert providers that we consider suspicious.
ISSUER_ATTRIBUTES_TO_RETRIEVE = ['C','CN','O'] # List of issuer attributes we want to retrieve from the certstream message.
INCREASED_RISK_SCORE_THRESHOLD = 50 # If the IPDB abuse confidence score is over this value (inclusive),
                                    # then the risk is considered one rank higher (for instance going from LOW to MEDIUM)

# Log configuration
LOGFILE_SUSPICIOUS_DOMAINS = "{}/suspicious_domains.log".format(os.path.join(os.path.dirname(os.path.abspath(__file__)),'logs'))
LOG_MODE = "Write" # "Write" or "Append". Be careful, picking "Write" will erase the previous data.
PRINT_SUSPICIOUS_DOMAINS_LOGS = True # True : print logs both to the log file "LOGFILE_SUSPICIOUS_DOMAINS" and to the standard output
                  # False: print logs only to the log file "LOGFILE_SUSPICIOUS_DOMAINS"