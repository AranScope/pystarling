import logging
from starling.utils.http import default_headers
import starling.utils.request as request
from starling.utils.validator import type_validation, ParameterDefinition

get_account_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]

get_balance_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]


class Account(object):
    """ Service to interact with a customer's account """

    def __init__(self, options):
        """
        Creates an instance of the account client

        :param options: application config
        """
        self.options = options

    def get_account(self, access_token):
        """
        Retrieves a customer's account

        :param access_token: the oauth bearer token
        :return: the http request promise
        """
        type_validation([access_token], get_account_parameter_definition)
        url = "{api_url}/api/v1/accounts".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def get_balance(self, access_token):
        """
        Retrieves the customer's balance

        :param access_token: the oauth bearer token
        :return: the http request promise
        """
        type_validation([access_token], get_balance_parameter_definition)
        url = "{api_url}/api/v1/accounts/balance".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))
