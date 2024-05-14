# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.inspection_statistics import InspectionStatistics


class TestInspectionStatistics(unittest.TestCase):
    """InspectionStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InspectionStatistics:
        """Test InspectionStatistics
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InspectionStatistics`
        """
        model = InspectionStatistics()
        if include_optional:
            return InspectionStatistics(
                total_inspections = 56,
                closed_inspections = 56,
                opened_inspections = 56,
                validation_requests = 56
            )
        else:
            return InspectionStatistics(
                total_inspections = 56,
                closed_inspections = 56,
                opened_inspections = 56,
                validation_requests = 56,
        )
        """

    def testInspectionStatistics(self):
        """Test InspectionStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
