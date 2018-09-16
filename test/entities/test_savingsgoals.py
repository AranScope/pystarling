import json

from starling.starling import Starling
from starling.utils.http import default_headers
from test.testsupport import expect_authorization_header


def test_get_savings_goal(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    savings_goal_id = "12345-12345"

    with open("../responses/v1-get-savings-goal.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/savings-goals/{}".format(mock_url, savings_goal_id),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.get_savings_goal(savings_goal_id, access_token=mock_access_token)

        assert expected_response == mocked_response


def test_list_savings_goals(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    with open("../responses/v1-list-savings-goals.json") as f:
        expected_response = json.load(f)

        requests_mock.get("{}/api/v1/savings-goals".format(mock_url),
                          headers=default_headers(mock_access_token),
                          request_headers=expect_authorization_header(mock_access_token),
                          json=expected_response)

        mocked_response = mock_object.list_savings_goals(access_token=mock_access_token)

        assert expected_response == mocked_response


def test_delete_savings_goal(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    savings_goal_id = "12345-12345"

    requests_mock.delete("{}/api/v1/savings-goals/{}".format(mock_url, savings_goal_id),
                         headers=default_headers(mock_access_token),
                         request_headers=expect_authorization_header(mock_access_token),
                         status_code=204)

    mock_object.delete_savings_goal(savings_goal_id, access_token=mock_access_token)


def test_add_money_to_savings_goal(requests_mock):
    mock_url = "http://localhost"
    mock_access_token = "0123456789"

    mock_object = Starling({
        "api_url": mock_url
    })

    savings_goal_id = "12345-12345"
    transaction_id = "54321-54321"
    minor_amount = 111
    savings_currency = "BRL"

    requests_mock.put("{}/api/v1/savings-goals/{}/add-money/{}".format(mock_url, savings_goal_id, transaction_id),
                      headers=default_headers(mock_access_token),
                      request_headers=expect_authorization_header(mock_access_token),
                      status_code=202)

    mock_object.add_money_to_savings_goal(savings_goal_id, transaction_id, minor_amount,
                                          currency=savings_currency, access_token=mock_access_token)
