import config
import certstream
from Logger import Logger
from functions import get_risk_level
from certstream_server.run_server import run_server
from CertstreamMessage import CertstreamMessage
from DomainAnalysis import DomainAnalysis

SUSPICIOUS_DOMAINS_LOGGER = Logger()

def my_callback(message,context):
    global SUSPICIOUS_DOMAINS_LOGGER
    # We are ignoring the other types of messages, such as heartbeats
    if message['message_type'] == "certificate_update":
        try:
            certstream_message = CertstreamMessage(message=message)
            domain_analysis = DomainAnalysis(my_domain=config.MY_DOMAIN,
                                             domains_list=certstream_message.domain_list,
                                             levenshtein_distance=config.LEVENSHTEIN_DISTANCE)
            if domain_analysis.suspicious_domains_list: # If suspicious domains are found
                domain_analysis.match_scores_to_suspicious_domains() # Then we call the AbuseIPDB API to get abuse confidence scores
                certstream_message.set_issuer_attributes() # And we retrieve the issuer attributes
                risk = get_risk_level(abuse_confidence_scores = domain_analysis.suspicious_domains_and_scores_dict.values(),
                                      cert_provider = certstream_message.issuer_attributes['O'])

                # Calling the logger to add a line in the log file, and optionally print the row to the terminal
                SUSPICIOUS_DOMAINS_LOGGER.alert(risk_level=risk,
                                                domains_and_scores=domain_analysis.get_domains_and_scores_as_string(),
                                                issuer_attributes=certstream_message.get_issuer_attributes_as_string())
        except Exception as e:
            print(f"Exception in my_callback : {e}")

def on_open():
    print("Connection successfully established!")

def main():
    if config.USING_LOCAL_SERVER:
        try:
            server_proc = run_server()
        except FileNotFoundError:
            print("Error: couldn't find the local Certstream server. Exiting the program")
        else:
            certstream.listen_for_events(my_callback, url='ws://localhost:8080',
                                         skip_heartbeats=True,
                                         on_open=on_open)
    else:
        certstream.listen_for_events(my_callback, url='wss://certstream.calidog.io/',
                                     skip_heartbeats=False,
                                     on_open=on_open)
if __name__ == "__main__":
    try:
        main()
    except Exception as exception_instance:
        print(f"Error : {exception_instance}.")
        print("The program is exiting")
