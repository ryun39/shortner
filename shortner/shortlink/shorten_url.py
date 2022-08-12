

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def uri_validator(x):
    try:
        result = urlparse(x)
        print(result)
        print(all([result.scheme, result.netloc, result.path]))
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

def make_shorten():
    # val = URLValidator(verify_exists=False)
    # try:
    #     val('http://www.google.com')
    # except ValidationError as e:
    #     print(e)

    return "test_url@.com"


    # a = 'http://www.cwi.nl:80/%7Eguido/Python.html'
    # b = '/data/Python.html'
    # c = 532
    # d = u'dkakasdkjdjakdjadjfalskdjfalk'
    # print(uri_validator(a))
    # print(uri_validator(b))
    # print(uri_validator(c))
    # print(uri_validator(d))
