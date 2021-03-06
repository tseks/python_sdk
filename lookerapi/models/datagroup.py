# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Datagroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, model_name=None, trigger_value=None, trigger_error=None, stale_before=None, triggered_at=None, trigger_check_at=None, created_at=None, can=None):
        """
        Datagroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'model_name': 'str',
            'trigger_value': 'str',
            'trigger_error': 'str',
            'stale_before': 'int',
            'triggered_at': 'int',
            'trigger_check_at': 'int',
            'created_at': 'int',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'model_name': 'model_name',
            'trigger_value': 'trigger_value',
            'trigger_error': 'trigger_error',
            'stale_before': 'stale_before',
            'triggered_at': 'triggered_at',
            'trigger_check_at': 'trigger_check_at',
            'created_at': 'created_at',
            'can': 'can'
        }

        self._id = id
        self._name = name
        self._model_name = model_name
        self._trigger_value = trigger_value
        self._trigger_error = trigger_error
        self._stale_before = stale_before
        self._triggered_at = triggered_at
        self._trigger_check_at = trigger_check_at
        self._created_at = created_at
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this Datagroup.
        ID of the datagroup. Also used as the unique identifier.

        :return: The id of this Datagroup.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Datagroup.
        ID of the datagroup. Also used as the unique identifier.

        :param id: The id of this Datagroup.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Datagroup.
        Name of the datagroup. Unique when combined with model_name.

        :return: The name of this Datagroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Datagroup.
        Name of the datagroup. Unique when combined with model_name.

        :param name: The name of this Datagroup.
        :type: str
        """

        self._name = name

    @property
    def model_name(self):
        """
        Gets the model_name of this Datagroup.
        Name of the model containing the datagroup. Unique when combined with name.

        :return: The model_name of this Datagroup.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """
        Sets the model_name of this Datagroup.
        Name of the model containing the datagroup. Unique when combined with name.

        :param model_name: The model_name of this Datagroup.
        :type: str
        """

        self._model_name = model_name

    @property
    def trigger_value(self):
        """
        Gets the trigger_value of this Datagroup.
        The value of the trigger when last checked.

        :return: The trigger_value of this Datagroup.
        :rtype: str
        """
        return self._trigger_value

    @trigger_value.setter
    def trigger_value(self, trigger_value):
        """
        Sets the trigger_value of this Datagroup.
        The value of the trigger when last checked.

        :param trigger_value: The trigger_value of this Datagroup.
        :type: str
        """

        self._trigger_value = trigger_value

    @property
    def trigger_error(self):
        """
        Gets the trigger_error of this Datagroup.
        The message returned with the error of the last trigger check.

        :return: The trigger_error of this Datagroup.
        :rtype: str
        """
        return self._trigger_error

    @trigger_error.setter
    def trigger_error(self, trigger_error):
        """
        Sets the trigger_error of this Datagroup.
        The message returned with the error of the last trigger check.

        :param trigger_error: The trigger_error of this Datagroup.
        :type: str
        """

        self._trigger_error = trigger_error

    @property
    def stale_before(self):
        """
        Gets the stale_before of this Datagroup.
        UNIX timestamp before which cache entries are considered stale. Cannot be in the future.

        :return: The stale_before of this Datagroup.
        :rtype: int
        """
        return self._stale_before

    @stale_before.setter
    def stale_before(self, stale_before):
        """
        Sets the stale_before of this Datagroup.
        UNIX timestamp before which cache entries are considered stale. Cannot be in the future.

        :param stale_before: The stale_before of this Datagroup.
        :type: int
        """

        self._stale_before = stale_before

    @property
    def triggered_at(self):
        """
        Gets the triggered_at of this Datagroup.
        UNIX timestamp at which this entry became triggered. Cannot be in the future.

        :return: The triggered_at of this Datagroup.
        :rtype: int
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        """
        Sets the triggered_at of this Datagroup.
        UNIX timestamp at which this entry became triggered. Cannot be in the future.

        :param triggered_at: The triggered_at of this Datagroup.
        :type: int
        """

        self._triggered_at = triggered_at

    @property
    def trigger_check_at(self):
        """
        Gets the trigger_check_at of this Datagroup.
        UNIX timestamp at which this entry trigger was last checked.

        :return: The trigger_check_at of this Datagroup.
        :rtype: int
        """
        return self._trigger_check_at

    @trigger_check_at.setter
    def trigger_check_at(self, trigger_check_at):
        """
        Sets the trigger_check_at of this Datagroup.
        UNIX timestamp at which this entry trigger was last checked.

        :param trigger_check_at: The trigger_check_at of this Datagroup.
        :type: int
        """

        self._trigger_check_at = trigger_check_at

    @property
    def created_at(self):
        """
        Gets the created_at of this Datagroup.
        UNIX timestamp at which this entry was created.

        :return: The created_at of this Datagroup.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Datagroup.
        UNIX timestamp at which this entry was created.

        :param created_at: The created_at of this Datagroup.
        :type: int
        """

        self._created_at = created_at

    @property
    def can(self):
        """
        Gets the can of this Datagroup.
        Operations the current user is able to perform on this object

        :return: The can of this Datagroup.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Datagroup.
        Operations the current user is able to perform on this object

        :param can: The can of this Datagroup.
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Datagroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
