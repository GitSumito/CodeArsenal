param (
    [Parameter(Mandatory=$true)]
    [string]$Message
)

# SECRET_KEYを環境変数から取得します。
$SecretKey = [System.Environment]::GetEnvironmentVariable('SECRET_KEY')

# シークレットキーとメッセージをバイト配列に変換します。
$SecretKeyBytes = [Text.Encoding]::ASCII.GetBytes($SecretKey)
$MessageBytes = [Text.Encoding]::ASCII.GetBytes($Message)

# HMAC-SHA512オブジェクトを作成します。
$hmacsha = New-Object System.Security.Cryptography.HMACSHA512
$hmacsha.key = $SecretKeyBytes

# メッセージをASCII形式のバイト列に変換して署名します。
$signature = $hmacsha.ComputeHash($MessageBytes)

# 署名されたデータを取得します。
$signatureHex = [BitConverter]::ToString($signature) -replace '-', '' | Out-String

# 取得した署名をBASE64に変換します。
$signatureBase64 = [Convert]::ToBase64String($signature)

# 出力
Write-Output "16進値の文字列:"
Write-Output $signatureHex
Write-Output "BASE64:"
Write-Output $signatureBase64

