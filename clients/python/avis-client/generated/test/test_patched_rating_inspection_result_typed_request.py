# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.patched_rating_inspection_result_typed_request import (
    PatchedRatingInspectionResultTypedRequest,
)


class TestPatchedRatingInspectionResultTypedRequest(unittest.TestCase):
    """PatchedRatingInspectionResultTypedRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PatchedRatingInspectionResultTypedRequest:
        """Test PatchedRatingInspectionResultTypedRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedRatingInspectionResultTypedRequest`
        """
        model = PatchedRatingInspectionResultTypedRequest()
        if include_optional:
            return PatchedRatingInspectionResultTypedRequest(
                team = 56,
                reported_by = 56,
                image = 56,
                type = '',
                confidence = '-8',
                comment = '',
                rating = '-8072'
            )
        else:
            return PatchedRatingInspectionResultTypedRequest(
        )
        """

    def testPatchedRatingInspectionResultTypedRequest(self):
        """Test PatchedRatingInspectionResultTypedRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
