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

    def account_add(self, account_name, seed=None, private_key=None, public_key=None, single_key=None):
        """Add a previously created account from a seed, private key or public key (read-only).
Specify --single_key for single address or vanity address accounts.

        :param str account_name: name of the account to add
        :param str seed: seed to generate new account from (Optional)
        :param str private_key: private key for new account (Optional)
        :param str public_key: public key for new account (Optional)
        :param bool single_key: create single key account, default is multi-key (Optional)
        :return: (map) added account details(map) added account details
        """
        __params_map = {'account_name': account_name,
                        'seed': seed,
                        'private_key': private_key,
                        'public_key': public_key,
                        'single_key': single_key}

        return self.make_request(SERVER_ADDRESS, 'account_add', __params_map, timeout=self.timeout)

    def account_balance(self, account_id=None, address=None, include_unconfirmed=None):
        """Return the balance of an account

        :param str account_id: If provided only the balance for this account will be given (Optional)
        :param str address: If provided only the balance for this address will be given (Optional)
        :param bool include_unconfirmed: Include unconfirmed (Optional)
        :rtype: float
        :return: (decimal) amount of lbry credits in wallet(decimal) amount of lbry credits in wallet
        """
        __params_map = {'account_id': account_id,
                        'address': address,
                        'include_unconfirmed': include_unconfirmed}

        return self.make_request(SERVER_ADDRESS, 'account_balance', __params_map, timeout=self.timeout)

    def account_create(self, account_name, single_key=None):
        """Create a new account. Specify --single_key if you want to use
the same address for all transactions (not recommended).

        :param str account_name: name of the account to create
        :param bool single_key: create single key account, default is multi-key (Optional)
        :return: (map) new account details(map) new account details
        """
        __params_map = {'account_name': account_name,
                        'single_key': single_key}

        return self.make_request(SERVER_ADDRESS, 'account_create', __params_map, timeout=self.timeout)

    def account_decrypt(self):
        """Decrypt an encrypted account, this will remove the wallet password

        :rtype: bool
        :return: (bool) true if wallet is decrypted, otherwise false(bool) true if wallet is decrypted, otherwise false
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'account_decrypt', __params_map, timeout=self.timeout)

    def account_encrypt(self, new_password):
        """Encrypt a wallet with a password, if the wallet is already encrypted this will update
the password

        :param str new_password: password string to be used for encrypting wallet
        :rtype: bool
        :return: (bool) true if wallet is decrypted, otherwise false(bool) true if wallet is decrypted, otherwise false
        """
        __params_map = {'new_password': new_password}

        return self.make_request(SERVER_ADDRESS, 'account_encrypt', __params_map, timeout=self.timeout)

    def account_fund(self, to_account, from_account, amount, everything=None, outputs=None, broadcast=None):
        """Transfer some amount (or --everything) to an account from another
account (can be the same account). Amounts are interpreted as LBC.
You can also spread the transfer across a number of --outputs (cannot
be used together with --everything).

        :param str to_account: send to this account
        :param str from_account: spend from this account
        :param str amount: the amount to transfer lbc
        :param bool everything: transfer everything (excluding claims), default: false. (Optional)
        :param int outputs: split payment across many outputs, default: 1. (Optional)
        :param bool broadcast: actually broadcast the transaction, default: false. (Optional)
        :return: (map) transaction performing requested action(map) transaction performing requested action
        """
        __params_map = {'to_account': to_account,
                        'from_account': from_account,
                        'amount': amount,
                        'everything': everything,
                        'outputs': outputs,
                        'broadcast': broadcast}

        return self.make_request(SERVER_ADDRESS, 'account_fund', __params_map, timeout=self.timeout)

    def account_list(self, account_id=None, confirmations=None, include_reserved=None, include_claims=None, show_seed=None):
        """List details of all of the accounts or a specific account.

        :param str account_id: If provided only the balance for this account will be given (Optional)
        :param int confirmations: required confirmations (default: 6) (Optional)
        :param bool include_reserved: include reserved UTXOs (default: false) (Optional)
        :param bool include_claims: include claims, requires than a LBC account is specified (default: false) (Optional)
        :param bool show_seed: show the seed for the account (Optional)
        :return: (map) balance of account(s)(map) balance of account(s)
        """
        __params_map = {'account_id': account_id,
                        'confirmations': confirmations,
                        'include_reserved': include_reserved,
                        'include_claims': include_claims,
                        'show_seed': show_seed}

        return self.make_request(SERVER_ADDRESS, 'account_list', __params_map, timeout=self.timeout)

    def account_max_address_gap(self, account_id):
        """Finds ranges of consecutive addresses that are unused and returns the length
