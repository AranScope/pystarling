from starling.starling import Starling

starling = Starling({
    "access_token": "some_access_token",
    "api_url": "https://api-sandbox.starlingbank.com"
})

print(starling.get_card())
