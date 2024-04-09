# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from avis_client.models.inspection_images_statistics_request import InspectionImagesStatisticsRequest

class TestInspectionImagesStatisticsRequest(unittest.TestCase):
    """InspectionImagesStatisticsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InspectionImagesStatisticsRequest:
        """Test InspectionImagesStatisticsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InspectionImagesStatisticsRequest`
        """
        model = InspectionImagesStatisticsRequest()
        if include_optional:
            return InspectionImagesStatisticsRequest(
                total_images = 56,
                images_to_inspect = 56
            )
        else:
            return InspectionImagesStatisticsRequest(
                total_images = 56,
                images_to_inspect = 56,
        )
        """

    def testInspectionImagesStatisticsRequest(self):
        """Test InspectionImagesStatisticsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
