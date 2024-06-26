# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.inspection_request import InspectionRequest


class TestInspectionRequest(unittest.TestCase):
    """InspectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InspectionRequest:
        """Test InspectionRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InspectionRequest`
        """
        model = InspectionRequest()
        if include_optional:
            return InspectionRequest(
                team = 56,
                product = 56,
                opened_by = 56,
                closed_by = 56,
                images = [
                    56
                    ],
                close_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                configuration = 56,
                metadata = 56
            )
        else:
            return InspectionRequest(
                team = 56,
        )
        """

    def testInspectionRequest(self):
        """Test InspectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
