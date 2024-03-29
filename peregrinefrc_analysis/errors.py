class AuthenticationError(Exception):
    def __init__(self, response):
        message = (
            f"Authentication Error [Status {response.status_code}]: {response.text}"
        )
        super().__init__(message)


class MissingAccessTokenError(Exception):
    def __init__(self, message):
        super().__init__(message)
