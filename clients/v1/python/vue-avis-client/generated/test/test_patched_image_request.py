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

from vue_avis_client.models.patched_image_request import PatchedImageRequest

class TestPatchedImageRequest(unittest.TestCase):
    """PatchedImageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedImageRequest:
        """Test PatchedImageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedImageRequest`
        """
        model = PatchedImageRequest()
        if include_optional:
            return PatchedImageRequest(
                team = 56,
                case = 56,
                uploaded_by = 56,
                inspection_results = [
                    56
                    ],
                format = 'image/png',
                capture_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                file = bytes(b'blah'),
                part_id = '',
                validation_status = 'NONE'
            )
        else:
            return PatchedImageRequest(
        )
        """

    def testPatchedImageRequest(self):
        """Test PatchedImageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
