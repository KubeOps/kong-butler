# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: daisheng
# Email: shawntai.ds@gmail.com


class KongError(Exception):

    def __init__(self, message=None, context=None):
        super(KongError, self).__init__(message)
        self.message = message
        self.context = context


class ResourceNotFoundError(KongError):
    pass


class MethodNotAllowedError(KongError):
    pass


class AuthenticationError(KongError):
    pass


class ServerError(KongError):
    pass


class BadGatewayError(KongError):
    pass


class ServiceUnavailableError(KongError):
    pass


class BadRequestError(KongError):
    pass


class RateLimitExceededError(KongError):
    pass


class MultipleMatchingUsersError(KongError):
    pass


class UnexpectedError(KongError):
    pass


class TokenUnauthorizedError(KongError):
    pass


class ConflictError(KongError):
    pass


class UnsupportedMediaTypeError(KongError):
    pass


error_codes = {
    400: BadRequestError,
    401: AuthenticationError,
    403: AuthenticationError,
    404: ResourceNotFoundError,
    405: MethodNotAllowedError,
    409: ConflictError,
    415: UnsupportedMediaTypeError,
    500: ServerError,
    502: BadGatewayError,
    503: ServiceUnavailableError
}


class UsernameDuplicateError(KongError):
    pass
