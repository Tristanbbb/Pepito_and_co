
# Introduction
This programs uses the Levenshtein distance to spot suspicious domains, get their AbuseIPDB confidence score,
and information about the certificate issuer.

# Running as a docker image 
### (under construction)
You can run the app as a docker image but there are some problems, notable with buffer size, making the app miss certs.
To run it as a docker image anyway:
- Get the docker image: `docker pull triton12/pepito_typosquatting:latest`
- Copy and paste app_config.py where you want and edit the values as you want
- run the docker image:
    `docker run -v /your/path/to/config/app_config.py:/app_config.py -e API_KEY_ABUSEIPDB=your_api_key -it triton12/pepito_typosquatting`
- Warning:
  - if too many certs are sent, we get "Not providing client with cert because client's buffer is full. The client can't keep up". This remains to be fixed and doesn't happen when the app is run in Pycharm.
  - if ran as a docker image, the suspicious domain alerts will only appear in the terminal and will not be saved in suspicious_domains.log

# Running in Pycharm
- `git clone https://github.com/Tristanbbb/Pepito_and_co.git`
- Open the project in Pycharm
- Click "Create a virtual environment using requirements.txt" or "install requirements" (should pop up at the top of Pycharm)
- Create a ".env" file at the root folder of the project and add a line like "API_KEY_ABUSEIPDB=your_key"
- Install the server locally if certstream.calidog.io doesn't work (see below)
- In app_config.py, update the PATH_TO_SERVER variable will the full path to your server (including ".exe" if on Windows).
- In app_config.py, update the MY_DOMAIN variable to the name we are trying to protect ("pepito" for instance)

### Installing the server locally
The certstream.calidog.io server hasn't been working at all since I've started working on this exercise, so I have had to run the server locally.
- Download a precompiled version of [certstream-server-go](https://github.com/d-Rickyy-b/certstream-server-go)
- Put it in the certstream_server folder and edit app_config.py at the root level with the name of your server in the PATH_TO_SERVER variable
- Create a config.yml file in the certstream_server folder (or keep the default file)
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
  - app_config.py: contains most of the configuration of the program
  - README.mdr
  - requirements.txt: needed python libraries.
  - .env (removed on Github): simulated env variables with the python dotenv lib. API_KEY_ABUSEIPDB=my_secret_api_key
  - .gitignore: removes .env because the API key is secret. You need to create your own .env file to run the program.

# Risk analysis
The risk analysis algorithm is very simple. We have 3 risk levels : LOW, MEDIUM, HIGH.
As long as at least one suspicious domain is found in a cert, we have a LOW risk.
The risk is bumped up one rank in any of those cases (and bumped up two ranks if both are true):
- At least one abuse confidence score is above the threshold configures in app_config.py (INCREASED_RISK_SCORE_THRESHOLD variable)
- If the certificate provider is considered as a suspicious one (also set in app_config.py, variable SUSPICIOUS_CERT_PROVIDERS)

# Potential improvements
- app_config.py => config.yml
- Improver docker image and test it on several envs
- Custom handling of more exception types, creating my own Exception classes.
- A better risk analysis function
- Automatically check if we receive heartbeats from the certstream.calidog server, else run the server locally.
- Warning/exception when we reached the limit of calls to AbuseIPDB with our current plan.
- In the unit_tests, testing also the exception behaviors.
- Log exceptions in a separate log file?
- Make the server as a class