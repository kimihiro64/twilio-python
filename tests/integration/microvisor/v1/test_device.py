# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class DeviceTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://microvisor.twilio.com/v1/Devices',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "devices": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://microvisor.twilio.com/v1/Devices?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://microvisor.twilio.com/v1/Devices?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "devices"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "devices": [
                    {
                        "sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "This is my device; there are many like it.",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "app": {
                            "target_sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "target_hash": null,
                            "date_targeted": "2021-01-01T12:34:56Z",
                            "update_status": "up-to-date",
                            "update_error_code": 0,
                            "reported_sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "date_reported": "2021-01-01T12:34:56Z"
                        },
                        "logging": {
                            "enabled": true,
                            "date_expires": "2021-01-01T12:34:56Z"
                        },
                        "date_created": "2021-01-01T12:34:56Z",
                        "date_updated": "2021-01-01T12:34:56Z",
                        "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://microvisor.twilio.com/v1/Devices?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://microvisor.twilio.com/v1/Devices?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "devices"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "This is my device; there are many like it.",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "app": {
                    "target_sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "target_hash": null,
                    "date_targeted": "2021-01-01T12:34:56Z",
                    "update_status": "up-to-date",
                    "update_error_code": 0,
                    "reported_sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_reported": "2021-01-01T12:34:56Z"
                },
                "logging": {
                    "enabled": true,
                    "date_expires": "2021-01-01T12:34:56Z"
                },
                "date_created": "2021-01-01T12:34:56Z",
                "date_updated": "2021-01-01T12:34:56Z",
                "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "UniqueName",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "app": {
                    "target_sid": "KAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "target_hash": null,
                    "date_targeted": "2021-01-01T12:34:56Z",
                    "update_status": "pending",
                    "update_error_code": 0,
                    "reported_sid": null,
                    "date_reported": "2021-01-01T12:34:56Z"
                },
                "logging": {
                    "enabled": false,
                    "date_expires": null
                },
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
