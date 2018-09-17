# Starling Python SDK 
[![Build Status](https://travis-ci.org/AranScope/starling-python.svg?branch=master)](https://travis-ci.org/AranScope/starling-python)

## Documentation

The documentation for the Starling SDK can be found <a href="https://starlingbank.github.io/starling-developer-sdk/">here</a>.

## Examples

```Python
from starling.starling import Starling

starling = Starling({
    "access_token": "some_access_token",
    "api_url": "https://api-sandbox.starlingbank.com"
})

print(starling.get_card())
```
