# coding: utf-8

"""
    FAX.IR REST API

    This is the fax.ir API v2 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:<br /><br /> - This API assumes **/accounts** as an entry point with the base url of **https://api.fax.ir/v2**. <br /><br /> - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**<br /><br /> - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://api.fax.ir/v2** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://api.fax.ir/v2/accounts/self** when **Authorization** header is set to \"Bearer YOUR_ACCESS_TOKEN\" and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from faxir.api_client import ApiClient


class NumbersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_number(self, number, **kwargs):  # noqa: E501
        """Get number information  # noqa: E501

        Get info of a single number  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_number(number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :return: Number
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_number_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_number_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def get_number_with_http_info(self, number, **kwargs):  # noqa: E501
        """Get number information  # noqa: E501

        Get info of a single number  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_number_with_http_info(number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :return: Number
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `get_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['fax_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/self/numbers/{number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Number',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_numbers(self, **kwargs):  # noqa: E501
        """Get your numbers  # noqa: E501

        List all your purchased numbers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_numbers(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ResponseNumberList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """Get your numbers  # noqa: E501

        List all your purchased numbers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_numbers_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ResponseNumberList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_numbers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['fax_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/self/numbers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseNumberList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revoke_number(self, number, **kwargs):  # noqa: E501
        """Revoke number  # noqa: E501

        Revoke a specific number from your corporate member  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.revoke_number(number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.revoke_number_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_number_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def revoke_number_with_http_info(self, number, **kwargs):  # noqa: E501
        """Revoke number  # noqa: E501

        Revoke a specific number from your corporate member  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.revoke_number_with_http_info(number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `revoke_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['fax_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/self/numbers/{number}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_number(self, number, payload_number_modification, **kwargs):  # noqa: E501
        """Assign number  # noqa: E501

        With this API call you will be able to assign a specific number to a specific account (one of your members).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_number(number, payload_number_modification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :param PayloadNumberModification payload_number_modification: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_number_with_http_info(number, payload_number_modification, **kwargs)  # noqa: E501
        else:
            (data) = self.update_number_with_http_info(number, payload_number_modification, **kwargs)  # noqa: E501
            return data

    def update_number_with_http_info(self, number, payload_number_modification, **kwargs):  # noqa: E501
        """Assign number  # noqa: E501

        With this API call you will be able to assign a specific number to a specific account (one of your members).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_number_with_http_info(number, payload_number_modification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str number: (required)
        :param PayloadNumberModification payload_number_modification: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number', 'payload_number_modification']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if ('number' not in params or
                params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `update_number`")  # noqa: E501
        # verify the required parameter 'payload_number_modification' is set
        if ('payload_number_modification' not in params or
                params['payload_number_modification'] is None):
            raise ValueError("Missing the required parameter `payload_number_modification` when calling `update_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload_number_modification' in params:
            body_params = params['payload_number_modification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['fax_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/self/numbers/{number}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
