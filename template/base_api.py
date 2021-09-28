"""Base class that provides an interface to make requests to the LBRY APIs.

The basic functionality is making a POST request to a given URL (server),
with a given method (API function), and the parameters which that method
needs (params).

We want to be able to continuously make requests if we need to,
so this is implemented as a class that is initialized once, and then
it can make multiple requests to the API.
"""
import requests
import pybry.exception as lbryex


class BaseApi:

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
        :raises LBRYException: If the request returns an error when calling the API
        :return: A `dict` of the JSON result member of the request
        :rtype: dict, PreparedResponse
        """
        # Default parameters
        params = {} if params is None else params

        # Increment the request ID
        cls.request_id += 1

        # Weed out all the None valued params
        params = {k: v for (k, v) in params.items() if v is not None}

        # This is the data to be sent
        data = {"method": method,
                "params": params,
                "jsonrpc": "2.0",
                "id": cls.request_id}

        # Send the request as JSON, and with the specified user-agent
        headers = {"Content-Type": "application/json-rpc",
                   "user-agent": "LBRY python3-api"}

        # You could create a request object and then make a prepared request object
        # And then be able to print the Request that will be sent
        request = requests.Request('POST', url,
                                   json=data,
                                   headers=headers,
                                   auth=basic_auth)

        prepared = request.prepare()

        try:
            # Send the prepared request object through
            sesh = requests.Session()
            response = sesh.send(prepared, timeout=timeout)
            response_json = response.json()

            # Returns the Result sub-JSON formatted as a dict
            if 'result' in response_json:
                return response_json['result'], response

            elif 'error' in response_json:
                raise lbryex.LBRYError("POST Request made to LBRY received an error",
                                       response_json,
                                       response.status_code,
                                       prepared)

        except requests.HTTPError as HE:
            print(HE)
            return None, None

        except requests.RequestException as RE:
            print(RE)
            print("Printing request:")
            lbryex.print_request(prepared)

            return None, None

