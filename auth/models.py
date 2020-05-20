import hashlib
import os
import re

from auth.exceptions import EmailValidationError, PasswordValidationError, FullNameValidationError,\
    PhoneValidationError, InvalidPasswordError, ConfirmationError
from notify import db

class Account:

    def __init__(self, data):
        self._validate_all(data)
        self.id = data['id'] if 'id' in data else None
        self._email = data['email']
        self._password = self._generate_hash(data['password'])
        self._full_name = data['full_name'] if 'full_name' in data else None
        self._phone = data['phone'] if 'phone' in data else None
        self.registration_date = data['registration_date'] if 'registration_date' in data else None

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._validate_email(email)
        self._email = email

    @property
    def password(self) -> bytes:
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        print('1')
        try:
            self._validate_password(password)
        except Exception as e:
            print(e)
        print('res')
        print('2')
        self._password = self._generate_hash(password)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self._validate_full_name(full_name)
        self._full_name = full_name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._validate_phone(phone)
        self._phone = phone

    @staticmethod
    def _validate_email(email: str) -> None:
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            raise EmailValidationError

    @staticmethod
    def _validate_password(password: str) -> None:
        if type(password) != bytes:
            if not (len(password) > 10 and all(re.search(symbol, password) for symbol in ('[A-Z]', '[0-9]', '[a-z]'))):
                raise PasswordValidationError

    @staticmethod
    def _validate_full_name(full_name: str):
        if not re.match(r'^([a-z]|[A-Z]|\s){0,30}$', full_name):
            raise FullNameValidationError

    @staticmethod
    def _validate_phone(phone: str):
        if not re.match(r'^[+]?[\s\-\d\(\)]{0,28}$', phone):
            raise PhoneValidationError

    def _validate_all(self, data) -> None:
        self._validate_email(data['email'])
        self._validate_password(data['password'])

    @staticmethod
    def _generate_hash(password, salt=os.urandom(8)) -> bytes:
        if type(password) == bytes:
            return password

        pw_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000,
            dklen=8
        )
        return salt + pw_hash

    def check_password(self, password):
        salt = self.password[:8]
        if self._password == self._generate_hash(password, salt):
            return True
        else:
            raise InvalidPasswordError

    async def create(self, pool):
        return await db.create_account(pool, self)

    async def update_personal_info(self, pool, data):
        self.full_name = data['full_name']
        self.phone = data['phone']
        return await db.update_account(pool, self)

    async def delete(self, pool, data):
        if data['confirm'] != 'DELETE':
            raise ConfirmationError
        self.check_password(data['password'])
        return await db.delete_account(pool, self.id)