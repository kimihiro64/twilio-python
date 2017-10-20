# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class FaxTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes(sid="FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "v1",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "direction": "outbound",
                "from": "+14155551234",
                "media_url": "https://www.example.com/fax.pdf",
                "media_sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "num_pages": null,
                "price": null,
                "price_unit": null,
                "quality": null,
                "sid": "FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "to": "+14155554321",
                "duration": null,
                "links": {
                    "media": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                },
                "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.fax.v1.faxes(sid="FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://fax.twilio.com/v1/Faxes',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "faxes": [],
                "meta": {
                    "first_page_url": "https://fax.twilio.com/v1/Faxes?PageSize=50&Page=0",
                    "key": "faxes",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://fax.twilio.com/v1/Faxes?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.fax.v1.faxes.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "faxes": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "v1",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "direction": "outbound",
                        "from": "+14155551234",
                        "media_url": "https://www.example.com/fax.pdf",
                        "media_sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "num_pages": null,
                        "price": null,
                        "price_unit": null,
                        "quality": null,
                        "sid": "FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "queued",
                        "to": "+14155554321",
                        "duration": null,
                        "links": {
                            "media": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                        },
                        "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://fax.twilio.com/v1/Faxes?PageSize=50&Page=0",
                    "key": "faxes",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://fax.twilio.com/v1/Faxes?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.fax.v1.faxes.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes.create(to="to", media_url="https://example.com")

        values = {
            'To': "to",
            'MediaUrl': "https://example.com",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://fax.twilio.com/v1/Faxes',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "v1",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "direction": "outbound",
                "from": "+14155551234",
                "media_url": null,
                "media_sid": null,
                "num_pages": null,
                "price": null,
                "price_unit": null,
                "quality": "superfine",
                "sid": "FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "to": "+14155554321",
                "duration": null,
                "links": {
                    "media": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                },
                "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.fax.v1.faxes.create(to="to", media_url="https://example.com")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes(sid="FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "v1",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "direction": "outbound",
                "from": "+14155551234",
                "media_url": null,
                "media_sid": null,
                "num_pages": null,
                "price": null,
                "price_unit": null,
                "quality": null,
                "sid": "FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "canceled",
                "to": "+14155554321",
                "duration": null,
                "links": {
                    "media": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                },
                "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.fax.v1.faxes(sid="FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes(sid="FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.fax.v1.faxes(sid="FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)