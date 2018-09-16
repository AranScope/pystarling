from starling.starling import Starling

starling = Starling({
    "access_token": "v9gAGv5CKMutzVrvyA8FkJggdqYF1q5Z5NUdNGiX4mfUkyLknpVNC70cfXriTts7",
    "api_url": "https://api-sandbox.starlingbank.com"
})

print(starling.get_card())
