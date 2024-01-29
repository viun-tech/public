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

from vue_avis_client.models.patched_rating_inspection_result_request import PatchedRatingInspectionResultRequest

class TestPatchedRatingInspectionResultRequest(unittest.TestCase):
    """PatchedRatingInspectionResultRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedRatingInspectionResultRequest:
        """Test PatchedRatingInspectionResultRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedRatingInspectionResultRequest`
        """
        model = PatchedRatingInspectionResultRequest()
        if include_optional:
            return PatchedRatingInspectionResultRequest(
                team = 56,
                reported_by = 56,
                image = 56,
                type = 'RatingInspectionResult',
                confidence = '-8',
                comment = '',
                rating = '-8072'
            )
        else:
            return PatchedRatingInspectionResultRequest(
        )
        """

    def testPatchedRatingInspectionResultRequest(self):
        """Test PatchedRatingInspectionResultRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
