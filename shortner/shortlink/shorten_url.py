
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urllib.parse import urlparse
import pyshorteners


def uri_validator(x):
    try:
        result = urlparse(x)
        print(result)
        print(all([result.scheme, result.netloc, result.path]))
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

def make_shorten():
    API_KEY = "bbae968b2337d147f0d1f9086409352110b55c4a"
    type_bitly = pyshorteners.Shortener(api_key=API_KEY)
    short_url = type_bitly.bitly.short('https://www.google.com')
    
    print("The Shortened URL is: " + short_url)
    return short_url