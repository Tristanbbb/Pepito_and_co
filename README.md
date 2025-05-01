
# Introduction
This programs uses the Levenshtein distance to spot suspicious domains, get their AbuseIPDB confidence score,
and information about the certificate issuer.

# Running as a docker image
You can run the app as a docker image but there is a limit with the buffer size, making the app miss certs. However, using a keyword that doesn't retrieve too many certs, like "pepito", seems sufficient to mitigate the issue.

To run as a docker image:
- Get the docker image: `docker pull triton12/pepito_typosquatting:latest`
- Copy and paste app_config.py where you want and edit the values as you want
- Create a suspicious_domains.log file where ever you want.
- run the docker image:
    `docker run -v /path/to/your/app_config.py:/app/app_config.py -v /path/to/your/suspicious_domains.log:/app/logs/suspicious_domains.log -e API_KEY_ABUSEIPDB=your_api_key -it triton12/pepito_typosquatting`

# Running locally
- `git clone https://github.com/Tristanbbb/Pepito_and_co.git`
- `pip install -r requirements.txt`
- Create a ".env" file at the root folder of the project and add a line like "API_KEY_ABUSEIPDB=your_key"
- Install the server in the certstream_server folder if you want to be able to run the certstream server locally.
- In app_config.py, update the SERVER_NAME variable will the name of the server (including ".exe" if on Windows).
- In app_config.py, update the MY_DOMAIN variable to the name we are trying to protect ("pepito" for instance). You can also tweak several other behaviors of the program in the app_config.py file.

### Installing the server locally
The certstream.calidog.io server hasn't been working at all since I've started working on this project, so I have had to run the server locally.
- Download a precompiled version of [certstream-server-go](https://github.com/d-Rickyy-b/certstream-server-go)
- Put it in the certstream_server folder and edit app_config.py with the name of your server in the SERVER_NAME variable
- Create a config.yml file in the certstream_server folder (or keep the default file)
- (Linux) Make the server executable (chmod u+x ./certstream-server-go_1.7.0_linux_amd64)

# Project structure

- certstream_server: contains the files needed to run the certstream server locally
  - certstream-server-go_1.7.0_linux_amd64: the server executable
  - config.yml: the server's configuration
  - run_server.py: the Python code to run the server
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
- root
  - app_config.py: contains most of the configuration of the program
  - README.md
  - requirements.txt: needed python libraries.
  - .env (removed on Github): simulated env variables with the python dotenv lib. API_KEY_ABUSEIPDB=my_secret_api_key
  - .gitignore: removes .env because the API key is secret. You need to create your own .env file to run the program.
  - .dockerignore: we remove the .env and unit tests from the docker image

# Risk analysis
The risk analysis algorithm is very simple. We have 3 risk levels : LOW, MEDIUM, HIGH.
As long as at least one suspicious domain is found in a cert, we have a LOW risk.
The risk is bumped up one rank in any of those cases (and bumped up two ranks if both are true):
- At least one abuse confidence score is above the threshold configures in app_config.py (INCREASED_RISK_SCORE_THRESHOLD variable)
- If the certificate provider is considered as a suspicious one (also set in app_config.py, variable SUSPICIOUS_CERT_PROVIDERS)

# Potential improvements
- Custom handling of more exception types, creating my own Exception classes.
- A better risk analysis function
- Automatically check if we receive heartbeats from the certstream.calidog server, else run the server locally.
- In the unit_tests, testing also the exception behaviors.
- Log exceptions in a separate log file?
- Make the server as a class