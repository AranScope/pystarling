import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

get_card_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]


class Card(object):
    """ Service to interact with a customer card"""

    def __init__(self, options: dict):
        """
        Creates an instance of the customer's card

        :param options: application config
        """
        self.options = options

    def get_card(self, access_token: str):
        """
        Retrieves a customer's card

        :param access_token: the oauth bearer token
        :return: the json response dict
        """
        type_validation([access_token], get_card_parameter_definition)
        url = "{api_url}/api/v1/cards".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))
