import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

list_mandates_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]

delete_mandate_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "mandateId", "validations": ("required", str)}
]


class Mandate(object):
    """Service to interact with a customer's transactions"""

    def __init__(self, options):
        """
        Create a new transaction service

        :param options: application config
        """
        self.options = options

    def list_mandates(self, access_token):
        """
        Gets a list of the customer's current direct debit mandates

        :param access_token: the oauth bearer token
        :return: the http request promise
        """
        type_validation([access_token], list_mandates_parameter_definition)
        url = "{api_url}/api/v1/direct-debit/mandates".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def get_mandate(self, access_token, mandate_id):
        """
        Gets a specific direct debit mandates

        :param access_token: the oauth bearer token
        :param mandate_id: the unique mandate ID
        :return: the http request promise
        """
        type_validation([access_token], list_mandates_parameter_definition)
        url = "{api_url}/api/v1/direct-debit/mandates/{mandate_id}".format(
            api_url=self.options["api_url"], mandate_id=mandate_id)
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def delete_mandate(self, access_token, mandate_id):
        """
        Deletes specific direct debit mandate

        :param access_token: the oauth bearer token
        :param mandate_id: the unique mandate ID
        :return: the http request promise
        """
        type_validation([access_token, mandate_id], delete_mandate_parameter_definition)
        url = "{api_url}/api/v1/direct-debit/mandates/{mandate_id}".format(
            api_url=self.options["api_url"], mandate_id=mandate_id)
        logging.debug("DELETE {url}".format(url=url))
        return request.delete(url, headers=default_headers(access_token))
