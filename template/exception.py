"""Exceptions when there is a problem with a call to the LBRY daemons."""


def print_request(request):
    """Print a prepared request to give the user info as to what they're sending.

    :param request.PreparedRequest request: PreparedRequest object to be printed
    :return: Nothing
    """
    start = "-----------START-----------"
    req = request.method + " " + request.url
    items = '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items())
    body = request.body
    print(start)
    print(req)
    print(items)
    print()
    print(body)


class LBRYError(Exception):

    def __init__(self, message, response, status_code, request):
        """Exception raised when there is a problem with a call to lbrynet.

        :param str message: Message to Display
        :param dict response: JSON Response received from LBRY
        :param int status_code: HTTP Status code received from HTTP request
        :param request.PreparedRequest request: PreparedRequest object which raised the exception
        """
        super().__init__(message)

        self.response = response
        self.status_code = status_code
        self.request = request

