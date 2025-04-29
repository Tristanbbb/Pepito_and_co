
# API Documentation : https://docs.abuseipdb.com/#check-endpoint

import os
import socket
import requests.exceptions
from src.BaseClient import BaseClient
import app_config
from dotenv import load_dotenv
from pathlib import Path

# Exceptions in this class should not be fatal: we can still log the suspicious domain names, even if we don't have confidence scores for them.
class AbuseIPDBClient(BaseClient):
    def __init__(self, api_key_id, base_url=app_config.ABUSEIPDB_API_BASE_URL):
        super().__init__(base_url=base_url)
        self.api_key_id = api_key_id
        try:
            self.api_key = self.get_api_key_from_dotenv()
            self.headers = {
                "Key": self.api_key
            }
        except KeyError:
            print("AbuseIPDBClient Error: there is a problem with the API key, analysis of the abuse confidence scores will be impossible.")
            raise
        except Exception as e:
            print(e)
            raise

    # Creating a function to retrieve API key, so that we don't hardcore it here.
    def get_api_key_from_dotenv(self):
        envpath = Path(__file__).resolve().parent.parent / '.env'
        load_dotenv(dotenv_path=envpath)
        try:
            api_key = os.environ[self.api_key_id]
            return api_key
        except KeyError:
            print(f"AbuseIPDBClient error: couldn't find an API key with id in the .env file '{self.api_key_id}'")
            raise

    def get_abuse_confidence_score(self, ip_param: str = None, domain_param: str = None):
        try:
            ip = ip_param
            # We need at least an ip or a domain, otherwise we raise an exception
            if not ip_param and not domain_param:
                raise ValueError("Missing ip/domain")
            elif ip_param:
                pass
            else:
                # AbuseIPDB API accepts only ip, so we have to resolve the domains
                ip = socket.gethostbyname(domain_param)

            params = {'ipAddress': ip}
            response = self.http_request(method='GET', params=params)
            response_data = response.json()
            abuse_confidence_score = response_data['data']['abuseConfidenceScore']
            return abuse_confidence_score

        except ValueError as exception_instance:
            if str(exception_instance) == "Missing ip/domain":
                print("AbuseIPDBClient error: check_reputation() needs an ip or a domain name. Both can't be empty.")
            return "SCORE_ERROR"
        except requests.exceptions.RequestException as exception_instance:
            if str(exception_instance).startswith("429"):
                print(f"AbuseIPDBClient error: 429 client error. Daily rate limit for calls to the API has been exceeded.")
            return "SCORE_ERROR"
        except Exception as exception_instance:
            if str(exception_instance) == "[Errno -5] No address associated with hostname":
                print(f"AbuseIPDBClient error when trying 'ip = socket.gethostbyname({domain_param})'. No IP address is associated with the hostname.")
            else:
                print(f"AbuseIPDBClient error : {exception_instance}")
            return "SCORE_ERROR"