class ValidationError(BaseException):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'validation error'


class EmailValidationError(ValidationError):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'email validation error'


class PasswordValidationError(ValidationError):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'password validation error'


class FullNameValidationError(ValidationError):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'full name validation error'


class PhoneValidationError(ValidationError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return 'phone validation error'


class RegistrationError(BaseException):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'registration error'


class EmailRegistrationError(BaseException):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'email is used'


class LoginError(BaseException):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'login error'


class AccountNotFound(LoginError):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'account not found'


class InvalidPasswordError(LoginError):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'invalid password'


class ConfirmationError(LoginError):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'invalid confirmation'
