import sys


class BaseError(Exception):
    pass


class Error(BaseError):
    pass


class Syntax_Error(Error):
    def __init__(self, *args):
        super().__init__(*args)


def RAISE_ERROR(error: Error):
    pass

