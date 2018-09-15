




'''
    What needs to be done is the following

    An API Wrapper for LBRY.io needs to be made in order to make requests to the API

    The only two examples I've seen both were making requests to the authorized-api, which
    required a username and a password. Since this is sort of confusing and not very
    test-friendly if you want to make requests without having a username and password


    basic idea is as follows: we need to make a POST request to a given URL,
    with a 'method' (api function), and the parameters we give it.

    We want to be able to continuously make requests if we need to, and so we will
    encapsulate this as a class


'''


class BaseApi(object):

    request_id = 0

    def __init__(self, credentials=None):
        """ Initializes the BaseApi object.

        :param list | tuple: This should be a list in the format ["username", "password"]. If None is used, then
         the API will presume to use the non-authenticated API.
        """

        # Set the credentials for subsequent calls
        self.credentials = [] if credentials is None else credentials


