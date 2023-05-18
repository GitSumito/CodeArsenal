import hashlib
import hmac
import binascii
import base64

# 署名用のシークレットキーを設定します。(サンプルなので値は適当です。)
SECRET_KEY = "456"
MESSAGE = "789"

# HMAC-SHA512で署名するためのオブジェクトを作成します。
# シークレットキーをASCII形式のバイト列に変換します。
oHMACSHA512 = hmac.new(bytes(SECRET_KEY, 'ascii'), digestmod=hashlib.sha512)

# メッセージをASCII形式のバイト列に変換して署名します。
oHMACSHA512.update(bytes(MESSAGE, 'ascii'))

# 署名されたデータを取得します。
signature_rawout = oHMACSHA512.digest()

# 取得した署名を16進数の文字列に変換します。
signature = binascii.hexlify(signature_rawout).decode()

print("16進値の文字列:")
print(signature)

# 取得した署名をBASE64に変換します。
signatureB64 = base64.b64encode(signature_rawout).decode()

print("BASE64:")
print(signatureB64)

