import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_starling_client(requests_mock):
    """test static access token provided in client instance"""
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("test/responses/v1-get-accounts.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/accounts".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_account(mock_access_token)

        assert expected_response == mocked_response
