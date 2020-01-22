

import re, ipaddress
from functools import wraps

from .exceptions import UnsupportedLanguageError, InvalidGeolocationError


def validate_args(func):
    """Utility to validate the different parameters"""
    
    @wraps(func)
    def wrapper(self, **kwargs):
        to_validate = kwargs.keys()

        if 'ip' in to_validate:
            try:
                ipaddress.ip_address(kwargs['ip'])
            except ValueError:
                raise

        if 'cidr' in to_validate:
            try:
                ipaddress.ip_network(kwargs['cidr'])
            except ValueError:
                raise
        
        if 'lang' in to_validate:
            lang = kwargs['lang']
            if lang not in self.SUPPORTED_LANGUAGES:
                raise UnsupportedLanguageError(f"BigDataCloud currently doesn't support `localityLanguage`, {lang}.")
        
        if 'email_address' in to_validate:
            email = kwargs['email_address']
            if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                raise ValueError(f"{email} is not a valid email address")

        if 'utc_reference' in to_validate:
            utc_ref = kwargs['utc_reference']
            try:
                int(utc_ref)
            except (ValueError, TypeError, OverflowError):
                raise ValueError(f"{utc_ref} is not a valid unix timestamp")

        if 'number' in to_validate:
            number = kwargs['number']
            try:
                [int(i) for i in number]
            except (ValueError):
                raise ValueError(f"{number} is not a valid phone number.\
                                 The phone number should be without hyphens or spaces")
        
        if 'latitude' in to_validate:
            lat = kwargs['latitude']
            if not re.match(r"^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$", lat):
                raise InvalidGeolocationError(f"{lat} is not a valid WGS 84 reference system latitude coordinate")

        if 'longitude' in to_validate:
            long = kwargs['longitude']
            if not re.match(r"^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$", long):
                raise InvalidGeolocationError(f"{long} is not a valid WGS 84 reference system longitude coordinate")

        return func(self, **kwargs)
    return wrapper