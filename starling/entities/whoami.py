import logging
from starling.utils.http import default_headers
import starling.utils.request as request
from starling.utils.validator import type_validation, ParameterDefinition

get_me_parameter_definition = [
    {"name": "accessToken", "validations": ("required", str)}
]


class WhoAmI(object):
    """ Service to interact with the Who Am I endpoint """

    def __init__(self, options):
        """
        Creates an instance of the who am I client

        :param options: application config
        """
        self.options = options

    def get_me(self, access_token):
        """
        Retrieves the customer UUID and permissions corresponding to the access token passed

        :param access_token: the oauth bearer token
        :return: the http request promise
        """
        type_validation([access_token], get_me_parameter_definition)
        url = "{api_url}/api/v1/me".format(api_url=self.options["api_url"])
        logging.debug("GET {url}".format(url=url))
        return request.get(url, headers=default_headers(access_token))
