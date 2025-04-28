import config

def get_list_of_issuer_attributes_to_retrieve():
    list_of_attributes = []
    try:
        list_of_attributes = config.ISSUER_ATTRIBUTES_TO_RETRIEVE
    # If for some reason there is a problem with the retrieval from the config above,
    # then we return a list of default attributes (the ones specified in the exercise instructions
    except Exception as exception_instance:
        print(exception_instance)
        list_of_attributes = ['C','CN','O']
    return list_of_attributes

# Class centralizing operations on the json received from certstream
class CertstreamMessage:
    def __init__(self,message: dict):
        self.message = message
        self.domain_list = self.get_domain_list()
        self.list_of_issuer_attributes = get_list_of_issuer_attributes_to_retrieve()
        self.issuer_attributes = {} # Filled upon calling get_issuer_attributes(). We do it only if suspicious domains are found, for performance reasons.

    def get_domain_list(self):
        try:
            domain_list = self.message["data"]["leaf_cert"]["all_domains"]
            return domain_list
        except Exception as exception_instance:
            print(f"CertstreamMessage Error: {exception_instance}")
            return []

    # Setting values to the self.issuer_attributes dictionary. Called only if suspicious domains are found.
    def set_issuer_attributes(self):
        for attribute in self.list_of_issuer_attributes:
            try:
                self.issuer_attributes[attribute] = self.message["data"]["leaf_cert"]["issuer"][attribute]
            except KeyError:
                print(f"CertstreamMessage Warning: attribute '{attribute}' not found in the certstream message")
                self.issuer_attributes[attribute] = 'UNKNOWN'

    # Passed to the Logger for logging
    def get_issuer_attributes_as_string(self):
        res_string = '('
        for attribute in self.issuer_attributes:
            res_string = res_string + f'/{attribute}={self.issuer_attributes[attribute]}'
        res_string += ')'
        return res_string