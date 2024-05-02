# Bedrock Guardrails Sample

このリポジトリは、Amazon Bedrock の Guardrails 機能を使用したサンプルコードを提供します。

## 前提条件

- Python 3.x がインストールされていること
- AWS アカウントを持っていること
- 必要な AWS SDK for Python (Boto3) がインストールされていること

## セットアップ

1. このリポジトリをクローンまたはダウンロードします。

```bash
pip install -r requirements.txt
export GUARDRAIL_IDENTIFIER='your-guardrail-identifier'
export MSG='your-prompt-message'
python guardrails.py
```

## response

```
Guardrail Trace:
{
  "amazon-bedrock-trace": {
    ...
  }
}

Response:
モデルからの応答メッセージ
```
