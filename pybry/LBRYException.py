

def print_request(request):
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


class LBRYException(Exception):

    def __init__(self, message, response, status_code, request):
        """

        :param str message: Message to Display
        :param dict response: JSON Response received from LBRY
        :param int status_code: HTTP Status code received from HTTP request
        :param request.PreparedRequest request: PreparedRequest object which raised the exception
        """

        # Call the
        super().__init__(message)

        self.response = response
        self.status_code = status_code
        self.request = request
