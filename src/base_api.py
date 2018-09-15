import requests
import src.LBRYException as LBRYUtils

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
    def make_request(cls, url, method, params=None, basic_auth=None, timeout=600):
        """ Makes a cURL POST request to the given URL, specifying the data to be passed in as
         {"method": method, "params": parameters}

        :param str url: URL to connect to.
        :param str method: The API method to call.
        :param dict params: Dictionary object of the parameters associated with the `method` given. None by default.
        :param list | tuple basic_auth: List containing your username and password as ['username', 'password'].
         This is empty by default, however it is required by all of the `lbrycrd` methods
        :param float timeout: Amount of seconds to wait for the server's response before we timeout.
        :return: A `dict` of the JSON result member of the request
        """

        # Default parameters
        params = {} if params is None else params

        # Default basic_auth to an empty list if it wasnt supplied
        basic_auth = () if basic_auth is None else basic_auth

        # Increment the request ID
        cls.request_id += 1

        # This is the data to be sent
        data = {"method": method, "params": params,"jsonrpc": "2.0","id": cls.request_id}

        headers = {"Content-Type": "application/json-rpc",  # sends the request as a json
                   "user-agent": "LBRY python3-api"}    # Sets the user agent

        try:
            # You could create a request object and then make a prepared request object
            # And then be able to print the Request that will be sent
            request = requests.Request('POST', url, json=data, headers=headers, auth=tuple(basic_auth))

            prepared = request.prepare()

            sesh = requests.Session()

            response = sesh.send(prepared)

            if 'error' in response:
                raise LBRYUtils.LBRYException("POST Request made to LBRY received an error",
                                              response.json(), response.status_code, prepared)

        except requests.HTTPError as HE:
            print(HE)

        except requests.RequestException as RE:
            # Print the Request Exception given
            print(RE)

            print("Printing Request Created:\n")

            LBRYUtils.print_request(prepared)

