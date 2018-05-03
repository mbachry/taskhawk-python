class RetryException(Exception):
    """
    Special exception that does not log an exception when it is received.
    This is a retryable error.
    """
    pass


class LoggingException(RetryException):
    """
    An exception that allows passing additional logging info.
    """
    def __init__(self, message, extra=None):
        super().__init__(message)
        self.extra = extra


class ValidationError(Exception):
    """
    Message failed JSON schema validation
    """
    pass


class ConfigurationError(Exception):
    """
    There was some problem with settings
    """
    pass


class TaskNotFound(Exception):
    """
    No task was found that can handle the given message. Ensure that you call `taskhawk.RegisterTask`.
    """
    pass
