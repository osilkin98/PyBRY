from pybry.base_api import BaseApi
from pybry.constants import LBRYD_SERVER_ADDRESS as SERVER_ADDRESS


class LbrydApi(BaseApi):

    def __init__(self, timeout=600):
        """
        LBRY daemon wrapper.

        Initialize this class, and use its methods.
        >>> lbry = LbrydApi()
        >>> response = lbry.claim_search(name='LBRYPlaylists')

        :param float timeout: The number of seconds to wait for a connection until we time out
        """
        self.timeout = timeout

    @classmethod
    def call(cls, method, params=None, timeout=600):
        """Makes a call to the LBRY API.

        :param str method: Method to call from the LBRY API. See the full list of methods at
         https://github.com/lbryio/lbry-sdk/blob/master/lbry/extras/daemon/daemon.py
         The daemon methods start with the string `jsonrpc_`
        :param dict params: Parameters to give the method selected
        :param float timeout: The number of seconds to wait for a connection until we time out; 600 By Default.
        :raises LBRYException: If the request returns an error when calling the API
        :return: A Python `dict` object containing the data requested from the API
        :rtype: dict
        """

        params = [] if params is None else params

        return cls.make_request(SERVER_ADDRESS, method, params, timeout=timeout)

