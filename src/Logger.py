# Logger.py
from app_config import LOGFILE_SUSPICIOUS_DOMAINS # Location of the log file
from app_config import PRINT_SUSPICIOUS_DOMAINS_LOGS # True if we want to print the logs to the terminal in addition to already adding them to the log file
from app_config import LOG_MODE # "Append" or "Write" ("Write" deletes the old data from the log file!)

class Logger:
    def __init__(self):
        self.print_logs = PRINT_SUSPICIOUS_DOMAINS_LOGS
        try:
            if LOG_MODE == 'Write':
                self.log_file = open(LOGFILE_SUSPICIOUS_DOMAINS,"w")
            elif LOG_MODE == 'Append':
                self.log_file = open(LOGFILE_SUSPICIOUS_DOMAINS, "a")
        except Exception as exception_instance:
            print(f"Logger Error: {exception_instance}")
            raise

    def __del__(self):
        try:
            self.log_file.close()
            print("Log file closed.")
        except AttributeError: # If we have an attribute error, it means the file was not opened in the first place
            pass               # As a result, we can safely ignore the exception

    # Functions that displays and saves the row under the format: [HIGH] pepitoo.com(20),www.pepitoo.com(20)  (/C=US/CN=Let's Encrypt AuthorityX3/O=Let's Encrypt)
    def alert(self,risk_level: str, domains_and_scores: str, issuer_attributes: str):
        alert_message = f"[{risk_level}]  {domains_and_scores} {issuer_attributes}\n"
        if self.print_logs:
            print(alert_message,end='')

        self.log_file.write(alert_message)
        self.log_file.flush() # Flushing each time may not be the best for performance
                              # but this way we don't lose any log in case the program crashes.
