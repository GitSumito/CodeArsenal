# HMAC-SHA512 in Python
This repository contains a Python script that generates a HMAC-SHA512 signature from a given message using a secret key.

# How to use
The script uses Python's built-in hashlib, hmac, binascii, and base64 libraries to create HMAC-SHA512 signatures.

In the script, replace the SECRET_KEY and MESSAGE values with the secret key and message you want to sign. The script will then generate a HMAC-SHA512 signature of the message, and print it as a hexadecimal string and a Base64-encoded string.

# example
```
# export SECRET_KEY=456
# python3 ./main.py 789 
16進値の文字列:
dc247cecbb2100248bb44f5c935c694e502accf1d397b51f238c18bfe823bd6c5bd948eec004eac42e19ea9dd3f1751006edd60a3437c282785170b235db6ecc
BASE64:
3CR87LshACSLtE9ck1xpTlAqzPHTl7UfI4wYv+gjvWxb2UjuwATqxC4Z6p3T8XUQBu3WCjQ3woJ4UXCyNdtuzA==
```

# Requirements
Python 3.x

# License
MIT

# Powershell
https://win.just4fun.biz/?PowerShell/HMAC-SHA%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95