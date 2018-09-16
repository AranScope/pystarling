import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

list_savings_goals_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]

get_savings_goals_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "savingsGoalId", "validations": ("required", str)}
]

delete_savings_goals_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "savingsGoalId", "validations": ("required", str)}
]

create_savings_goals_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "savingsGoalId", "validations": ("required", str)},
    {"name": "name", "validations": ("required", str)},
    {"name": "currency", "validations": ("required", str)},
    {"name": "targetAmount", "validations": ("optional", str)},
    {"name": "targetCurrency", "validations": ("optional", str)},
    {"name": "base64EncodedPhoto", "validations": ("optional", str)}
]

add_money_to_savings_goal_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "savingsGoalId", "validations": ("required", str)},
    {"name": "transactionId", "validations": ("required", str)},
    {"name": "amount", "validations": ("required", int)}
]


class SavingsGoals(object):
    """ Service to interact with a customer's savings goals """

    def __init__(self, options):
        """
        Creates an instance of the savings goals service

        :param options: application config
        """
        self.options = options

    def list_savings_goals(self, access_token):
        """
        Gets a lists of the customer's savings goals

        :param access_token: the oauth bearer token
        :return: the http request promise
        """
        type_validation([access_token], list_savings_goals_parameter_definition)
        url = "{api_url}/api/v1/savings-goals".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def get_savings_goal(self, access_token, savings_goal_id):
        """
        Gets a specific savings goal

        :param access_token: the oauth bearer token
        :param savings_goal_id: the savings goal's ID
        :return: the http request promise
        """
        type_validation([access_token, savings_goal_id], get_savings_goals_parameter_definition)
        url = "{api_url}/api/v1/savings-goals/{goal_id}".format(
            api_url=self.options["api_url"], goal_id=savings_goal_id)
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def create_savings_goal(self, access_token, savings_goal_id, name, currency,
                            target_amount, target_currency, base64_encoded_photo):
        """
        Creates a savings goal

        :param access_token: the oauth bearer token
        :param savings_goal_id: the saving's goal's ID
        :param name: the name of the savings goal
        :param currency: the currency of the savings goal
        :param target_amount: the target amount in minor units (e.g. 1234 => £12.34)
        :param target_currency: the target currenct, defaults to 'GBP'
        :param base64_encoded_photo: base64 encoded image to associate with the goal. (optional)
        :return: the http request promise
        """

        type_validation([access_token, savings_goal_id, name, currency,
                         target_amount, target_currency, base64_encoded_photo],
                        create_savings_goals_parameter_definition)

        url = "{api_url}/api/v1/savings-goals/{goal_id}".format(
            api_url=self.options["api_url"], goal_id=savings_goal_id)

        logging.debug("PUT {url}".format(url=url))

        return request.put(url, headers=default_headers(access_token), data={
            "name": name,
            "currency": currency,
            "target": {
                "targetAmount": target_amount,
                "targetCurrency": target_currency
            },
            "base64EncodedPhoto": base64_encoded_photo
        })

    def delete_savings_goal(self, access_token, savings_goal_id):
        """
        Deletes a specific savings goal

        :param access_token: the oauth bearer token
        :param savings_goal_id: the savings goal's ID
        :return: the http request promise
        """
        type_validation([access_token, savings_goal_id], delete_savings_goals_parameter_definition)
        url = "{api_url}/api/v1/savings-goals/{goal_id}".format(
            api_url=self.options["api_url"], goal_id=savings_goal_id)
        logging.debug("DELETE {url}".format(url=url))
        return request.delete(url, headers=default_headers(access_token))

    def add_money_to_savings_goal(self, access_token, savings_goal_id, transaction_id, amount, currency):
        """
        Add money to a specific savings goal

        :param access_token: the oauth bearer token
        :param savings_goal_id: the saving's goal's ID
        :param transaction_id:
        :param amount: an amount in minor unit
        :param currency: the currency of the savings goal

        :return: the http request promise
        """

        type_validation([access_token, savings_goal_id, transaction_id, amount, currency],
                        add_money_to_savings_goal_parameter_definition)

        url = "{api_url}/api/v1/savings-goals/{goal_id}/add-money/{transaction_id}".format(
            api_url=self.options["api_url"], goal_id=savings_goal_id, transaction_id=transaction_id)

        logging.debug("PUT {url}".format(url=url))

        return request.put(url, headers=default_headers(access_token), data={
            "amount": {
                "currency": currency,
                "targetCurrency": currency
            }
        })
