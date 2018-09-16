from starling.entities.account import Account
from starling.entities.address import Address
from starling.entities.card import Card
from starling.entities.contact import Contact
from starling.entities.customer import Customer
from starling.entities.mandate import Mandate
from starling.entities.oauth import OAuth
from starling.entities.payment import Payment
from starling.entities.savingsgoals import SavingsGoals
from starling.entities.transaction import Transaction
from starling.entities.whoami import WhoAmI


class Starling(object):
    """ facade to dispatch operations to services """

    def __init__(self, options):
        """
        create an instance of the starling client
        :param options: configuration parameters
        """

        defaults = {
            "api_url": "https://api.starlingbank.com",
            "oauth_url": "https://oauth.starlingbank.com",
            "client_id": "",
            "client_secret": ""
        }

        self.config = {**defaults, **options}

        self.whoami = WhoAmI(self.config)
        self.customer = Customer(self.config)
        self.account = Account(self.config)
        self.address = Address(self.config)
        self.transaction = Transaction(self.config)
        self.payment = Payment(self.config)
        self.mandate = Mandate(self.config)
        self.contact = Contact(self.config)
        self.card = Card(self.config)
        self.savings_goals = SavingsGoals(self.config)
        self.oauth = OAuth(self.config)

    def get_me(self, access_token=None):
        """
        gets the customer uuid and permissions corresponding to the access token passed

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.whoami.get_me(access_token)

    def get_customer(self, access_token=None):
        """
        gets the customer's details

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.customer.get_customer(access_token)

    def get_account(self, access_token=None):
        """
        gets the customer's account details

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.account.get_account(access_token)

    def get_balance(self, access_token=None):
        """
        gets the customer's balance

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.account.get_balance(access_token)

    def get_addresses(self, access_token=None):
        """
        gets the customer's addresses (current and previous)

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.address.get_addresses(access_token)

    def get_transactions(self, from_date, to_date, source, access_token=None):
        """
        gets the customer's transaction history

        :param from_date: filter transactions after this date. _format: yyyy-mm-dd (optional,
                          defaults to most recent 100 transactions)
        :param to_date: filter transactions before this date. _format: yyyy-mm-dd (optional,
                        defaults to current date if not provided)
        :param source: the transaction type (e.g. faster payments, mastercard).
                       if not specified, results are not filtered by source.
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.transaction.get_transactions(access_token, from_date, to_date, source)

    def get_transaction(self, transaction_id, source, access_token=None):
        """
        gets the full details of a single transaction

        :param transaction_id: the unique transaction id
        :param source: the transaction type (e.g. faster payments, mastercard).
                       if not specified, only generic transaction information will be returned.
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.transaction.get_transaction(access_token, transaction_id, source)

    def list_mandates(self, access_token=None):
        """
        gets the customer's current direct-debit mandates

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.mandate.list_mandates(access_token)

    def get_mandate(self, mandate_id, access_token=None):
        """
        gets a specific direct-debit mandate

        :param mandate_id: the unique mandate id
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.mandate.get_mandate(access_token, mandate_id)

    def delete_mandate(self, mandate_id, access_token=None):
        """
        gets the customer's current direct-debit mandates

        :param mandate_id: the unique mandate id
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.mandate.delete_mandate(access_token, mandate_id)

    def list_scheduled_payments(self, access_token=None):
        """
        lists the customer's scheduled payments

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.payment.list_scheduled_payments(access_token)

    def make_local_payment(self, destination_account_uid, reference, amount, currency="GBP", access_token=None):
        """
        makes a payment on behalf of the customer to another uk bank account using the _faster _payments network

        :param destination_account_uid: the account identifier of the recipient
        :param reference: the payment reference, max. 18 characters
        :param amount: the amount to be send
        :param currency: the currency, optional, defaults to "GBP"
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.payment.make_local_payment(access_token, destination_account_uid, reference, amount, currency)

    def get_contacts(self, access_token=None):
        """
        gets the customer's contacts (payees)

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.contact.get_contacts(access_token)

    def get_contact_account(self, contact_id, access_token=None):
        """
        gets a specific contact (payee)

        :param contact_id: the contact's id
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.contact.get_contact_account(access_token, contact_id)

    def create_contact(self, name, account_number, sort_code, customer_id="", account_type="UK_ACCOUNT_AND_SORT_CODE",
                       access_token=None):
        """
        _creates a contact (payee) for the customer

        :param name: the name of the new contact
        :param account_number: the contact's bank account number
        :param sort_code: the contact's sort code
        :param customer_id: the customer's id
        :param account_type: the account type (domestic or international), optional and defaults to
                            "UK_ACCOUNT_AND_SORT_CODE".
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used.
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.contact.create_contact(access_token, name, account_type, account_number, sort_code, customer_id)

    def delete_contact(self, contact_id, access_token=None):
        """
        _deletes a contact (payee) for the customer

        :param contact_id: the contact's id
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.contact.delete_contact(access_token, contact_id)

    def list_savings_goals(self, access_token=None):
        """
        gets a list of the customer's savings goals

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.savings_goals.list_savings_goals(access_token)

    def get_savings_goal(self, savings_goal_id, access_token=None):
        """
        gets a specific savings goal

        :param savings_goal_id:
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.savings_goals.get_savings_goal(access_token, savings_goal_id)

    def add_money_to_savings_goal(self, savings_goal_id, transaction_id, amount, currency="GBP", access_token=None):
        """
        add money to a specific savings goal

        :param savings_goal_id: the savings goal's id
        :param transaction_id: a transaction id for this transaction
        :param amount: an amount in minor unit
        :param currency: the currency unit
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.savings_goals.add_money_to_savings_goal(
            access_token,
            savings_goal_id,
            transaction_id,
            amount,
            currency
        )

    def create_savings_goal(self, savings_goal_id, name, target_amount, base64_encoded_photo, currency="GBP",
                            target_currency="GBP", access_token=None):
        """
        _create a new savings goal

        :param savings_goal_id: the savings goal's id, generate one if creating a goal
        :param name: the name of the new contact
        :param target_amount: the target amount in minor units (e.g. 1234 => £12.34)
        :param base64_encoded_photo: base64 encoded image to associate with the goal. (optional)
        :param currency: the currency of the savings goal. defaults to "GBP"
        :param target_currency: the target currency, also defaults to "GBP"
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.savings_goals.create_savings_goal(access_token, savings_goal_id, name, currency, target_amount,
                                                      target_currency, base64_encoded_photo)

    def delete_savings_goal(self, savings_goal_id, access_token=None):
        """
        _deletes specific direct debit mandate

        :param savings_goal_id: the savings goal's id
        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """
        if access_token is None:
            access_token = self.config["access_token"]

        return self.savings_goals.delete_savings_goal(access_token, savings_goal_id)

    def get_card(self, access_token=None):
        """
        gets the customer's card

        :param access_token: the oauth bearer token. if not specified, the access_token on the options object is used
        :return: the http request promise
        """

        if access_token is None:
            access_token = self.config["access_token"]

        return self.card.get_card(access_token)

    def get_access_token(self, authorization_code):
        """
        exchanges the authorization code for an access token

        :param self:
        :param authorization_code: the authorization code, acquired from the user agent after the
                                  user authenticates with starling
        :return: the http request promise
        """

        return self.oauth.get_access_token(authorization_code)

    def refresh_access_token(self, refresh_token):
        """
        exchanges the authorization code for an access token

        :param refresh_token: the oauth refresh token, used to claim a new access token when the access token
                             expires. a new refresh token is also returned
        :return:
        """
        return self.oauth.refresh_access_token(refresh_token)
