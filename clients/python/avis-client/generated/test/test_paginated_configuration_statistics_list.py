# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avis_client.models.paginated_configuration_statistics_list import (
    PaginatedConfigurationStatisticsList,
)


class TestPaginatedConfigurationStatisticsList(unittest.TestCase):
    """PaginatedConfigurationStatisticsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedConfigurationStatisticsList:
        """Test PaginatedConfigurationStatisticsList
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedConfigurationStatisticsList`
        """
        model = PaginatedConfigurationStatisticsList()
        if include_optional:
            return PaginatedConfigurationStatisticsList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    avis_client.models.configuration_statistics.ConfigurationStatistics(
                        configuration = 56,
                        opened_inspections = 56,
                        inspections_marked_for_validation = 56, )
                    ]
            )
        else:
            return PaginatedConfigurationStatisticsList(
                count = 123,
                results = [
                    avis_client.models.configuration_statistics.ConfigurationStatistics(
                        configuration = 56,
                        opened_inspections = 56,
                        inspections_marked_for_validation = 56, )
                    ],
        )
        """

    def testPaginatedConfigurationStatisticsList(self):
        """Test PaginatedConfigurationStatisticsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
