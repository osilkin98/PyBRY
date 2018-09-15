import requests
import json

def pretty_print_POST(request):
    """ Prints a prepared request to give the user info as to what they're sending

    :param request.PreparedRequest request: PreparedRequest object to be printed
    :return: Nothing
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body,
    ))


