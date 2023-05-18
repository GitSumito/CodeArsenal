import os
import sys
import hashlib
import hmac
import binascii
import base64

def generate_signature(MESSAGE):
    # SECRET_KEYを環境変数から取得します。
    SECRET_KEY = os.getenv('SECRET_KEY')

    # HMAC-SHA512オブジェクトを作成します。
    oHMACSHA512 = hmac.new(bytes(SECRET_KEY, 'ascii'), digestmod=hashlib.sha512)

    # メッセージをASCII形式のバイト列に変換して署名します。
    oHMACSHA512.update(bytes(MESSAGE, 'ascii'))

    # 署名されたデータを取得します。
    signature_rawout = oHMACSHA512.digest()

    # 取得した署名を16進数の文字列に変換します。
    signature = binascii.hexlify(signature_rawout).decode()

    # 取得した署名をBASE64に変換します。
    signatureB64 = base64.b64encode(signature_rawout).decode()

    return signature, signatureB64

if __name__ == '__main__':
    message = sys.argv[1]
    hex_signature, base64_signature = generate_signature(message)

    print("16進値の文字列:")
    print(hex_signature)
    print("BASE64:")
    print(base64_signature)
