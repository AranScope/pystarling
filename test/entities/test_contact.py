import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_get_contacts(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("test/responses/v1-get-contacts.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/contacts".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_contacts(mock_access_token)

        assert expected_response == mocked_response


def test_get_contact_account(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    contact_id = "fc17e7d5-ff2c-4a3c-8f64-9ac93d80de62"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("test/responses/v1-get-contact-account.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/contacts/{}".format(mock_url, contact_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_contact_account(contact_id, access_token=mock_access_token)

        assert expected_response == mocked_response


def test_create_contact_account(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    name = "Mickey Mouse"
    account_type = "3"
    account_number = "87654321"
    sort_code = "60-83-71"
    customer_id = "2022a9c9-01fa-4c8d-ab19-daec80d7a111"

    mock_object = Starling({
        "api_url": mock_url
    })

    requests_mock.post("{}/api/v1/contacts".format(mock_url),
                       headers=default_headers(mock_access_token),
                       request_headers=expect_authorization_header(mock_access_token),
                       status_code=202)

    mocked_response = mock_object.create_contact(
        name,
        account_number,
        sort_code,
        customer_id=customer_id,
        account_type=account_type,
        access_token=mock_access_token
    )

    print(mocked_response)

    assert mocked_response == {}


def test_delete_contact_account(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    contact_id = "fc17e7d5-ff2c-4a3c-8f64-9ac93d80de62"

    mock_object = Starling({
        "api_url": mock_url
    })

    requests_mock.delete("{}/api/v1/contacts/{}".format(mock_url, contact_id),
                         headers=default_headers(mock_access_token),
                         request_headers=expect_authorization_header(mock_access_token),
                         status_code=204)

    mocked_response = mock_object.delete_contact(contact_id, access_token=mock_access_token)

    assert mocked_response == {}
