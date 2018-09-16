"""
Errors defined in Starling docs Errors section.
https://developer.starlingbank.com/docs
"""


class BadRequestError(Exception):
    """An exception raised when something is wrong with the request made"""


class UnauthorizedError(Exception):
    """An exception raised when you are not authorized to access the requested data"""


class ForbiddenError(Exception):
    """An exception raised when authentication is failed, usually due to an expired token,
       or attempting to access a resource beyond the scope of the token"""


class NotFoundError(Exception):
    """An exception raised when the requested resource does not exist"""


class InternalServerError(Exception):
    """An exception raised when Starling has an internal server error"""


class TypeValidationError(Exception):
    """An exception raised when a type validation fails"""

    def __init__(self, validation_errors):
        self.validation_errors = validation_errors


class ClientConfigurationError(Exception):
    """Raised when a client is misconfigured"""


class UnhandledStatusCodeError(Exception):
    """Raised when an unexpected status code is received"""
