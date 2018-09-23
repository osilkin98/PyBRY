from urllib.request import urlopen
from urllib.error import URLError
from json import loads, dumps
from pybry.constants import LBRY_API_RAW_JSON_URL


def get_lbry_api_function_docs(url=LBRY_API_RAW_JSON_URL):
    """ Scrapes the given URL to a page in JSON format to obtain the documentation for the LBRY API

    :param str url: URL to the documentation we need to obtain,
     pybry.constants.LBRY_API_RAW_JSON_URL by default
    :return: List of functions retrieved from the `url` given
    :rtype: list
    """

    try:
        # Grab the page content
        docs_page = urlopen(url)

        # Read the contents of the actual url we grabbed and decode them into UTF-8
        contents = docs_page.read().decode("utf-8")

        # Return the contents loaded as JSON
        return loads(contents)

        # If we get an exception, simply exit
    except URLError as UE:
        print(UE)

    except Exception as E:
        print(E)

    return []
