import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_get_transactions(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("../responses/v1-get-transactions.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/transactions".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response,
                          query={"from": "2017-03-01", "to": "2017-03-06"})

        mocked_response = mock_object.get_transactions("2017-03-01", "2017-03-06", "", access_token=mock_access_token)

        assert expected_response == mocked_response


def test_get_transaction_with_unspecified_source(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    transaction_id = "32b4d093-f3b3-45da-9f89-d6a1395ab397"

    with open("../responses/v1-get-transaction.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/transactions/{}".format(mock_url, transaction_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_transaction(transaction_id, "", access_token=mock_access_token)

        assert expected_response == mocked_response


def test_get_incoming_fps_transaction(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    transaction_id = "32b4d093-f3b3-45da-9f89-d6a1395ab397"
    source = "FASTER_PAYMENTS_IN"

    with open("../responses/v1-get-transaction-fps-in.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/transactions/fps/in/{}".format(mock_url, transaction_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_transaction(transaction_id, source, access_token=mock_access_token)

        assert expected_response == mocked_response


def test_get_outgoing_fps_transaction(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    transaction_id = "b5c65fd2-1795-4262-93f0-f0490759bf1f"
    source = "FASTER_PAYMENTS_OUT"

    with open("../responses/v1-get-transaction-fps-out.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/transactions/fps/out/{}".format(mock_url, transaction_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_transaction(transaction_id, source, access_token=mock_access_token)

        assert expected_response == mocked_response


def test_get_specific_card_transaction(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    transaction_id = "77b7d507-6546-4301-a841-fbf570de65c6"
    source = "MASTER_CARD"

    with open("../responses/v1-get-transaction-card.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/transactions/mastercard/{}".format(mock_url, transaction_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_transaction(transaction_id, source, access_token=mock_access_token)

        assert expected_response == mocked_response
