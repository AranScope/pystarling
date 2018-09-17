import logging

import starling.utils.request as request
from starling.utils.http import default_headers
from starling.utils.validator import type_validation

get_contact_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]

get_contacts_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]

get_contact_account_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "contactId", "validations": ("required", str)}
]

create_contact_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "name", "validations": ("required", str)},
    {"name": "accountNumber", "validations": ("required", str)},
    {"name": "sortCode", "validations": ("required", str)}
]

delete_contact_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)},
    {"name": "contactId", "validations": ("required", str)}
]


class Contact(object):
    """ Service to interact with a customer's customer's contacts (payees)"""

    def __init__(self, options):
        """
        Creates a new contact service

        :param options: application config
        """
        self.options = options

    def get_contact_account(self, access_token: str, contact_id: str):
        """
        Gets a specific contact from the customer's contacts (payees)

        :param contact_id: the id of the contact
        :param access_token: the oauth bearer token
        :return: the json response dict
        """
        type_validation([access_token], get_contact_parameter_definition)
        url = "{api_url}/api/v1/contacts/{contact_id}".format(api_url=self.options["api_url"], contact_id=contact_id)
        print(url)
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def get_contacts(self, access_token):
        """
        Gets the customer's contacts (payees)

        :param access_token: the oauth bearer token
        :return: the json response dict
        """
        type_validation([access_token], get_contacts_parameter_definition)
        url = "{api_url}/api/v1/contacts".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def get_contact_accounts(self, access_token, contact_id):
        """
        Gets a specific contact's (payee) list of accounts

        :param access_token: the oauth bearer token
        :param contact_id: the contact's ID
        :return: the json response dict
        """
        type_validation([access_token, contact_id], get_contact_account_parameter_definition)
        url = "{api_url}/api/v1/contacts/{contact_id}/accounts".format(
            api_url=self.options["api_url"], contact_id=contact_id)
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))

    def create_contact(self, access_token, name, account_number, sort_code):
        """
        Creates a contact (payee) for the customer

        :param access_token: the oauth bearer token
        :param name: the name of the new contact
        :param account_number: the contact's bank account number
        :param sort_code: the contact's sort code
        :return: the json response dict
        """
        type_validation([access_token, name, account_number, sort_code],
                        get_contact_account_parameter_definition)
        url = "{api_url}/api/v1/contacts".format(api_url=self.options["api_url"])
        logging.debug("POST {url}".format(url=url))

        return request.post(
            url,
            headers=default_headers(access_token),
            data={
                "name": name,
                "accountNumber": account_number,
                "sortCode": sort_code
            }
        )

    def delete_contact(self, access_token, contact_id):
        """
        Deletes a specific contact (payee) from the customer's account

        :param access_token: the oauth bearer token
        :param contact_id: the contact's ID
        :return: the json response dict
        """
        type_validation([access_token, contact_id], delete_contact_parameter_definition)
        url = "{api_url}/api/v1/contacts/{contact_id}".format(api_url=self.options["api_url"], contact_id=contact_id)
        logging.debug("DELETE {url}".format(url=url))
        return request.delete(url, headers=default_headers(access_token))
