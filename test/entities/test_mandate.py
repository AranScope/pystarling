import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_list_mandates(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("../responses/v1-list-mandates.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/direct-debit/mandates".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.list_mandates(access_token=mock_access_token)

        assert expected_response == mocked_response


def test_get_mandate(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"
    mandate_id = "12345-12345"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("../responses/v1-get-mandate.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/direct-debit/mandates/{}".format(mock_url, mandate_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_mandate(mandate_id, access_token=mock_access_token)

        assert expected_response == mocked_response


def test_delete_mandate(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"
    mandate_id = "12345-12345"

    mock_object = Starling({
        "api_url": mock_url
    })

    requests_mock.delete("{}/api/v1/direct-debit/mandates/{}".format(mock_url, mandate_id),
                         headers=default_headers(mock_access_token),
                         request_headers=expect_authorization_header(mock_access_token),
                         status_code=204)

    mock_object.delete_mandate(mandate_id, access_token=mock_access_token)
