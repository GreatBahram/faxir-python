# faxir.NumbersApi

All URIs are relative to *https://api.fax.ir/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_number**](NumbersApi.md#get_number) | **GET** /accounts/self/numbers/{number} | Get number information
[**list_numbers**](NumbersApi.md#list_numbers) | **GET** /accounts/self/numbers | Get your numbers
[**revoke_number**](NumbersApi.md#revoke_number) | **DELETE** /accounts/self/numbers/{number} | Revoke number
[**update_number**](NumbersApi.md#update_number) | **PUT** /accounts/self/numbers/{number} | Assign number


# **get_number**
> Number get_number(number)

Get number information

Get info of a single number

### Example
```python
from __future__ import print_function
import time
import faxir
from faxir.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxir.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxir.NumbersApi(faxir.ApiClient(configuration))
number = 'number_example' # str | 

try:
    # Get number information
    api_response = api_instance.get_number(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->get_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**|  | 

### Return type

[**Number**](Number.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_numbers**
> ResponseNumberList list_numbers()

Get your numbers

List all your purchased numbers

### Example
```python
from __future__ import print_function
import time
import faxir
from faxir.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxir.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxir.NumbersApi(faxir.ApiClient(configuration))

try:
    # Get your numbers
    api_response = api_instance.list_numbers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumbersApi->list_numbers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseNumberList**](ResponseNumberList.md)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_number**
> revoke_number(number)

Revoke number

Revoke a specific number from your corporate member

### Example
```python
from __future__ import print_function
import time
import faxir
from faxir.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxir.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxir.NumbersApi(faxir.ApiClient(configuration))
number = 'number_example' # str | 

try:
    # Revoke number
    api_instance.revoke_number(number)
except ApiException as e:
    print("Exception when calling NumbersApi->revoke_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_number**
> update_number(number, payload_number_modification)

Assign number

With this API call you will be able to assign a specific number to a specific account (one of your members).

### Example
```python
from __future__ import print_function
import time
import faxir
from faxir.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: fax_oauth
configuration = faxir.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = faxir.NumbersApi(faxir.ApiClient(configuration))
number = 'number_example' # str | 
payload_number_modification = faxir.PayloadNumberModification() # PayloadNumberModification | 

try:
    # Assign number
    api_instance.update_number(number, payload_number_modification)
except ApiException as e:
    print("Exception when calling NumbersApi->update_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**|  | 
 **payload_number_modification** | [**PayloadNumberModification**](PayloadNumberModification.md)|  | 

### Return type

void (empty response body)

### Authorization

[fax_oauth](../README.md#fax_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

