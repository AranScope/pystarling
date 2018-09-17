import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

get_address_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]


class Address(object):
    """ Service to interact with a customer address"""

    def __init__(self, options):
        """
        Creates an instance of the address client

        :param options: application config
        """
        self.options = options

    def get_addresses(self, access_token):
        """
        Retrieves a customer's address

        :param access_token: the oauth bearer token
        :return: the json response dict
        """
        type_validation([access_token], get_address_parameter_definition)
        url = "{api_url}/api/v1/addresses".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))
