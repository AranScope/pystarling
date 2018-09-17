import logging

import starling.utils.request as request
from starling.errors import ClientConfigurationError
from starling.utils.http import oauth_headers
from starling.utils.validator import type_validation

refresh_token_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]

authorization_code_parameter_definition = [
    {"name": "authorizationCode", "validations": ("required", str)}
]

ACCESS_TOKEN_GRANT_TYPE = "authorization_code"
REFRESH_TOKEN_GRANT_TYPE = "refresh_token"


class OAuth(object):
    """Service to interact with the oauth endpoint"""

    def __init__(self, options):
        """
        Creates a instance of the oauth service

        :param options: application config
        """
        self.options = options

    def get_access_token(self, authorization_code):
        """
        Exchanges the authorization code for an access token

        :param authorization_code: the authorization code, acquired from the user agent after the
                                   user authenticates with starling
        :return: the json response dict
        """
        type_validation([authorization_code], authorization_code_parameter_definition)

        return self.get_oauth_token({
            "code": authorization_code,
            "grant_type": ACCESS_TOKEN_GRANT_TYPE,
            "client_id": self.options["client_id"],
            "client_secret": self.options["client_secret"],
            "redirect_uri": self.options["redirect_uri"]
        })

    def refresh_access_token(self, refresh_token):
        """
        Exchanges the authorization code for an access token

        :param refresh_token: the oauth refresh token, used when the access token
                              expires to claim a new access token.
        :return: the json response dict
        """
        type_validation([refresh_token], refresh_token_parameter_definition)

        return self.get_oauth_token({
            "refresh_token": refresh_token,
            "grant_type": REFRESH_TOKEN_GRANT_TYPE,
            "client_id": self.options["client_id"],
            "client_secret": self.options["client_secret"],
        })

    def get_oauth_token(self, params):
        """
        Gets the access token from the starling oauth endpoint

        :param params: the query params passed to the oauth endpoint as per the oauth spec
        :return: the json response dict
        """
        if not self.options["client_id"]:
            raise ClientConfigurationError("clientId is not configured")

        if not self.options["client_secret"]:
            raise ClientConfigurationError("clientSecret is not configured")

        url = "{url}/oauth/access-token".format(url=self.options["oauth_url"])
        logging.debug("POST {url}".format(url=url))
        return request.post(url, headers=oauth_headers(), params=params)
