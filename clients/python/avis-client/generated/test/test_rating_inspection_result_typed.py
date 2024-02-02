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

from vue_avis_client.models.rating_inspection_result_typed import RatingInspectionResultTyped

class TestRatingInspectionResultTyped(unittest.TestCase):
    """RatingInspectionResultTyped unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RatingInspectionResultTyped:
        """Test RatingInspectionResultTyped
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RatingInspectionResultTyped`
        """
        model = RatingInspectionResultTyped()
        if include_optional:
            return RatingInspectionResultTyped(
                id = 56,
                team = 56,
                reported_by = 56,
                image = 56,
                type = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                confidence = '-8',
                comment = '',
                rating = '-8072'
            )
        else:
            return RatingInspectionResultTyped(
                id = 56,
                team = 56,
                type = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                confidence = '-8',
                rating = '-8072',
        )
        """

    def testRatingInspectionResultTyped(self):
        """Test RatingInspectionResultTyped"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
