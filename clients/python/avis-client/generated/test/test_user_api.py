# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_user_email_list(self) -> None:
        """Test case for user_email_list

        """
        pass

    def test_user_whoami_retrieve(self) -> None:
        """Test case for user_whoami_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