of the longest such range: for change and receiving address chains. This is
useful to figure out ideal values to set for 'receiving_gap' and 'change_gap'
account settings.

        :param str account_id: account for which to get max gaps
        :return: (map) maximum gap for change and receiving addresses(map) maximum gap for change and receiving addresses
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'account_max_address_gap', __params_map, timeout=self.timeout)

    def account_remove(self, account_id):
        """Remove an existing account.

        :param str account_id: id of the account to remove
        :return: (map) details of removed account(map) details of removed account
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'account_remove', __params_map, timeout=self.timeout)

    def account_set(self, account_id, default=None, new_name=None, receiving_gap=None, receiving_max_uses=None, change_gap=None, change_max_uses=None):
        """Change various settings on an account.

        :param str account_id: id of the account to change
        :param bool default: make this account the default (Optional)
        :param str new_name: new name for the account (Optional)
        :param int receiving_gap: set the gap for receiving addresses (Optional)
        :param int receiving_max_uses: set the maximum number of times to use a receiving address (Optional)
        :param int change_gap: set the gap for change addresses (Optional)
        :param int change_max_uses: set the maximum number of times to use a change address (Optional)
        :return: (map) updated account details(map) updated account details
        """
        __params_map = {'account_id': account_id,
                        'default': default,
                        'new_name': new_name,
                        'receiving_gap': receiving_gap,
                        'receiving_max_uses': receiving_max_uses,
                        'change_gap': change_gap,
                        'change_max_uses': change_max_uses}

        return self.make_request(SERVER_ADDRESS, 'account_set', __params_map, timeout=self.timeout)

    def account_unlock(self, password):
        """Unlock an encrypted account

        :param str password: password for unlocking wallet
        :rtype: bool
        :return: (bool) true if account is unlocked, otherwise false(bool) true if account is unlocked, otherwise false
        """
        __params_map = {'password': password}

        return self.make_request(SERVER_ADDRESS, 'account_unlock', __params_map, timeout=self.timeout)

    def address_is_mine(self, address, account_id=None):
        """Checks if an address is associated with the current wallet.

        :param str address: address to check
        :param str account_id: id of the account to use (Optional)
        :rtype: bool
        :return: (bool) true, if address is associated with current wallet(bool) true, if address is associated with current wallet
        """
        __params_map = {'address': address,
                        'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'address_is_mine', __params_map, timeout=self.timeout)

    def address_list(self, account_id=None):
        """List account addresses

        :param str account_id: id of the account to use (Optional)
        :return: List of wallet addressesList of wallet addresses
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'address_list', __params_map, timeout=self.timeout)

    def address_public_key(self, address):
        """Get public key from wallet address

        :param str address: address for which to get the public key
        :rtype: list
        :return: (list) list of public keys associated with address.        Could contain more than one public key if multisig.(list) list of public keys associated with address.        Could conta
        in more than one public key if multisig.
        """
        __params_map = {'address': address}

        return self.make_request(SERVER_ADDRESS, 'address_public_key', __params_map, timeout=self.timeout)

    def address_unused(self, account_id=None):
        """Return an address containing no balance, will create
a new address if there is none.

        :param str account_id: id of the account to use (Optional)
        :rtype: str
        :return: (str) Unused wallet address in base58(str) Unused wallet address in base58
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'address_unused', __params_map, timeout=self.timeout)

    def blob_announce(self, blob_hash=None, stream_hash=None, sd_hash=None):
        """Announce blobs to the DHT

        :param str blob_hash: announce a blob, specified by blob_hash (Optional)
        :param str stream_hash: announce all blobs associated with stream_hash (Optional)
        :param str sd_hash: announce all blobs associated with sd_hash and the sd_hash itself (Optional)
        :rtype: bool
        :return: (bool) true if successful(bool) true if successful
        """
        __params_map = {'blob_hash': blob_hash,
                        'stream_hash': stream_hash,
                        'sd_hash': sd_hash}

        return self.make_request(SERVER_ADDRESS, 'blob_announce', __params_map, timeout=self.timeout)

    def blob_availability(self, blob_hash, search_timeout=None, blob_timeout=None):
        """Get blob availability

        :param str blob_hash: check availability for this blob hash
        :param int search_timeout: how long to search for peers for the blob in the dht (Optional)
        :param int blob_timeout: how long to try downloading from a peer (Optional)
        :rtype: dict
        :return: (dict) {        "is_available": <bool, true if blob is available from a peer from peer list>        "reachable_peers": ["<ip>:<port>"],        "unreachable_peers": ["<ip>:<port>"]    }(dict) {        "is_available": <bool, true if blob is available from
        a peer from peer list>        "reachable_peers": ["<ip>:<port>"],
           "unreachable_peers": ["<ip>:<port>"]    }
        """
        __params_map = {'blob_hash': blob_hash,
                        'search_timeout': search_timeout,
                        'blob_timeout': blob_timeout}

        return self.make_request(SERVER_ADDRESS, 'blob_availability', __params_map, timeout=self.timeout)

    def blob_delete(self, blob_hash):
        """Delete a blob

        :param str blob_hash: blob hash of the blob to delete
        :rtype: str
        :return: (str) Success/fail message(str) Success/fail message
        """
        __params_map = {'blob_hash': blob_hash}

        return self.make_request(SERVER_ADDRESS, 'blob_delete', __params_map, timeout=self.timeout)

    def blob_get(self, blob_hash, timeout=None, encoding=None, payment_rate_manager=None):
        """Download and return a blob

        :param str blob_hash: blob hash of the blob to get
        :param int timeout: timeout in number of seconds (Optional)
        :param str encoding: by default no attempt at decoding is made, can be set to one of the following decoders: 'json' (Optional)
        :param str payment_rate_manager: if not given the default payment rate manager will be used. supported alternative rate managers: 'only-free' (Optional)
        :rtype: str
        :return: (str) Success/Fail message or (dict) decoded data(str) Success/Fail message or (dict) decoded data
        """
        __params_map = {'blob_hash': blob_hash,
                        'timeout': timeout,
                        'encoding': encoding,
                        'payment_rate_manager': payment_rate_manager}

        return self.make_request(SERVER_ADDRESS, 'blob_get', __params_map, timeout=self.timeout)

    def blob_list(self, needed=None, finished=None, uri=None, stream_hash=None, sd_hash=None, page_size=None, page=None):
        """Returns blob hashes. If not given filters, returns all blobs known by the blob manager

        :param bool needed: only return needed blobs (Optional)
        :param bool finished: only return finished blobs (Optional)
        :param str uri: filter blobs by stream in a uri (Optional)
        :param str stream_hash: filter blobs by stream hash (Optional)
        :param str sd_hash: filter blobs by sd hash (Optional)
        :param int page_size: results page size (Optional)
        :param int page: page of results to return (Optional)
        :rtype: list
        :return: (list) List of blob hashes(list) List of blob hashes
        """
        __params_map = {'needed': needed,
                        'finished': finished,
                        'uri': uri,
                        'stream_hash': stream_hash,
                        'sd_hash': sd_hash,
                        'page_size': page_size,
                        'page': page}

        return self.make_request(SERVER_ADDRESS, 'blob_list', __params_map, timeout=self.timeout)

    def blob_reflect(self, reflector_server=None):
        """Reflects specified blobs

        :param str reflector_server: reflector address (Optional)
        :rtype: list
        :return: (list) reflected blob hashes(list) reflected blob hashes
        """
        __params_map = {'reflector_server': reflector_server}

        return self.make_request(SERVER_ADDRESS, 'blob_reflect', __params_map, timeout=self.timeout)

    def blob_reflect_all(self):
        """Reflects all saved blobs

        :rtype: bool
        :return: (bool) true if successful(bool) true if successful
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'blob_reflect_all', __params_map, timeout=self.timeout)

    def block_show(self, blockhash, height):
        """Get contents of a block

        :param str blockhash: hash of the block to look up
        :param int height: height of the block to look up
        :rtype: dict
        :return: (dict) Requested block(dict) Requested block
        """
        __params_map = {'blockhash': blockhash,
                        'height': height}

        return self.make_request(SERVER_ADDRESS, 'block_show', __params_map, timeout=self.timeout)

    def channel_export(self, claim_id):
        """Export serialized channel signing information for a given certificate claim id

        :param str claim_id: Claim ID to export information about
        :rtype: str
        :return: (str) Serialized certificate information(str) Serialized certificate information
        """
        __params_map = {'claim_id': claim_id}

        return self.make_request(SERVER_ADDRESS, 'channel_export', __params_map, timeout=self.timeout)

    def channel_import(self, serialized_certificate_info):
        """Import serialized channel signing information (to allow signing new claims to the channel)

        :param str serialized_certificate_info: certificate info
        :rtype: dict
        :return: (dict) Result dictionary(dict) Result dictionary
        """
        __params_map = {'serialized_certificate_info': serialized_certificate_info}

        return self.make_request(SERVER_ADDRESS, 'channel_import', __params_map, timeout=self.timeout)

    def channel_list(self):
        """Get certificate claim infos for channels that can be published to

        :rtype: list
        :return: (list) ClaimDict, includes 'is_mine' field to indicate if the certificate claim    is in the wallet.(list) ClaimDict, includes 'is_mine' field to indicate if the certific
        ate claim    is in the wallet.
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'channel_list', __params_map, timeout=self.timeout)

    def channel_new(self, channel_name, amount):
        """Generate a publisher key and create a new '@' prefixed certificate claim

        :param str channel_name: name of the channel prefixed with '@'
        :param float amount: bid amount on the channel
        :rtype: dict
        :return: (dict) Dictionary containing result of the claim    {        'tx' : (str) hex encoded transaction        'txid' : (str) txid of resulting claim        'nout' : (int) nout of the resulting claim        'fee' : (float) fee paid for the claim transaction        'claim_id' : (str) claim ID of the resulting claim    }(dict) Dictionary containing result of the claim    {        'tx' : (s
        tr) hex encoded transaction        'txid' : (str) txid of resulting cl
        aim        'nout' : (int) nout of the resulting claim        'fee' : (
        float) fee paid for the claim transaction        'claim_id' : (str) cl
        aim ID of the resulting claim    }
        """
        __params_map = {'channel_name': channel_name,
                        'amount': amount}

        return self.make_request(SERVER_ADDRESS, 'channel_new', __params_map, timeout=self.timeout)

    def claim_abandon(self, claim_id=None, txid=None, nout=None, account_id=None):
        """Abandon a name and reclaim credits from the claim

        :param str claim_id: claim_id of the claim to abandon (Optional)
        :param str txid: txid of the claim to abandon (Optional)
        :param int nout: nout of the claim to abandon (Optional)
        :param str account_id: id of the account to use (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing result of the claim    {        success: (bool) True if txn is successful        txid : (str) txid of resulting transaction    }(dict) Dictionary containing result of the claim    {        success:
        (bool) True if txn is successful        txid : (str) txid of resulting
         transaction    }
        """
        __params_map = {'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'claim_abandon', __params_map, timeout=self.timeout)

    def claim_list(self, name):
        """List current claims and information about them for a given name

        :param str name: name of the claim to list info about
        :rtype: dict
        :return: (dict) State of claims assigned for the name    {        'claims': (list) list of claims for the name        [            {            'amount': (float) amount assigned to the claim            'effective_amount': (float) total amount assigned to the claim,                                including supports            'claim_id': (str) claim ID of the claim            'height': (int) height of block containing the claim            'txid': (str) txid of the claim            'nout': (int) nout of the claim            'permanent_url': (str) permanent url of the claim,            'supports': (list) a list of supports attached to the claim            'value': (str) the value of the claim            },        ]        'supports_without_claims': (list) supports without any claims attached to them        'last_takeover_height': (int) the height of last takeover for the name    }(dict) State of claims assigned for the name    {        'claims': (li
        st) list of claims for the name        [            {            'amou
        nt': (float) amount assigned to the claim            'effective_amount
        ': (float) total amount assigned to the claim,
                including supports            'claim_id': (str) claim ID of th
        e claim            'height': (int) height of block containing the clai
        m            'txid': (str) txid of the claim            'nout': (int)
        nout of the claim            'permanent_url': (str) permanent url of t
        he claim,            'supports': (list) a list of supports attached to
         the claim            'value': (str) the value of the claim
         },        ]        'supports_without_claims': (list) supports without
         any claims attached to them        'last_takeover_height': (int) the
        height of last takeover for the name    }
        """
        __params_map = {'name': name}

        return self.make_request(SERVER_ADDRESS, 'claim_list', __params_map, timeout=self.timeout)

    def claim_list_by_channel(self, uri, uris=None, page=None, page_size=None):
        """Get paginated claims in a channel specified by a channel uri

        :param str uri: uri of the channel
        :param list uris: uris of the channel (Optional)
        :param int page: which page of results to return where page 1 is the first page, defaults to no pages (Optional)
        :param int page_size: number of results in a page, default of 10 (Optional)
        :rtype: str
        :return: {         resolved channel uri: {            If there was an error:            'error': (str) error message            'claims_in_channel': the total number of results for the channel,            If a page of results was requested:            'returned_page': page number returned,            'claims_in_channel': [                {                    'absolute_channel_position': (int) claim index number in sorted list of                                                 claims which assert to be part of the                                                 channel                    'address': (str) claim address,                    'amount': (float) claim amount,                    'effective_amount': (float) claim amount including supports,                    'claim_id': (str) claim id,                    'claim_sequence': (int) claim sequence number,                    'decoded_claim': (bool) whether or not the claim value was decoded,                    'height': (int) claim height,                    'depth': (int) claim depth,                    'has_signature': (bool) included if decoded_claim                    'name': (str) claim name,                    'supports: (list) list of supports [{'txid': (str) txid,                                                         'nout': (int) nout,                                                         'amount': (float) amount}],                    'txid': (str) claim txid,                    'nout': (str) claim nout,                    'signature_is_valid': (bool), included if has_signature,                    'value': ClaimDict if decoded, otherwise hex string                }            ],        }    }{         resolved channel uri: {            If there was an error:
                 'error': (str) error message            'claims_in_channel':
        the total number of results for the channel,            If a page of r
        esults was requested:            'returned_page': page number returned
        ,            'claims_in_channel': [                {
          'absolute_channel_position': (int) claim index number in sorted list
         of                                                 claims which asser
        t to be part of the                                                 ch
        annel                    'address': (str) claim address,
              'amount': (float) claim amount,                    'effective_am
        ount': (float) claim amount including supports,                    'cl
        aim_id': (str) claim id,                    'claim_sequence': (int) cl
        aim sequence number,                    'decoded_claim': (bool) whethe
        r or not the claim value was decoded,                    'height': (in
        t) claim height,                    'depth': (int) claim depth,
                     'has_signature': (bool) included if decoded_claim
                    'name': (str) claim name,                    'supports: (l
        ist) list of supports [{'txid': (str) txid,
                                      'nout': (int) nout,
                                            'amount': (float) amount}],
                     'txid': (str) claim txid,                    'nout': (str
        ) claim nout,                    'signature_is_valid': (bool), include
        d if has_signature,                    'value': ClaimDict if decoded,
        otherwise hex string                }            ],        }    }
        """
        __params_map = {'uri': uri,
                        'uris': uris,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'claim_list_by_channel', __params_map, timeout=self.timeout)

    def claim_list_mine(self, account_id=None):
        """List my name claims

        :param str account_id: id of the account to query (Optional)
        :rtype: list
        :return: (list) List of name claims owned by user    [        {            'address': (str) address that owns the claim            'amount': (float) amount assigned to the claim            'blocks_to_expiration': (int) number of blocks until it expires            'category': (str) "claim", "update" , or "support"            'claim_id': (str) claim ID of the claim            'confirmations': (int) number of blocks of confirmations for the claim            'expiration_height': (int) the block height which the claim will expire            'expired': (bool) true if expired, false otherwise            'height': (int) height of the block containing the claim            'is_spent': (bool) true if claim is abandoned, false otherwise            'name': (str) name of the claim            'permanent_url': (str) permanent url of the claim,            'txid': (str) txid of the claim            'nout': (int) nout of the claim            'value': (str) value of the claim        },   ](list) List of name claims owned by user    [        {            'add
        ress': (str) address that owns the claim            'amount': (float)
        amount assigned to the claim            'blocks_to_expiration': (int)
        number of blocks until it expires            'category': (str) "claim"
        , "update" , or "support"            'claim_id': (str) claim ID of the
         claim            'confirmations': (int) number of blocks of confirmat
        ions for the claim            'expiration_height': (int) the block hei
        ght which the claim will expire            'expired': (bool) true if e
        xpired, false otherwise            'height': (int) height of the block
         containing the claim            'is_spent': (bool) true if claim is a
        bandoned, false otherwise            'name': (str) name of the claim
                  'permanent_url': (str) permanent url of the claim,
          'txid': (str) txid of the claim            'nout': (int) nout of the
         claim            'value': (str) value of the claim        },   ]
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'claim_list_mine', __params_map, timeout=self.timeout)

    def claim_new_support(self, name, claim_id, amount, account_id=None):
        """Support a name claim

        :param str name: name of the claim to support
        :param str claim_id: claim_id of the claim to support
        :param float amount: amount of support
        :param str account_id: id of the account to use (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing the transaction information    {        "hex": (str) raw transaction,        "inputs": (list) inputs(dict) used for the transaction,        "outputs": (list) outputs(dict) for the transaction,        "total_fee": (int) fee in dewies,        "total_input": (int) total of inputs in dewies,        "total_output": (int) total of outputs in dewies(input - fees),        "txid": (str) txid of the transaction,    }(dict) Dictionary containing the transaction information    {        "
        hex": (str) raw transaction,        "inputs": (list) inputs(dict) used
         for the transaction,        "outputs": (list) outputs(dict) for the t
        ransaction,        "total_fee": (int) fee in dewies,        "total_inp
        ut": (int) total of inputs in dewies,        "total_output": (int) tot
        al of outputs in dewies(input - fees),        "txid": (str) txid of th
        e transaction,    }
        """
        __params_map = {'name': name,
                        'claim_id': claim_id,
                        'amount': amount,
                        'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'claim_new_support', __params_map, timeout=self.timeout)

    def claim_renew(self, outpoint, height):
        """Renew claim(s) or support(s)

        :param str outpoint: outpoint of the claim to renew
        :param str height: update claims expiring before or at this block height
        :rtype: dict
        :return: (dict) Dictionary where key is the the original claim's outpoint and    value is the result of the renewal    {        outpoint:{            'tx' : (str) hex encoded transaction            'txid' : (str) txid of resulting claim            'nout' : (int) nout of the resulting claim            'fee' : (float) fee paid for the claim transaction            'claim_id' : (str) claim ID of the resulting claim        },    }(dict) Dictionary where key is the the original claim's outpoint and
          value is the result of the renewal    {        outpoint:{
         'tx' : (str) hex encoded transaction            'txid' : (str) txid o
        f resulting claim            'nout' : (int) nout of the resulting clai
        m            'fee' : (float) fee paid for the claim transaction
             'claim_id' : (str) claim ID of the resulting claim        },    }

        """
        __params_map = {'outpoint': outpoint,
                        'height': height}

        return self.make_request(SERVER_ADDRESS, 'claim_renew', __params_map, timeout=self.timeout)

    def claim_send_to_address(self, claim_id, address, amount=None):
        """Send a name claim to an address

        :param str claim_id: claim_id to send
        :param str address: address to send the claim to
        :param int amount: Amount of credits to claim name for, defaults to the current amount on the claim (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing result of the claim    {        'tx' : (str) hex encoded transaction        'txid' : (str) txid of resulting claim        'nout' : (int) nout of the resulting claim        'fee' : (float) fee paid for the claim transaction        'claim_id' : (str) claim ID of the resulting claim    }(dict) Dictionary containing result of the claim    {        'tx' : (s
        tr) hex encoded transaction        'txid' : (str) txid of resulting cl
        aim        'nout' : (int) nout of the resulting claim        'fee' : (
        float) fee paid for the claim transaction        'claim_id' : (str) cl
        aim ID of the resulting claim    }
        """
        __params_map = {'claim_id': claim_id,
                        'address': address,
                        'amount': amount}

        return self.make_request(SERVER_ADDRESS, 'claim_send_to_address', __params_map, timeout=self.timeout)

    def claim_show(self, txid=None, nout=None, claim_id=None):
        """Resolve claim info from txid/nout or with claim ID

        :param str txid: look for claim with this txid, nout must also be specified (Optional)
        :param int nout: look for claim with this nout, txid must also be specified (Optional)
        :param str claim_id: look for claim with this claim id (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing claim info as below,    {        'txid': (str) txid of claim        'nout': (int) nout of claim        'amount': (float) amount of claim        'value': (str) value of claim        'height' : (int) height of claim takeover        'claim_id': (str) claim ID of claim        'supports': (list) list of supports associated with claim    }    if claim cannot be resolved, dictionary as below will be returned    {        'error': (str) reason for error    }(dict) Dictionary containing claim info as below,    {        'txid':
        (str) txid of claim        'nout': (int) nout of claim        'amount'
        : (float) amount of claim        'value': (str) value of claim
        'height' : (int) height of claim takeover        'claim_id': (str) cla
        im ID of claim        'supports': (list) list of supports associated w
        ith claim    }    if claim cannot be resolved, dictionary as below wil
        l be returned    {        'error': (str) reason for error    }
        """
        __params_map = {'txid': txid,
                        'nout': nout,
                        'claim_id': claim_id}

        return self.make_request(SERVER_ADDRESS, 'claim_show', __params_map, timeout=self.timeout)

    def claim_tip(self, claim_id, amount, account_id=None):
        """Tip the owner of the claim

        :param str claim_id: claim_id of the claim to support
        :param float amount: amount of support
        :param str account_id: id of the account to use (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing the transaction information    {        "hex": (str) raw transaction,        "inputs": (list) inputs(dict) used for the transaction,        "outputs": (list) outputs(dict) for the transaction,        "total_fee": (int) fee in dewies,        "total_input": (int) total of inputs in dewies,        "total_output": (int) total of outputs in dewies(input - fees),        "txid": (str) txid of the transaction,    }(dict) Dictionary containing the transaction information    {        "
        hex": (str) raw transaction,        "inputs": (list) inputs(dict) used
         for the transaction,        "outputs": (list) outputs(dict) for the t
        ransaction,        "total_fee": (int) fee in dewies,        "total_inp
        ut": (int) total of inputs in dewies,        "total_output": (int) tot
        al of outputs in dewies(input - fees),        "txid": (str) txid of th
        e transaction,    }
        """
        __params_map = {'claim_id': claim_id,
                        'amount': amount,
                        'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'claim_tip', __params_map, timeout=self.timeout)

    def commands(self):
        """Return a list of available commands

        :rtype: list
        :return: (list) list of available commands(list) list of available commands
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'commands', __params_map, timeout=self.timeout)

    def file_delete(self, delete_from_download_dir=None, delete_all=None, sd_hash=None, file_name=None, stream_hash=None, rowid=None, claim_id=None, txid=None, nout=None, claim_name=None, channel_claim_id=None, channel_name=None):
        """Delete a LBRY file

        :param bool delete_from_download_dir: delete file from download directory, instead of just deleting blobs (Optional)
        :param bool delete_all: if there are multiple matching files, allow the deletion of multiple files. Otherwise do not delete anything. (Optional)
        :param str sd_hash: delete by file sd hash (Optional)
        :param str file_name: delete by file name in downloads folder (Optional)
        :param str stream_hash: delete by file stream hash (Optional)
        :param int rowid: delete by file row id (Optional)
        :param str claim_id: delete by file claim id (Optional)
        :param str txid: delete by file claim txid (Optional)
        :param int nout: delete by file claim nout (Optional)
        :param str claim_name: delete by file claim name (Optional)
        :param str channel_claim_id: delete by file channel claim id (Optional)
        :param str channel_name: delete by file channel claim name (Optional)
        :rtype: bool
        :return: (bool) true if deletion was successful(bool) true if deletion was successful
        """
        __params_map = {'delete_from_download_dir': delete_from_download_dir,
                        'delete_all': delete_all,
                        'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'claim_name': claim_name,
                        'channel_claim_id': channel_claim_id,
                        'channel_name': channel_name}

        return self.make_request(SERVER_ADDRESS, 'file_delete', __params_map, timeout=self.timeout)

    def file_list(self, sd_hash=None, file_name=None, stream_hash=None, rowid=None, claim_id=None, outpoint=None, txid=None, nout=None, channel_claim_id=None, channel_name=None, claim_name=None, sort=None):
        """List files limited by optional filters

        :param str sd_hash: get file with matching sd hash (Optional)
        :param str file_name: get file with matching file name in the downloads folder (Optional)
        :param str stream_hash: get file with matching stream hash (Optional)
        :param int rowid: get file with matching row id (Optional)
        :param str claim_id: get file with matching claim id (Optional)
        :param str outpoint: get file with matching claim outpoint (Optional)
        :param str txid: get file with matching claim txid (Optional)
        :param int nout: get file with matching claim nout (Optional)
        :param str channel_claim_id: get file with matching channel claim id (Optional)
        :param str channel_name: get file with matching channel name (Optional)
        :param str claim_name: get file with matching claim name (Optional)
        :param str sort: sort by any property, like 'file_name' or 'metadata.author'; to specify direction append ',asc' or ',desc' (Optional)
        :rtype: list
        :return: (list) List of files    [        {            'completed': (bool) true if download is completed,            'file_name': (str) name of file,            'download_directory': (str) download directory,            'points_paid': (float) credit paid to download file,            'stopped': (bool) true if download is stopped,            'stream_hash': (str) stream hash of file,            'stream_name': (str) stream name ,            'suggested_file_name': (str) suggested file name,            'sd_hash': (str) sd hash of file,            'download_path': (str) download path of file,            'mime_type': (str) mime type of file,            'key': (str) key attached to file,            'total_bytes': (int) file size in bytes,            'written_bytes': (int) written size in bytes,            'blobs_completed': (int) number of fully downloaded blobs,            'blobs_in_stream': (int) total blobs on stream,            'status': (str) downloader status            'claim_id': (str) None if claim is not found else the claim id,            'outpoint': (str) None if claim is not found else the tx and output,            'txid': (str) None if claim is not found else the transaction id,            'nout': (int) None if claim is not found else the transaction output index,            'metadata': (dict) None if claim is not found else the claim metadata,            'channel_claim_id': (str) None if claim is not found or not signed,            'channel_name': (str) None if claim is not found or not signed,            'claim_name': (str) None if claim is not found else the claim name        },    ](list) List of files    [        {            'completed': (bool) true
         if download is completed,            'file_name': (str) name of file,
                    'download_directory': (str) download directory,
         'points_paid': (float) credit paid to download file,            'stop
        ped': (bool) true if download is stopped,            'stream_hash': (s
        tr) stream hash of file,            'stream_name': (str) stream name ,
                    'suggested_file_name': (str) suggested file name,
           'sd_hash': (str) sd hash of file,            'download_path': (str)
         download path of file,            'mime_type': (str) mime type of fil
        e,            'key': (str) key attached to file,            'total_byt
        es': (int) file size in bytes,            'written_bytes': (int) writt
        en size in bytes,            'blobs_completed': (int) number of fully
        downloaded blobs,            'blobs_in_stream': (int) total blobs on s
        tream,            'status': (str) downloader status            'claim_
        id': (str) None if claim is not found else the claim id,            'o
        utpoint': (str) None if claim is not found else the tx and output,
                'txid': (str) None if claim is not found else the transaction
        id,            'nout': (int) None if claim is not found else the trans
        action output index,            'metadata': (dict) None if claim is no
        t found else the claim metadata,            'channel_claim_id': (str)
        None if claim is not found or not signed,            'channel_name': (
        str) None if claim is not found or not signed,            'claim_name'
        : (str) None if claim is not found else the claim name        },    ]
        """
        __params_map = {'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'claim_id': claim_id,
                        'outpoint': outpoint,
                        'txid': txid,
                        'nout': nout,
                        'channel_claim_id': channel_claim_id,
                        'channel_name': channel_name,
                        'claim_name': claim_name,
                        'sort': sort}

        return self.make_request(SERVER_ADDRESS, 'file_list', __params_map, timeout=self.timeout)

    def file_reflect(self, sd_hash=None, file_name=None, stream_hash=None, rowid=None, reflector=None):
        """Reflect all the blobs in a file matching the filter criteria

        :param str sd_hash: get file with matching sd hash (Optional)
        :param str file_name: get file with matching file name in the downloads folder (Optional)
        :param str stream_hash: get file with matching stream hash (Optional)
        :param int rowid: get file with matching row id (Optional)
        :param str reflector: reflector server, ip address or url by default choose a server from the config (Optional)
        :rtype: list
        :return: (list) list of blobs reflected(list) list of blobs reflected
        """
        __params_map = {'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'reflector': reflector}

        return self.make_request(SERVER_ADDRESS, 'file_reflect', __params_map, timeout=self.timeout)

    def file_set_status(self, status, sd_hash=None, file_name=None, stream_hash=None, rowid=None):
        """Start or stop downloading a file

        :param str status: one of "start" or "stop"
        :param str sd_hash: set status of file with matching sd hash (Optional)
        :param str file_name: set status of file with matching file name in the downloads folder (Optional)
        :param str stream_hash: set status of file with matching stream hash (Optional)
        :param int rowid: set status of file with matching row id (Optional)
        :rtype: str
        :return: (str) Confirmation message(str) Confirmation message
        """
        __params_map = {'status': status,
                        'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid}

        return self.make_request(SERVER_ADDRESS, 'file_set_status', __params_map, timeout=self.timeout)

    def get(self, uri=None, file_name=None, timeout=None):
        """Download stream from a LBRY name.

        :param str uri: uri of the content to download (Optional)
        :param str file_name: specified name for the downloaded file (Optional)
        :param int timeout: download timeout in number of seconds (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing information about the stream    {        'completed': (bool) true if download is completed,        'file_name': (str) name of file,        'download_directory': (str) download directory,        'points_paid': (float) credit paid to download file,        'stopped': (bool) true if download is stopped,        'stream_hash': (str) stream hash of file,        'stream_name': (str) stream name ,        'suggested_file_name': (str) suggested file name,        'sd_hash': (str) sd hash of file,        'download_path': (str) download path of file,        'mime_type': (str) mime type of file,        'key': (str) key attached to file,        'total_bytes': (int) file size in bytes,        'written_bytes': (int) written size in bytes,        'blobs_completed': (int) number of fully downloaded blobs,        'blobs_in_stream': (int) total blobs on stream,        'status': (str) downloader status,        'claim_id': (str) claim id,        'outpoint': (str) claim outpoint string,        'txid': (str) claim txid,        'nout': (int) claim nout,        'metadata': (dict) claim metadata,        'channel_claim_id': (str) None if claim is not signed        'channel_name': (str) None if claim is not signed        'claim_name': (str) claim name    }(dict) Dictionary containing information about the stream    {
        'completed': (bool) true if download is completed,        'file_name':
         (str) name of file,        'download_directory': (str) download direc
        tory,        'points_paid': (float) credit paid to download file,
           'stopped': (bool) true if download is stopped,        'stream_hash'
        : (str) stream hash of file,        'stream_name': (str) stream name ,
                'suggested_file_name': (str) suggested file name,        'sd_h
        ash': (str) sd hash of file,        'download_path': (str) download pa
        th of file,        'mime_type': (str) mime type of file,        'key':
         (str) key attached to file,        'total_bytes': (int) file size in
        bytes,        'written_bytes': (int) written size in bytes,        'bl
        obs_completed': (int) number of fully downloaded blobs,        'blobs_
        in_stream': (int) total blobs on stream,        'status': (str) downlo
        ader status,        'claim_id': (str) claim id,        'outpoint': (st
        r) claim outpoint string,        'txid': (str) claim txid,        'nou
        t': (int) claim nout,        'metadata': (dict) claim metadata,
         'channel_claim_id': (str) None if claim is not signed        'channel
        _name': (str) None if claim is not signed        'claim_name': (str) c
        laim name    }
        """
        __params_map = {'uri': uri,
                        'file_name': file_name,
                        'timeout': timeout}

        return self.make_request(SERVER_ADDRESS, 'get', __params_map, timeout=self.timeout)

    def help(self, command=None):
        """Return a useful message for an API command

        :param str command: command to retrieve documentation for (Optional)
        :rtype: str
        :return: (str) Help message(str) Help message
        """
        __params_map = {'command': command}

        return self.make_request(SERVER_ADDRESS, 'help', __params_map, timeout=self.timeout)

    def peer_list(self, blob_hash, timeout=None):
        """Get peers for blob hash

        :param str blob_hash: find available peers for this blob hash
        :param int timeout: peer search timeout in seconds (Optional)
        :rtype: list
        :return: (list) List of contact dictionaries {'host': <peer ip>, 'port': <peer port>, 'node_id': <peer node id>}(list) List of contact dictionaries {'host': <peer ip>, 'port': <peer
        port>, 'node_id': <peer node id>}
        """
        __params_map = {'blob_hash': blob_hash,
                        'timeout': timeout}

        return self.make_request(SERVER_ADDRESS, 'peer_list', __params_map, timeout=self.timeout)

    def peer_ping(self, address=None, port=None):
        """Send a kademlia ping to the specified peer. If address and port are provided the peer is directly pinged,
if not provided the peer is located first.

        :param str address: ip address of the peer (Optional)
        :param int port: udp port of the peer (Optional)
        :rtype: str
        :return: (str) pong, or {'error': <error message>} if an error is encountered(str) pong, or {'error': <error message>} if an error is encountered
        """
        __params_map = {'address': address,
                        'port': port}

        return self.make_request(SERVER_ADDRESS, 'peer_ping', __params_map, timeout=self.timeout)

    def publish(self, name, bid, metadata=None, file_path=None, fee=None, title=None, description=None, author=None, language=None, license=None, license_url=None, thumbnail=None, preview=None, nsfw=None, sources=None, channel_name=None, channel_id=None, claim_address=None):
        """Make a new name claim and publish associated data to lbrynet,
update over existing claim if user already has a claim for name.

Fields required in the final Metadata are:
    'title'
    'description'
    'author'
    'language'
    'license'
    'nsfw'

Metadata can be set by either using the metadata argument or by setting individual arguments
fee, title, description, author, language, license, license_url, thumbnail, preview, nsfw,
or sources. Individual arguments will overwrite the fields specified in metadata argument.

        :param str name: name of the content (can only consist of a-z A-Z 0-9 and -(dash))
        :param float bid: amount to back the claim
        :param dict metadata: ClaimDict to associate with the claim. (Optional)
        :param str file_path: path to file to be associated with name. If provided, a lbry stream of this file will be used in 'sources'. If no path is given but a sources dict is provided, it will be used. If neither are provided, an error is raised. (Optional)
        :param dict fee: Dictionary representing key fee to download content: { 'currency': currency_symbol, 'amount': decimal, 'address': str, optional } supported currencies: LBC, USD, BTC If an address is not provided a new one will be automatically generated. Default fee is zero. (Optional)
        :param str title: title of the publication (Optional)
        :param str description: description of the publication (Optional)
        :param str author: author of the publication. The usage for this field is not the same as for channels. The author field is used to credit an author who is not the publisher and is not represented by the channel. For example, a pdf file of 'The Odyssey' has an author of 'Homer' but may by published to a channel such as '@classics', or to no channel at all (Optional)
        :param str language: language of the publication (Optional)
        :param str license: publication license (Optional)
        :param str license_url: publication license url (Optional)
        :param str thumbnail: thumbnail url (Optional)
        :param str preview: preview url (Optional)
        :param bool nsfw: whether the content is nsfw (Optional)
        :param str sources: {'lbry_sd_hash': sd_hash} specifies sd hash of file (Optional)
        :param str channel_name: name of the publisher channel name in the wallet (Optional)
        :param str channel_id: claim id of the publisher channel, does not check for channel claim being in the wallet. This allows publishing to a channel where only the certificate private key is in the wallet. (Optional)
        :param str claim_address: address where the claim is sent to, if not specified new address wil automatically be created (Optional)
        :rtype: dict
        :return: (dict) Dictionary containing result of the claim    {        'tx' : (str) hex encoded transaction        'txid' : (str) txid of resulting claim        'nout' : (int) nout of the resulting claim        'fee' : (decimal) fee paid for the claim transaction        'claim_id' : (str) claim ID of the resulting claim    }(dict) Dictionary containing result of the claim    {        'tx' : (s
        tr) hex encoded transaction        'txid' : (str) txid of resulting cl
        aim        'nout' : (int) nout of the resulting claim        'fee' : (
        decimal) fee paid for the claim transaction        'claim_id' : (str)
        claim ID of the resulting claim    }
        """
        __params_map = {'name': name,
                        'bid': bid,
                        'metadata': metadata,
                        'file_path': file_path,
                        'fee': fee,
                        'title': title,
                        'description': description,
                        'author': author,
                        'language': language,
                        'license': license,
                        'license_url': license_url,
                        'thumbnail': thumbnail,
                        'preview': preview,
                        'nsfw': nsfw,
                        'sources': sources,
                        'channel_name': channel_name,
                        'channel_id': channel_id,
                        'claim_address': claim_address}

        return self.make_request(SERVER_ADDRESS, 'publish', __params_map, timeout=self.timeout)

    def report_bug(self, message):
        """Report a bug to slack

        :param str message: Description of the bug
        :rtype: bool
        :return: (bool) true if successful(bool) true if successful
        """
        __params_map = {'message': message}

        return self.make_request(SERVER_ADDRESS, 'report_bug', __params_map, timeout=self.timeout)

    def resolve(self, uri, force=None, uris=None):
        """Resolve given LBRY URIs

        :param str uri: uri to resolve
        :param bool force: force refresh and ignore cache (Optional)
        :param list uris: uris to resolve (Optional)
        :rtype: str
        :return: Dictionary of results, keyed by uri    '<uri>': {            If a resolution error occurs:            'error': Error message            If the uri resolves to a channel or a claim in a channel:            'certificate': {                'address': (str) claim address,                'amount': (float) claim amount,                'effective_amount': (float) claim amount including supports,                'claim_id': (str) claim id,                'claim_sequence': (int) claim sequence number,                'decoded_claim': (bool) whether or not the claim value was decoded,                'height': (int) claim height,                'depth': (int) claim depth,                'has_signature': (bool) included if decoded_claim                'name': (str) claim name,                'permanent_url': (str) permanent url of the certificate claim,                'supports: (list) list of supports [{'txid': (str) txid,                                                     'nout': (int) nout,                                                     'amount': (float) amount}],                'txid': (str) claim txid,                'nout': (str) claim nout,                'signature_is_valid': (bool), included if has_signature,                'value': ClaimDict if decoded, otherwise hex string            }            If the uri resolves to a channel:            'claims_in_channel': (int) number of claims in the channel,            If the uri resolves to a claim:            'claim': {                'address': (str) claim address,                'amount': (float) claim amount,                'effective_amount': (float) claim amount including supports,                'claim_id': (str) claim id,                'claim_sequence': (int) claim sequence number,                'decoded_claim': (bool) whether or not the claim value was decoded,                'height': (int) claim height,                'depth': (int) claim depth,                'has_signature': (bool) included if decoded_claim                'name': (str) claim name,                'permanent_url': (str) permanent url of the claim,                'channel_name': (str) channel name if claim is in a channel                'supports: (list) list of supports [{'txid': (str) txid,                                                     'nout': (int) nout,                                                     'amount': (float) amount}]                'txid': (str) claim txid,                'nout': (str) claim nout,                'signature_is_valid': (bool), included if has_signature,                'value': ClaimDict if decoded, otherwise hex string            }    }Dictionary of results, keyed by uri    '<uri>': {            If a reso
        lution error occurs:            'error': Error message            If t
        he uri resolves to a channel or a claim in a channel:            'cert
        ificate': {                'address': (str) claim address,
            'amount': (float) claim amount,                'effective_amount':
         (float) claim amount including supports,                'claim_id': (
        str) claim id,                'claim_sequence': (int) claim sequence n
        umber,                'decoded_claim': (bool) whether or not the claim
         value was decoded,                'height': (int) claim height,
                  'depth': (int) claim depth,                'has_signature':
        (bool) included if decoded_claim                'name': (str) claim na
        me,                'permanent_url': (str) permanent url of the certifi
        cate claim,                'supports: (list) list of supports [{'txid'
        : (str) txid,                                                     'nou
        t': (int) nout,                                                     'a
        mount': (float) amount}],                'txid': (str) claim txid,
                    'nout': (str) claim nout,                'signature_is_val
        id': (bool), included if has_signature,                'value': ClaimD
        ict if decoded, otherwise hex string            }            If the ur
        i resolves to a channel:            'claims_in_channel': (int) number
        of claims in the channel,            If the uri resolves to a claim:
                  'claim': {                'address': (str) claim address,
                     'amount': (float) claim amount,                'effective
        _amount': (float) claim amount including supports,                'cla
        im_id': (str) claim id,                'claim_sequence': (int) claim s
        equence number,                'decoded_claim': (bool) whether or not
        the claim value was decoded,                'height': (int) claim heig
        ht,                'depth': (int) claim depth,                'has_sig
        nature': (bool) included if decoded_claim                'name': (str)
         claim name,                'permanent_url': (str) permanent url of th
        e claim,                'channel_name': (str) channel name if claim is
         in a channel                'supports: (list) list of supports [{'txi
        d': (str) txid,                                                     'n
        out': (int) nout,
        'amount': (float) amount}]                'txid': (str) claim txid,
                     'nout': (str) claim nout,                'signature_is_va
        lid': (bool), included if has_signature,                'value': Claim
        Dict if decoded, otherwise hex string            }    }
        """
        __params_map = {'uri': uri,
                        'force': force,
                        'uris': uris}

        return self.make_request(SERVER_ADDRESS, 'resolve', __params_map, timeout=self.timeout)

    def resolve_name(self, name, force=None):
        """Resolve stream info from a LBRY name

        :param str name: the name to resolve
        :param bool force: force refresh and do not check cache (Optional)
        :rtype: dict
        :return: (dict) Metadata dictionary from name claim, None if the name is not            resolvable(dict) Metadata dictionary from name claim, None if the name is not
                 resolvable
        """
        __params_map = {'name': name,
                        'force': force}

        return self.make_request(SERVER_ADDRESS, 'resolve_name', __params_map, timeout=self.timeout)

    def routing_table_get(self):
        """Get DHT routing information

        :rtype: dict
        :return: (dict) dictionary containing routing and contact information    {        "buckets": {            <bucket index>: [                {                    "address": (str) peer address,                    "port": (int) peer udp port                    "node_id": (str) peer node id,                    "blobs": (list) blob hashes announced by peer                }            ]        },        "contacts": (list) contact node ids,        "blob_hashes": (list) all of the blob hashes stored by peers in the list of buckets,        "node_id": (str) the local dht node id    }(dict) dictionary containing routing and contact information    {
           "buckets": {            <bucket index>: [                {
                   "address": (str) peer address,                    "port": (
        int) peer udp port                    "node_id": (str) peer node id,
                          "blobs": (list) blob hashes announced by peer
                 }            ]        },        "contacts": (list) contact no
        de ids,        "blob_hashes": (list) all of the blob hashes stored by
        peers in the list of buckets,        "node_id": (str) the local dht no
        de id    }
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'routing_table_get', __params_map, timeout=self.timeout)

    def settings_get(self):
        """Get daemon settings

        :rtype: dict
        :return: (dict) Dictionary of daemon settings    See ADJUSTABLE_SETTINGS in lbrynet/conf.py for full list of settings(dict) Dictionary of daemon settings    See ADJUSTABLE_SETTINGS in lbr
        ynet/conf.py for full list of settings
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'settings_get', __params_map, timeout=self.timeout)

    def settings_set(self, download_directory=None, data_rate=None, download_timeout=None, peer_port=None, max_key_fee=None, disable_max_key_fee=None, use_upnp=None, run_reflector_server=None, cache_time=None, reflect_uploads=None, share_usage_data=None, peer_search_timeout=None, sd_download_timeout=None, auto_renew_claim_height_delta=None):
        """Set daemon settings

        :param str download_directory: path of download directory (Optional)
        :param float data_rate: 0.0001 (Optional)
        :param int download_timeout: 180 (Optional)
        :param int peer_port: 3333 (Optional)
        :param dict max_key_fee: maximum key fee for downloads, in the format: { 'currency': <currency_symbol>, 'amount': <amount> }. In the CLI, it must be an escaped JSON string Supported currency symbols: LBC, USD, BTC (Optional)
        :param bool disable_max_key_fee: False (Optional)
        :param bool use_upnp: True (Optional)
        :param bool run_reflector_server: False (Optional)
        :param int cache_time: 150 (Optional)
        :param bool reflect_uploads: True (Optional)
        :param bool share_usage_data: True (Optional)
        :param int peer_search_timeout: 3 (Optional)
        :param int sd_download_timeout: 3 (Optional)
        :param int auto_renew_claim_height_delta: 0 claims set to expire within this many blocks will be automatically renewed after startup (if set to 0, renews will not be made automatically) (Optional)
        :rtype: dict
        :return: (dict) Updated dictionary of daemon settings(dict) Updated dictionary of daemon settings
        """
        __params_map = {'download_directory': download_directory,
                        'data_rate': data_rate,
                        'download_timeout': download_timeout,
                        'peer_port': peer_port,
                        'max_key_fee': max_key_fee,
                        'disable_max_key_fee': disable_max_key_fee,
                        'use_upnp': use_upnp,
                        'run_reflector_server': run_reflector_server,
                        'cache_time': cache_time,
                        'reflect_uploads': reflect_uploads,
                        'share_usage_data': share_usage_data,
                        'peer_search_timeout': peer_search_timeout,
                        'sd_download_timeout': sd_download_timeout,
                        'auto_renew_claim_height_delta': auto_renew_claim_height_delta}

        return self.make_request(SERVER_ADDRESS, 'settings_set', __params_map, timeout=self.timeout)

    def status(self):
        """Get daemon status

        :rtype: dict
        :return: (dict) lbrynet-daemon status    {        'installation_id': (str) installation id - base58,        'is_running': (bool),        'is_first_run': bool,        'skipped_components': (list) [names of skipped components (str)],        'startup_status': { Does not include components which have been skipped            'database': (bool),            'wallet': (bool),            'session': (bool),            'dht': (bool),            'hash_announcer': (bool),            'stream_identifier': (bool),            'file_manager': (bool),            'blob_manager': (bool),            'blockchain_headers': (bool),            'peer_protocol_server': (bool),            'reflector': (bool),            'upnp': (bool),            'exchange_rate_manager': (bool),        },        'connection_status': {            'code': (str) connection status code,            'message': (str) connection status message        },        'blockchain_headers': {            'downloading_headers': (bool),            'download_progress': (float) 0-100.0        },        'wallet': {            'blocks': (int) local blockchain height,            'blocks_behind': (int) remote_height - local_height,            'best_blockhash': (str) block hash of most recent block,            'is_encrypted': (bool),            'is_locked': (bool),        },        'dht': {            'node_id': (str) lbry dht node id - hex encoded,            'peers_in_routing_table': (int) the number of peers in the routing table,        },        'blob_manager': {            'finished_blobs': (int) number of finished blobs in the blob manager,        },        'hash_announcer': {            'announce_queue_size': (int) number of blobs currently queued to be announced        },        'file_manager': {            'managed_files': (int) count of files in the file manager,        }    }(dict) lbrynet-daemon status    {        'installation_id': (str) inst
        allation id - base58,        'is_running': (bool),        'is_first_ru
        n': bool,        'skipped_components': (list) [names of skipped compon
        ents (str)],        'startup_status': { Does not include components wh
        ich have been skipped            'database': (bool),            'walle
        t': (bool),            'session': (bool),            'dht': (bool),
                 'hash_announcer': (bool),            'stream_identifier': (bo
        ol),            'file_manager': (bool),            'blob_manager': (bo
        ol),            'blockchain_headers': (bool),            'peer_protoco
        l_server': (bool),            'reflector': (bool),            'upnp':
        (bool),            'exchange_rate_manager': (bool),        },        '
        connection_status': {            'code': (str) connection status code,
                    'message': (str) connection status message        },
          'blockchain_headers': {            'downloading_headers': (bool),
                 'download_progress': (float) 0-100.0        },        'wallet
        ': {            'blocks': (int) local blockchain height,            'b
        locks_behind': (int) remote_height - local_height,            'best_bl
        ockhash': (str) block hash of most recent block,            'is_encryp
        ted': (bool),            'is_locked': (bool),        },        'dht':
        {            'node_id': (str) lbry dht node id - hex encoded,
           'peers_in_routing_table': (int) the number of peers in the routing
        table,        },        'blob_manager': {            'finished_blobs':
         (int) number of finished blobs in the blob manager,        },
        'hash_announcer': {            'announce_queue_size': (int) number of
        blobs currently queued to be announced        },        'file_manager'
        : {            'managed_files': (int) count of files in the file manag
        er,        }    }
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'status', __params_map, timeout=self.timeout)

    def stop(self):
        """Stop lbrynet

        :return: (string) Shutdown message(string) Shutdown message
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'stop', __params_map, timeout=self.timeout)

    def stream_availability(self, uri, search_timeout=None, blob_timeout=None):
        """Get stream availability for lbry uri

        :param str uri: check availability for this uri
        :param int search_timeout: how long to search for peers for the blob in the dht (Optional)
        :param int blob_timeout: how long to try downloading from a peer (Optional)
        :rtype: dict
        :return: (dict) {        'is_available': <bool>,        'did_decode': <bool>,        'did_resolve': <bool>,        'is_stream': <bool>,        'num_blobs_in_stream': <int>,        'sd_hash': <str>,        'sd_blob_availability': <dict> see `blob_availability`,        'head_blob_hash': <str>,        'head_blob_availability': <dict> see `blob_availability`,        'use_upnp': <bool>,        'upnp_redirect_is_set': <bool>,        'error': <None> | <str> error message    }(dict) {        'is_available': <bool>,        'did_decode': <bool>,
              'did_resolve': <bool>,        'is_stream': <bool>,        'num_b
        lobs_in_stream': <int>,        'sd_hash': <str>,        'sd_blob_avail
        ability': <dict> see `blob_availability`,        'head_blob_hash': <st
        r>,        'head_blob_availability': <dict> see `blob_availability`,
              'use_upnp': <bool>,        'upnp_redirect_is_set': <bool>,
          'error': <None> | <str> error message    }
        """
        __params_map = {'uri': uri,
                        'search_timeout': search_timeout,
                        'blob_timeout': blob_timeout}

        return self.make_request(SERVER_ADDRESS, 'stream_availability', __params_map, timeout=self.timeout)

    def stream_cost_estimate(self, uri, size=None):
        """Get estimated cost for a lbry stream

        :param str uri: uri to use
        :param float size: stream size in bytes. if provided an sd blob won't be downloaded. (Optional)
        :rtype: float
        :return: (float) Estimated cost in lbry credits, returns None if uri is not        resolvable(float) Estimated cost in lbry credits, returns None if uri is not
            resolvable
        """
        __params_map = {'uri': uri,
                        'size': size}

        return self.make_request(SERVER_ADDRESS, 'stream_cost_estimate', __params_map, timeout=self.timeout)

    def transaction_list(self, account_id=None):
        """List transactions belonging to wallet

        :param str account_id: id of the account to query (Optional)
        :rtype: list
        :return: (list) List of transactions    {        "claim_info": (list) claim info if in txn [{                                                "address": (str) address of claim,                                                "balance_delta": (float) bid amount,                                                "amount": (float) claim amount,                                                "claim_id": (str) claim id,                                                "claim_name": (str) claim name,                                                "nout": (int) nout                                                }],        "abandon_info": (list) abandon info if in txn [{                                                "address": (str) address of abandoned claim,                                                "balance_delta": (float) returned amount,                                                "amount": (float) claim amount,                                                "claim_id": (str) claim id,                                                "claim_name": (str) claim name,                                                "nout": (int) nout                                                }],        "confirmations": (int) number of confirmations for the txn,        "date": (str) date and time of txn,        "fee": (float) txn fee,        "support_info": (list) support info if in txn [{                                                "address": (str) address of support,                                                "balance_delta": (float) support amount,                                                "amount": (float) support amount,                                                "claim_id": (str) claim id,                                                "claim_name": (str) claim name,                                                "is_tip": (bool),                                                "nout": (int) nout                                                }],        "timestamp": (int) timestamp,        "txid": (str) txn id,        "update_info": (list) update info if in txn [{                                                "address": (str) address of claim,                                                "balance_delta": (float) credited/debited                                                "amount": (float) absolute amount,                                                "claim_id": (str) claim id,                                                "claim_name": (str) claim name,                                                "nout": (int) nout                                                }],        "value": (float) value of txn    }(list) List of transactions    {        "claim_info": (list) claim inf
        o if in txn [{                                                "address
        ": (str) address of claim,
            "balance_delta": (float) bid amount,
                          "amount": (float) claim amount,
                                   "claim_id": (str) claim id,
                                        "claim_name": (str) claim name,
                                                 "nout": (int) nout
                                             }],        "abandon_info": (list)
         abandon info if in txn [{
            "address": (str) address of abandoned claim,
                                  "balance_delta": (float) returned amount,
                                                     "amount": (float) claim a
        mount,                                                "claim_id": (str
        ) claim id,                                                "claim_name
        ": (str) claim name,                                                "n
        out": (int) nout                                                }],
             "confirmations": (int) number of confirmations for the txn,
          "date": (str) date and time of txn,        "fee": (float) txn fee,
              "support_info": (list) support info if in txn [{
                                        "address": (str) address of support,
                                                      "balance_delta": (float)
         support amount,                                                "amoun
        t": (float) support amount,
             "claim_id": (str) claim id,
                  "claim_name": (str) claim name,
                           "is_tip": (bool),
                      "nout": (int) nout
                  }],        "timestamp": (int) timestamp,        "txid": (str
        ) txn id,        "update_info": (list) update info if in txn [{
                                                 "address": (str) address of c
        laim,                                                "balance_delta":
        (float) credited/debited
          "amount": (float) absolute amount,
                      "claim_id": (str) claim id,
                           "claim_name": (str) claim name,
                                    "nout": (int) nout
                                }],        "value": (float) value of txn    }
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'transaction_list', __params_map, timeout=self.timeout)

    def transaction_show(self, txid):
        """Get a decoded transaction from a txid

        :param str txid: txid of the transaction
        :rtype: dict
        :return: (dict) JSON formatted transaction(dict) JSON formatted transaction
        """
        __params_map = {'txid': txid}

        return self.make_request(SERVER_ADDRESS, 'transaction_show', __params_map, timeout=self.timeout)

    def utxo_list(self, account_id=None):
        """List unspent transaction outputs

        :param str account_id: id of the account to query (Optional)
        :rtype: list
        :return: (list) List of unspent transaction outputs (UTXOs)    [        {            "address": (str) the output address            "amount": (float) unspent amount            "height": (int) block height            "is_claim": (bool) is the tx a claim            "is_coinbase": (bool) is the tx a coinbase tx            "is_support": (bool) is the tx a support            "is_update": (bool) is the tx an update            "nout": (int) nout of the output            "txid": (str) txid of the output        },        ...    ](list) List of unspent transaction outputs (UTXOs)    [        {
              "address": (str) the output address            "amount": (float)
         unspent amount            "height": (int) block height            "is
        _claim": (bool) is the tx a claim            "is_coinbase": (bool) is
        the tx a coinbase tx            "is_support": (bool) is the tx a suppo
        rt            "is_update": (bool) is the tx an update            "nout
        ": (int) nout of the output            "txid": (str) txid of the outpu
        t        },        ...    ]
        """
        __params_map = {'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'utxo_list', __params_map, timeout=self.timeout)

    def version(self):
        """Get lbry version information

        :rtype: dict
        :return: (dict) Dictionary of lbry version information    {        'build': (str) build type (e.g. "dev", "rc", "release"),        'ip': (str) remote ip, if available,        'lbrynet_version': (str) lbrynet_version,        'lbryum_version': (str) lbryum_version,        'lbryschema_version': (str) lbryschema_version,        'os_release': (str) os release string        'os_system': (str) os name        'platform': (str) platform string        'processor': (str) processor type,        'python_version': (str) python version,    }(dict) Dictionary of lbry version information    {        'build': (st
        r) build type (e.g. "dev", "rc", "release"),        'ip': (str) remote
         ip, if available,        'lbrynet_version': (str) lbrynet_version,
             'lbryum_version': (str) lbryum_version,        'lbryschema_versio
        n': (str) lbryschema_version,        'os_release': (str) os release st
        ring        'os_system': (str) os name        'platform': (str) platfo
        rm string        'processor': (str) processor type,        'python_ver
        sion': (str) python version,    }
        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'version', __params_map, timeout=self.timeout)

    def wallet_prefill_addresses(self, num_addresses, amount, no_broadcast=None):
        """Create new UTXOs, each containing `amount` credits

        :param int num_addresses: num of addresses to create
        :param float amount: initial amount in each address
        :param bool no_broadcast: whether to broadcast or not (Optional)
        :rtype: dict
        :return: (dict) the resulting transaction(dict) the resulting transaction
        """
        __params_map = {'num_addresses': num_addresses,
                        'amount': amount,
                        'no_broadcast': no_broadcast}

        return self.make_request(SERVER_ADDRESS, 'wallet_prefill_addresses', __params_map, timeout=self.timeout)

    def wallet_send(self, amount, address, claim_id, account_id=None):
        """Send credits. If given an address, send credits to it. If given a claim id, send a tip
to the owner of a claim specified by uri. A tip is a claim support where the recipient
of the support is the claim address for the claim being supported.

        :param float amount: amount of credit to send
        :param str address: address to send credits to
        :param str claim_id: claim_id of the claim to send to tip to
        :param str account_id: account to fund the transaction (Optional)
        :rtype: dict
        :return: If sending to an address:    (dict) Dictionary containing the transaction information    {        "hex": (str) raw transaction,        "inputs": (list) inputs(dict) used for the transaction,        "outputs": (list) outputs(dict) for the transaction,        "total_fee": (int) fee in dewies,        "total_input": (int) total of inputs in dewies,        "total_output": (int) total of outputs in dewies(input - fees),        "txid": (str) txid of the transaction,    }    If sending a claim tip:    (dict) Dictionary containing the result of the support    {        txid : (str) txid of resulting support claim        nout : (int) nout of the resulting support claim        fee : (float) fee paid for the transaction    }If sending to an address:    (dict) Dictionary containing the transact
        ion information    {        "hex": (str) raw transaction,        "inpu
        ts": (list) inputs(dict) used for the transaction,        "outputs": (
        list) outputs(dict) for the transaction,        "total_fee": (int) fee
         in dewies,        "total_input": (int) total of inputs in dewies,
            "total_output": (int) total of outputs in dewies(input - fees),
             "txid": (str) txid of the transaction,    }    If sending a claim
         tip:    (dict) Dictionary containing the result of the support    {
              txid : (str) txid of resulting support claim        nout : (int)
         nout of the resulting support claim        fee : (float) fee paid for
         the transaction    }
        """
        __params_map = {'amount': amount,
                        'address': address,
                        'claim_id': claim_id,
                        'account_id': account_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_send', __params_map, timeout=self.timeout)

