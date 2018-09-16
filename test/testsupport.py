def expect_authorization_header(api_key):
    return {
        "Authorization": "Bearer {api_key}".format(api_key=api_key)
    }
