import logging

from starling.utils import request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

get_transactions_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "fromDate", "validations": ("optional", str)},
    {"name": "toDate", "validations": ("optional", str)},
    {"name": "source", "validations": ("optional", str)}
]

get_transaction_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "transactionId", "validations": ("required", str)},
    {"name": "source", "validations": ("optional", str)}
]


def transaction_source(source):
    source_map = {
        "MASTER_CARD": "/mastercard",
        "FASTER_PAYMENTS_IN": "/fps/in",
        "FASTER_PAYMENTS_OUT": "/fps/out",
        "DIRECT_DEBIT": "/direct-debit"

    }

    if source in source_map:
        return source_map[source]
    else:
        return ""


class Transaction(object):
    """ Service to interact with a customer's transactions """

    def __init__(self, options):
        """
        Creates an instance of the transaction service

        :param options: application config
        """
        self.options = options

    def get_transactions(self, access_token, from_date, to_date, source):
        """
        Makes a payment on behalf of the customer to another UK bank account using the Faster Payments network

        :param access_token: the oauth bearer token
        :param from_date: filter transactions after this date. Format: YYYY-MM-DD
        :param to_date: filter transactions before this date. Format: YYYY-MM-DD
        :param source: the transaction type (e.g. faster payments, mastercard)
                       if not specified, results are not filtered by source
        :return: the json response dict
        """

        type_validation([access_token, from_date, to_date, source],
                        get_transactions_parameter_definition)

        url = "{api_url}/api/v1/transactions{source}".format(
            api_url=self.options["api_url"], source=transaction_source(source))

        logging.debug("GET {url}".format(url=url))

        return request.get(url, headers=default_headers(access_token), params={
            "from": from_date,
            "to": to_date
        })

    def get_transaction(self, access_token, transaction_id, source):
        """
        Makes a payment on behalf of the customer to another UK bank account using the Faster Payments network

        :param access_token: the oauth bearer token
        :param transaction_id: the unique transaction ID
        :param source: the transaction type (e.g. faster payments, mastercard)
                       if not specified, only generic transaction information is provided
        :return: the json response dict
        """

        type_validation([access_token, transaction_id, source],
                        get_transaction_parameter_definition)

        url = "{api_url}/api/v1/transactions{source}/{id}".format(
            api_url=self.options["api_url"], source=transaction_source(source), id=transaction_id)

        logging.debug("GET {url}".format(url=url))

        return request.get(url, headers=default_headers(access_token))
