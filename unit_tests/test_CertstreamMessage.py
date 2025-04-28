# API Documentation : https://docs.abuseipdb.com/#check-endpoint

import unittest

import src.config
from src.CertstreamMessage import CertstreamMessage, get_list_of_issuer_attributes_to_retrieve
from unit_tests import message_samples
# To run : python3 -m unittest test_api_key_manager.py

class CertstreamMessageTest(unittest.TestCase):
    def setUp(self):
        src.config.ISSUER_ATTRIBUTES_TO_RETRIEVE=['C','CN','O','TOTO']

    def test_standard_message(self):
        my_certstream_message = CertstreamMessage(message_samples.standard_message)
        my_certstream_message.set_issuer_attributes()
        self.assertEqual(['mail.prophesyclothing.com'],my_certstream_message.domain_list)
        self.assertEqual("(/C=US/CN=R10/O=Let's Encrypt/TOTO=UNKNOWN)", my_certstream_message.get_issuer_attributes_as_string())

    def test_message_without_domains(self):
        my_certstream_message = CertstreamMessage(message_samples.message_without_domains)
        self.assertEqual([],my_certstream_message.domain_list)

    def test_message_with_missing_issuer_org(self):
        my_certstream_message = CertstreamMessage(message_samples.message_with_missing_issuer_org)
        my_certstream_message.set_issuer_attributes()
        self.assertEqual("(/C=US/CN=R10/O=UNKNOWN/TOTO=UNKNOWN)", my_certstream_message.get_issuer_attributes_as_string())