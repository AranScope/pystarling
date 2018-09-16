import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

make_local_payment_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "destinationAccountUid", "validations": ("required", str)},
    {"name": "reference", "validations": ("required", str)},
    {"name": "amount", "validations": ("required", str)},
    {"name": "currency", "validations": ("optional", str)}
]

list_scheduled_payments_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]


class Payment(object):
    """ Service to interact with a customer's payments """

    def __init__(self, options):
        """
        Creates an instance of the payment service

        :param options: application config
        """
        self.options = options

    def make_local_payment(self, access_token, destination_account_uid, reference, amount, currency):
        """
        Makes a payment on behalf of the customer to another UK bank account using the Faster Payments network

        :param access_token: the oauth bearer token
        :param destination_account_uid:
        :param reference: the payment reference, max. 18 characters
        :param amount: the amount to be send
        :param currency: the currency, optional, defaults to "GBP"
        :return: the http request promise
        """
        type_validation([access_token, destination_account_uid, reference, amount, currency],
                        make_local_payment_parameter_definition)
        url = "{api_url}/api/v1/payments/local".format(api_url=self.options["api_url"])
        logging.debug("POST {url}".format(url=url))
        return request.post(url, headers=default_headers(access_token), data={
            "destinationAccountUid": destination_account_uid,
            "payment": {
                "amount": amount,
                "currency": currency
            },
            "reference": reference
        })

    def list_scheduled_payments(self, access_token):
        """
        Lists the customer's scheduled payments

        :param access_token: the oauth bearer token
        :return: the http request promise
        """
        type_validation([access_token], list_scheduled_payments_parameter_definition)
        url = "{api_url}/api/v1/payments/scheduled".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))
