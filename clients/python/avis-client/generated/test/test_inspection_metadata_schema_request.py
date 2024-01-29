# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from vue_avis_client.models.inspection_metadata_schema_request import InspectionMetadataSchemaRequest

class TestInspectionMetadataSchemaRequest(unittest.TestCase):
    """InspectionMetadataSchemaRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InspectionMetadataSchemaRequest:
        """Test InspectionMetadataSchemaRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InspectionMetadataSchemaRequest`
        """
        model = InspectionMetadataSchemaRequest()
        if include_optional:
            return InspectionMetadataSchemaRequest(
                team = 56,
                var_json = None
            )
        else:
            return InspectionMetadataSchemaRequest(
                team = 56,
                var_json = None,
        )
        """

    def testInspectionMetadataSchemaRequest(self):
        """Test InspectionMetadataSchemaRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
