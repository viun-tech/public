# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.inspection_process_blueprint_request import (
    InspectionProcessBlueprintRequest,
)


class TestInspectionProcessBlueprintRequest(unittest.TestCase):
    """InspectionProcessBlueprintRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InspectionProcessBlueprintRequest:
        """Test InspectionProcessBlueprintRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InspectionProcessBlueprintRequest`
        """
        model = InspectionProcessBlueprintRequest()
        if include_optional:
            return InspectionProcessBlueprintRequest(
                team = 56,
                name = '0',
                metadata_schema = 56,
                image_quality_gate = 56,
                ml_model = 56,
                inspection_object_type = 56,
                description = ''
            )
        else:
            return InspectionProcessBlueprintRequest(
                team = 56,
                name = '0',
        )
        """

    def testInspectionProcessBlueprintRequest(self):
        """Test InspectionProcessBlueprintRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
