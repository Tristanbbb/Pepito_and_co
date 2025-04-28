
# Introduction
This programs uses the Levenshtein distance to spot suspicious domains, get their AbuseIPDB confidence score,
and information about the certificate issuer.

# Prerequisites
- git clone https://github.com/Tristanbbb/Pepito_and_co.git
- Open the project in Pycharm
- Click "Create a virtual environment using requirements.txt"
- Create a ".env" file at the root folder of the project and add a line like "API_KEY_ABUSEIPDB=your_key"
- Install the server locally if certstream.calidog.io doesn't work (see below)
- In config.py, update the PATH_TO_SERVER variable will the full path to your server (including ".exe" if on Windows).
- In config.py, update the MY_DOMAIN variable to the name we are trying to protect ("pepito" for instance)

### Installing the server locally
The certstream.calidog.io server hasn't been working at all since I've started working on this exercise, so I have had to run the server locally.
- Download a precompiled version of [certstream-server-go](https://github.com/d-Rickyy-b/certstream-server-go)
- Create a config.yml file in the Pepito_and_co/src folder (or keep the default file)
- (Linux) Make the server executable (chmod u+x ./certstream-server-go_1.7.0_linux_amd64)

# Project structure
- src: contains the python files
  - AbuseIPDBClient.py: contains the class calling the AbuseIPDB API
  - BaseClient.py: base class for http requests
  - CertstreamMessages.py: class to represent the interesting parts of the certstream message
  - DomainAnalysis.py: class retrieving the suspicious domains from a certstream message and from which the calls to the AbuseIPDBClient class are made
  - Logger.py: contains the logging logic, including accessing and closing the file
  - functions.py: other functions
  - config.yml: configuration for the locally run certstream server
  - main.py
- unit_tests: contains the unit tests
- logs
  - suspicious_domains.log: contains the log of suspicious domains found.
- .venv (removed on Github): contains the Python virtual environment with the necessary libraries
- files in root
  - config.py: contains most of the configuration of the program
  - README.mdr
  - requirements.txt: needed python libraries.
  - .env (removed on Github): simulated env variables with the python dotenv lib. API_KEY_ABUSEIPDB=my_secret_api_key
  - .gitignore: removes .env because the API key is secret. You need to create your own .env file to run the program.

# Risk analysis
The risk analysis algorithm is very simple. We have 3 risk levels : LOW, MEDIUM, HIGH.
As long as at least one suspicious domain is found in a cert, we have a LOW risk.
The risk is bumped up one rank in any of those cases (and bumped up two ranks if both are true):
- At least one abuse confidence score is above the threshold configures in config.py (INCREASED_RISK_SCORE_THRESHOLD variable)
- If the certificate provider is considered as a suspicious one (also set in config.py, variable SUSPICIOUS_CERT_PROVIDERS)

# Potential improvements
- Containerize with Docker?
- Custom handling of more exception types, creating my own Exception classes.
- A better risk analysis function
- Automatically check if we receive heartbeats from the certstream.calidog server, else run the server locally.
- Warning/exception when we reached the limit of calls to AbuseIPDB with our current plan.
- In the unit_tests, testing also the exception behaviors.
- Log exceptions in a separate log file?
- Make the server as a class