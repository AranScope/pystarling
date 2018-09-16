def default_headers(access_token):
    return {
        "Accept": "application/json",
        "Authorization": "Bearer {access_token}".format(access_token=access_token)
    }


def post_headers(access_token):
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {access_token}".format(access_token=access_token)
    }


def oauth_headers():
    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

