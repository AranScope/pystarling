import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_make_local_payment(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    destination_account_uid = "11eb8d9b-386a-43ba-825d-7edee5c6b01a"
    reference = "dinner"
    amount = "10"

    requests_mock.post("{}/api/v1/payments/local".format(mock_url),
                       headers=default_headers(mock_access_token),
                       request_headers=expect_authorization_header(mock_access_token),
                       status_code=202)

    try:
        mock_object.make_local_payment(destination_account_uid, reference, amount, access_token=mock_access_token)
        assert True
    except:
        assert False


def test_list_scheduled_payments(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("test/responses/v1-list-scheduled-payments.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/payments/scheduled".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.list_scheduled_payments(access_token=mock_access_token)

        assert expected_response == mocked_response
