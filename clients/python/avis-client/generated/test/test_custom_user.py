# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.custom_user import CustomUser


class TestCustomUser(unittest.TestCase):
    """CustomUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomUser:
        """Test CustomUser
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CustomUser`
        """
        model = CustomUser()
        if include_optional:
            return CustomUser(
                id = 56,
                first_name = '',
                last_name = '',
                email = ''
            )
        else:
            return CustomUser(
                id = 56,
        )
        """

    def testCustomUser(self):
        """Test CustomUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
