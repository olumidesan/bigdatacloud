

class UnsupportedLanguageError(AttributeError):
    """Raised when an unsupported language is supplied"""
    pass

class InvalidGeolocationError(ValueError):
    """Raised when an invalid latitude or longitude is supplied"""
    pass
