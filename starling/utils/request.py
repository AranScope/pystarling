"""
The module that represents any HTTP request related logic.
Delegates to the requests library with Starling-specific validation.

Adapted from https://github.com/muyiwaolu/monzo-python/blob/master/monzo/request.py
"""
from json import JSONDecodeError

import requests

from starling.errors import (BadRequestError, UnauthorizedError, ForbiddenError,
                             InternalServerError, NotFoundError, UnhandledStatusCodeError)


def get(url, headers=None, params=None):
    """Sends a GET request to a specified URL
       :param url: The URL to send the request to
       :param headers: The headers to include with the request
       :param params: The data to include with the request
       :rtype: A Dictionary representation of the response
    """
    response = requests.get(url=url, headers=headers, params=params)
    return _validate_response(response)


def post(url, headers=None, params=None, data=None):
    """Sends a POST request to a specified URL
       :param url: The URL to send the request to
       :param headers: The headers to include with the request
       :param params: The data to include with the request
       :rtype: A Dictionary representation of the response
    """
    response = requests.post(url=url, headers=headers, data=data, params=params)
    return _validate_response(response)


def put(url, headers=None, params=None, data=None):
    """Sends a PUT request to a specified URL
       :param url: The URL to send the request to
       :param headers: The headers to include with the request
       :param params: The data to include with the request
       :rtype: A Dictionary representation of the response
    """
    response = requests.put(url=url, headers=headers, data=data, params=params)
    return _validate_response(response)


def delete(url, headers=None, params=None, data=None):
    """Sends a DELETE request to a specified URL
       :param url: The URL to send the request to
       :param headers: The headers to include with the request
       :param params: The data to include with the request
       :rtype: A Dictionary representation of the response
    """
    response = requests.delete(url=url, headers=headers, data=data, params=params)
    return _validate_response(response)


def _validate_response(response):
    """Validate the response and raises any appropriate errors.
       :param response: The response to validate
       :rtype: A Dictionary representation of the response, if no errors occured.
    """

    if response.status_code == 204:
        return {}

    try:
        json_response = response.json()
    except JSONDecodeError:
        json_response = {}

    if response.status_code == 200 or response.status_code == 202:
        return json_response
    if response.status_code == 400:
        raise BadRequestError(json_response["error_description"])
    if response.status_code == 401:
        raise UnauthorizedError(json_response["error_description"])
    if response.status_code == 403:
        raise ForbiddenError(json_response["error_description"])
    if response.status_code == 404:
        raise NotFoundError(json_response["error_description"])
    if response.status_code == 400:
        raise InternalServerError(json_response["error_description"])

    raise UnhandledStatusCodeError(response.status_code)
