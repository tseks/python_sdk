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


class GitBranch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, remote=None, remote_name=None, error=None, message=None, owner_name=None, readonly=None, personal=None, is_local=None, is_remote=None, is_production=None, ahead_count=None, behind_count=None, commit_at=None, can=None):
        """
        GitBranch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'remote': 'str',
            'remote_name': 'str',
            'error': 'str',
            'message': 'str',
            'owner_name': 'str',
            'readonly': 'bool',
            'personal': 'bool',
            'is_local': 'bool',
            'is_remote': 'bool',
            'is_production': 'bool',
            'ahead_count': 'int',
            'behind_count': 'int',
            'commit_at': 'int',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'name': 'name',
            'remote': 'remote',
            'remote_name': 'remote_name',
            'error': 'error',
            'message': 'message',
            'owner_name': 'owner_name',
            'readonly': 'readonly',
            'personal': 'personal',
            'is_local': 'is_local',
            'is_remote': 'is_remote',
            'is_production': 'is_production',
            'ahead_count': 'ahead_count',
            'behind_count': 'behind_count',
            'commit_at': 'commit_at',
            'can': 'can'
        }

        self._name = name
        self._remote = remote
        self._remote_name = remote_name
        self._error = error
        self._message = message
        self._owner_name = owner_name
        self._readonly = readonly
        self._personal = personal
        self._is_local = is_local
        self._is_remote = is_remote
        self._is_production = is_production
        self._ahead_count = ahead_count
        self._behind_count = behind_count
        self._commit_at = commit_at
        self._can = can

    @property
    def name(self):
        """
        Gets the name of this GitBranch.
        The short name on the local

        :return: The name of this GitBranch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GitBranch.
        The short name on the local

        :param name: The name of this GitBranch.
        :type: str
        """

        self._name = name

    @property
    def remote(self):
        """
        Gets the remote of this GitBranch.
        The name of the remote

        :return: The remote of this GitBranch.
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """
        Sets the remote of this GitBranch.
        The name of the remote

        :param remote: The remote of this GitBranch.
        :type: str
        """

        self._remote = remote

    @property
    def remote_name(self):
        """
        Gets the remote_name of this GitBranch.
        The short name on the remote

        :return: The remote_name of this GitBranch.
        :rtype: str
        """
        return self._remote_name

    @remote_name.setter
    def remote_name(self, remote_name):
        """
        Sets the remote_name of this GitBranch.
        The short name on the remote

        :param remote_name: The remote_name of this GitBranch.
        :type: str
        """

        self._remote_name = remote_name

    @property
    def error(self):
        """
        Gets the error of this GitBranch.
        Name of error

        :return: The error of this GitBranch.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this GitBranch.
        Name of error

        :param error: The error of this GitBranch.
        :type: str
        """

        self._error = error

    @property
    def message(self):
        """
        Gets the message of this GitBranch.
        Message describing an error if present

        :return: The message of this GitBranch.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this GitBranch.
        Message describing an error if present

        :param message: The message of this GitBranch.
        :type: str
        """

        self._message = message

    @property
    def owner_name(self):
        """
        Gets the owner_name of this GitBranch.
        Name of the owner of a personal branch

        :return: The owner_name of this GitBranch.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """
        Sets the owner_name of this GitBranch.
        Name of the owner of a personal branch

        :param owner_name: The owner_name of this GitBranch.
        :type: str
        """

        self._owner_name = owner_name

    @property
    def readonly(self):
        """
        Gets the readonly of this GitBranch.
        Whether or not this branch is readonly

        :return: The readonly of this GitBranch.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """
        Sets the readonly of this GitBranch.
        Whether or not this branch is readonly

        :param readonly: The readonly of this GitBranch.
        :type: bool
        """

        self._readonly = readonly

    @property
    def personal(self):
        """
        Gets the personal of this GitBranch.
        Whether or not this branch is a personal branch - readonly for all developers except the owner

        :return: The personal of this GitBranch.
        :rtype: bool
        """
        return self._personal

    @personal.setter
    def personal(self, personal):
        """
        Sets the personal of this GitBranch.
        Whether or not this branch is a personal branch - readonly for all developers except the owner

        :param personal: The personal of this GitBranch.
        :type: bool
        """

        self._personal = personal

    @property
    def is_local(self):
        """
        Gets the is_local of this GitBranch.
        Whether or not a local ref exists for the branch

        :return: The is_local of this GitBranch.
        :rtype: bool
        """
        return self._is_local

    @is_local.setter
    def is_local(self, is_local):
        """
        Sets the is_local of this GitBranch.
        Whether or not a local ref exists for the branch

        :param is_local: The is_local of this GitBranch.
        :type: bool
        """

        self._is_local = is_local

    @property
    def is_remote(self):
        """
        Gets the is_remote of this GitBranch.
        Whether or not a remote ref exists for the branch

        :return: The is_remote of this GitBranch.
        :rtype: bool
        """
        return self._is_remote

    @is_remote.setter
    def is_remote(self, is_remote):
        """
        Sets the is_remote of this GitBranch.
        Whether or not a remote ref exists for the branch

        :param is_remote: The is_remote of this GitBranch.
        :type: bool
        """

        self._is_remote = is_remote

    @property
    def is_production(self):
        """
        Gets the is_production of this GitBranch.
        Whether or not this is the production branch

        :return: The is_production of this GitBranch.
        :rtype: bool
        """
        return self._is_production

    @is_production.setter
    def is_production(self, is_production):
        """
        Sets the is_production of this GitBranch.
        Whether or not this is the production branch

        :param is_production: The is_production of this GitBranch.
        :type: bool
        """

        self._is_production = is_production

    @property
    def ahead_count(self):
        """
        Gets the ahead_count of this GitBranch.
        Number of commits the local branch is ahead of the remote

        :return: The ahead_count of this GitBranch.
        :rtype: int
        """
        return self._ahead_count

    @ahead_count.setter
    def ahead_count(self, ahead_count):
        """
        Sets the ahead_count of this GitBranch.
        Number of commits the local branch is ahead of the remote

        :param ahead_count: The ahead_count of this GitBranch.
        :type: int
        """

        self._ahead_count = ahead_count

    @property
    def behind_count(self):
        """
        Gets the behind_count of this GitBranch.
        Number of commits the local branch is behind the remote

        :return: The behind_count of this GitBranch.
        :rtype: int
        """
        return self._behind_count

    @behind_count.setter
    def behind_count(self, behind_count):
        """
        Sets the behind_count of this GitBranch.
        Number of commits the local branch is behind the remote

        :param behind_count: The behind_count of this GitBranch.
        :type: int
        """

        self._behind_count = behind_count

    @property
    def commit_at(self):
        """
        Gets the commit_at of this GitBranch.
        UNIX timestamp at which this branch was last committed.

        :return: The commit_at of this GitBranch.
        :rtype: int
        """
        return self._commit_at

    @commit_at.setter
    def commit_at(self, commit_at):
        """
        Sets the commit_at of this GitBranch.
        UNIX timestamp at which this branch was last committed.

        :param commit_at: The commit_at of this GitBranch.
        :type: int
        """

        self._commit_at = commit_at

    @property
    def can(self):
        """
        Gets the can of this GitBranch.
        Operations the current user is able to perform on this object

        :return: The can of this GitBranch.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this GitBranch.
        Operations the current user is able to perform on this object

        :param can: The can of this GitBranch.
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
        if not isinstance(other, GitBranch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
