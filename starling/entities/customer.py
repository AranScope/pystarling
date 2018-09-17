import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

get_customer_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]


class Customer(object):
    """Service to interact with a customer"""

    def __init__(self, options):
        """
        Creates a instance of the customer client

        :param options: application config
        """
        self.options = options

    def get_customer(self, access_token):
        """
        Gets a customer's details

        :param access_token: the oauth bearer token
        :return: the json response dict
        """
        type_validation([access_token], get_customer_parameter_definition)
        url = "{api_url}/api/v1/customers".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))
