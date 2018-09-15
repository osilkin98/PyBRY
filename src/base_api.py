




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


    @classmethod
    def make_request(cls, url, method, params=None, basic_auth=None):
        """ Makes a cURL POST request to the given URL, specifying the data to be passed in as
         {"method": method, "params": parameters}

        :param str url: URL to connect to.
        :param str method: The API method to call.
        :param dict params: Dictionary object of the parameters associated with the `method` given. None by default.
        :param list basic_auth: List containing your username and password as ['username', 'password'].
         This is empty by default, however it is required by all of the `lbrycrd` methods
        :return: A `dict` of the JSON result member of the request
        """




    # I'm not sure if this is actually needed
    def __init__(self, credentials=None):
        """ Initializes the BaseApi object.

        :param list | tuple: This should be a list in the format ["username", "password"]. If None is used, then
         the API will presume to use the non-authenticated API.
        """

        # Set the credentials for subsequent calls
        self.credentials = [] if credentials is None else credentials



