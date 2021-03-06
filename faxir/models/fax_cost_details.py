# coding: utf-8

"""
    FAX.IR REST API

    This is the fax.ir API v2 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:<br /><br /> - This API assumes **/accounts** as an entry point with the base url of **https://api.fax.ir/v2**. <br /><br /> - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**<br /><br /> - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://api.fax.ir/v2** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://api.fax.ir/v2/accounts/self** when **Authorization** header is set to \"Bearer YOUR_ACCESS_TOKEN\" and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FaxCostDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'notification_cost': 'int',
        'multiplier': 'int'
    }

    attribute_map = {
        'notification_cost': 'notification_cost',
        'multiplier': 'multiplier'
    }

    def __init__(self, notification_cost=None, multiplier=None):  # noqa: E501
        """FaxCostDetails - a model defined in Swagger"""  # noqa: E501

        self._notification_cost = None
        self._multiplier = None
        self.discriminator = None

        if notification_cost is not None:
            self.notification_cost = notification_cost
        if multiplier is not None:
            self.multiplier = multiplier

    @property
    def notification_cost(self):
        """Gets the notification_cost of this FaxCostDetails.  # noqa: E501


        :return: The notification_cost of this FaxCostDetails.  # noqa: E501
        :rtype: int
        """
        return self._notification_cost

    @notification_cost.setter
    def notification_cost(self, notification_cost):
        """Sets the notification_cost of this FaxCostDetails.


        :param notification_cost: The notification_cost of this FaxCostDetails.  # noqa: E501
        :type: int
        """

        self._notification_cost = notification_cost

    @property
    def multiplier(self):
        """Gets the multiplier of this FaxCostDetails.  # noqa: E501


        :return: The multiplier of this FaxCostDetails.  # noqa: E501
        :rtype: int
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this FaxCostDetails.


        :param multiplier: The multiplier of this FaxCostDetails.  # noqa: E501
        :type: int
        """

        self._multiplier = multiplier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FaxCostDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
