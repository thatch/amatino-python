"""
Amatino API Python Bindings
API Request Module
Author: hugh@amatino.io

This module is intended to be private, used indirectly
by public classes, and should not be used directly.
"""
from json import loads
from urllib.request import Request
from urllib.request import urlopen
from urllib.request import HTTPError
from amatino.internal.credentials import Credentials
from amatino.internal.data_package import DataPackage
from amatino.internal.url_parameters import UrlParameters
from amatino.internal.request_headers import RequestHeaders
from amatino.internal.http_method import HTTPMethod
from typing import Optional


class ApiRequest:
    """
    Private - Not intended to be used directly.

    An instance of an http request to the Amatino API.
    """

    _ENDPOINT = 'https://api.amatino.io'
    _DEBUG_ENDPOINT = 'http://127.0.0.1:5000'
    _TIMEOUT = 5

    def __init__(
        self,
        path: str,
        method: HTTPMethod,
        credentials: Optional[Credentials] = None,
        data: Optional[DataPackage] = None,
        url_parameters: Optional[UrlParameters] = None,
        debug: bool = False
    ) -> None:

        self.response_data = None

        if credentials is not None:
            assert isinstance(credentials, Credentials)

        if data is not None:
            assert isinstance(data, DataPackage)
            request_data = data.as_json_bytes()
        else:
            request_data = None

        if url_parameters is not None:
            assert isinstance(url_parameters, UrlParameters)

        if debug is False:
            url = self._ENDPOINT
        else:
            url = self._DEBUG_ENDPOINT

        url += path

        if url_parameters is not None:
            url += url_parameters.parameter_string()

        headers = RequestHeaders(path, credentials, data)
        request = Request(
            url=url,
            data=request_data,
            headers=headers.dictionary(),
            method=method.value,
        )
        try:
            self._response = urlopen(request, timeout=self._TIMEOUT)
        except HTTPError as error:
            # Insert error handling
            raise error

        self.response_data = loads(self._response.read().decode('utf-8'))

        return
