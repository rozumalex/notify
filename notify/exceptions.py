class ValidationError(BaseException):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'validation error'


class NameValidationError(ValidationError):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'name validation error'
