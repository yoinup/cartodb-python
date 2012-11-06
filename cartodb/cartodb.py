# coding=utf-8

from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

import warnings
from urllib import quote_plus

try:
    import json
except ImportError:
    import simplejson as json


RESOURCE_URL = '%(protocol)s://%(user)s.%(domain)s/api/%(api_version)s/sql/'


class CartoDBException(Exception):
    pass


class CartoDBBase(object):
    """ basic client to access cartodb api """
    MAX_GET_QUERY_LEN = 2048

    def __init__(
            self, cartodb_domain, host='cartodb.com',
            protocol='https', api_version='v2'):
        self.resource_url = RESOURCE_URL % {
            'user': cartodb_domain,
            'domain': host,
            'protocol': protocol,
            'api_version': api_version}

    def req(self, url, http_method="GET", http_headers=None, body=''):
        """
        this method should implement
        how to send a request to server using propper auth
        """
        raise NotImplementedError('req method must be implemented')

    def sql(self, sql, parse_json=True, do_post=True):
        """
        executes sql in cartodb server
        set parse_json to False if you want raw reponse
        """
        url = URL(self.resource_url)
        # depending on query size do a POST or GET
        if len(sql) < self.MAX_GET_QUERY_LEN and not do_post:
            url['q'] = sql
            resp = self.req(url)
        else:
            resp = self.req(url, 'POST', body="q=%s" % quote_plus(sql))
        content = resp.read()
        if resp.status_code == 200:
            if parse_json:
                return json.loads(content)
            return content
        elif resp.status_code == 400:
            raise CartoDBException(json.loads(content)['error'])
        elif resp.status_code == 500:
            raise CartoDBException('internal server error')
        return None


class CartoDBAPIKey(CartoDBBase):
    """
    this class provides you access to auth CartoDB API using your API.
    You can find your API key in:
        https://USERNAME.cartodb.com/your_apps/api_key.
    this method is easier than use the oauth authentification but if
    less secure, it is recommended to use only using the https endpoint
    """

    def __init__(
            self, api_key, cartodb_domain, host='cartodb.com',
            protocol='https', proxy_info=None, *args, **kwargs):
        super(CartoDBAPIKey, self).__init__(
            cartodb_domain, host, protocol, *args, **kwargs)
        self.api_key = api_key
        self.client = HTTPClient(
            '.'.join([cartodb_domain, host]),
            connection_timeout=10.0,
            network_timeout=10.0,
            ssl=protocol == 'https')
        if protocol != 'https':
            warnings.warn("you are using API key auth method with http")

    def req(self, url, http_method="GET", http_headers={}, body=''):
        if http_method == "POST":
            body = body + '&api_key=%s' % self.api_key
            headers = {'Content-type': 'application/x-www-form-urlencoded'}
            headers.update(http_headers)
            resp = self.client.post(
                url.request_uri, body=body, headers=headers)
        else:
            url['api_key'] = self.api_key
            resp = self.client.get(url.request_uri, headers=http_headers)
        return resp
