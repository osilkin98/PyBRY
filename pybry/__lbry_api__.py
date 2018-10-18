from pybry.base_api import BaseApi
from pybry.constants import LBRYD_SERVER_ADDRESS as SERVER_ADDRESS


class LbryApi(BaseApi):

    def __init__(self, timeout=600):
        """
        :param float timeout: The number of seconds to wait for a connection until we time out
        """
        self.timeout = timeout

    @classmethod
    def call(cls, method, params=None, timeout=600):
        """ Makes a Call to the LBRY API

        :param str method: Method to call from the LBRY API. See the full list of methods at
         https://lbryio.github.io/lbry/cli/
        :param dict params: Parameters to give the method selected
        :param float timeout: The number of seconds to wait for a connection until we time out; 600 By Default.
        :raises LBRYException: If the request returns an error when calling the API
        :return: A Python `dict` object containing the data requested from the API
        :rtype: dict
        """

        params = [] if params is None else params

        return cls.make_request(SERVER_ADDRESS, method, params, timeout=timeout)

