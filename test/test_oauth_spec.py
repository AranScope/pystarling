import json

from starling.starling import Starling
from starling.utils.http import oauth_headers


def test_get_access_token(requests_mock):
    mock_object = Starling({
        "oauth_url": "http://localhost",
        "client_id": "myclientid",
        "client_secret": "myclientsecret",
        "redirect_uri": "redirect"
    })

    with open("../responses/v1-get-access-token.json") as f:
        expected_response = json.load(f)

        requests_mock.post("http://localhost/oauth/access-token",
                           request_headers=oauth_headers(),
                           json=expected_response)

        mock_response = mock_object.get_access_token("code")

        assert expected_response == mock_response


def test_refresh_access_token(requests_mock):
    mock_object = Starling({
        "oauth_url": "http://localhost",
        "client_id": "myclientid",
        "client_secret": "myclientsecret",
        "redirect_uri": "redirect"
    })

    with open("../responses/v1-refresh-access-token.json") as f:
        expected_response = json.load(f)

        requests_mock.post("http://localhost/oauth/access-token",
                           request_headers=oauth_headers(),
                           json=expected_response)

        mock_response = mock_object.refresh_access_token(
            "11tyjapK8Vx3mBbCMkCrTmlbxjVRSny16MmbvGSvRlwhKYmFC4dbZetV0nTcXGjT")

        assert expected_response == mock_response
