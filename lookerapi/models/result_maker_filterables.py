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


class ResultMakerFilterables(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, model=None, view=None, name=None, listen=None, can=None):
        """
        ResultMakerFilterables - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'model': 'str',
            'view': 'str',
            'name': 'str',
            'listen': 'list[ResultMakerFilterablesListen]',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'model': 'model',
            'view': 'view',
            'name': 'name',
            'listen': 'listen',
            'can': 'can'
        }

        self._model = model
        self._view = view
        self._name = name
        self._listen = listen
        self._can = can

    @property
    def model(self):
        """
        Gets the model of this ResultMakerFilterables.
        The model this filterable comes from (used for field suggestions).

        :return: The model of this ResultMakerFilterables.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ResultMakerFilterables.
        The model this filterable comes from (used for field suggestions).

        :param model: The model of this ResultMakerFilterables.
        :type: str
        """

        self._model = model

    @property
    def view(self):
        """
        Gets the view of this ResultMakerFilterables.
        The view this filterable comes from (used for field suggestions).

        :return: The view of this ResultMakerFilterables.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this ResultMakerFilterables.
        The view this filterable comes from (used for field suggestions).

        :param view: The view of this ResultMakerFilterables.
        :type: str
        """

        self._view = view

    @property
    def name(self):
        """
        Gets the name of this ResultMakerFilterables.
        The name of the filterable thing (Query or Merged Results).

        :return: The name of this ResultMakerFilterables.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResultMakerFilterables.
        The name of the filterable thing (Query or Merged Results).

        :param name: The name of this ResultMakerFilterables.
        :type: str
        """

        self._name = name

    @property
    def listen(self):
        """
        Gets the listen of this ResultMakerFilterables.
        array of dashboard_filter_name: and field: objects.

        :return: The listen of this ResultMakerFilterables.
        :rtype: list[ResultMakerFilterablesListen]
        """
        return self._listen

    @listen.setter
    def listen(self, listen):
        """
        Sets the listen of this ResultMakerFilterables.
        array of dashboard_filter_name: and field: objects.

        :param listen: The listen of this ResultMakerFilterables.
        :type: list[ResultMakerFilterablesListen]
        """

        self._listen = listen

    @property
    def can(self):
        """
        Gets the can of this ResultMakerFilterables.
        Operations the current user is able to perform on this object

        :return: The can of this ResultMakerFilterables.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this ResultMakerFilterables.
        Operations the current user is able to perform on this object

        :param can: The can of this ResultMakerFilterables.
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
        if not isinstance(other, ResultMakerFilterables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other