# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.paginated_quality_criteria_list import (
    PaginatedQualityCriteriaList,
)


class TestPaginatedQualityCriteriaList(unittest.TestCase):
    """PaginatedQualityCriteriaList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedQualityCriteriaList:
        """Test PaginatedQualityCriteriaList
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedQualityCriteriaList`
        """
        model = PaginatedQualityCriteriaList()
        if include_optional:
            return PaginatedQualityCriteriaList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    avis_client.models.quality_criteria.QualityCriteria(
                        id = 56,
                        team = 56,
                        configurations = [
                            56
                            ],
                        good_quality_classes = [
                            ''
                            ],
                        uncertain_quality_classes = [
                            ''
                            ],
                        bad_quality_classes = [
                            ''
                            ],
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return PaginatedQualityCriteriaList(
                count = 123,
                results = [
                    avis_client.models.quality_criteria.QualityCriteria(
                        id = 56,
                        team = 56,
                        configurations = [
                            56
                            ],
                        good_quality_classes = [
                            ''
                            ],
                        uncertain_quality_classes = [
                            ''
                            ],
                        bad_quality_classes = [
                            ''
                            ],
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testPaginatedQualityCriteriaList(self):
        """Test PaginatedQualityCriteriaList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
