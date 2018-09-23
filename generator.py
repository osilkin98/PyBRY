from urllib.request import urlopen
from urllib.error import URLError
from json import loads, dumps
from pybry.constants import LBRY_API_RAW_JSON_URL


def get_lbry_api_function_docs(url=LBRY_API_RAW_JSON_URL):

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
        return None

    except Exception as E:
        print(E)
        return None
