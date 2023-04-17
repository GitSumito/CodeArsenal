# AWS CloudWatch Logs Query Python Script
このPythonスクリプトは、AWS CloudWatch Logsのログデータをクエリし、結果を表示するために使用されます。
検索文字列にヒットした前後1分のログを表示します。

## 機能
タイムゾーンを指定してログを取得できます。
ログデータから特定の文字列を検索し、その検索結果を表示できます。

## 使い方
このスクリプトをPython 3環境で実行します。
必要なライブラリをインストールします。
```
pip install boto3
pip install pytz
```
環境変数を設定します。
```
export LOG_GROUP_NAME=<your-log-group-name>
export SEARCH_STRING=<search-string>
```
スクリプトを実行します。
```
python main.py
```

## テスト
```
python3 -m unittest test_main.py
```
## スクリプトの説明
get_logs 関数: 

指定したタイムゾーンとターゲット時刻を使用して、ログデータを取得し、結果を表示します。

if __name__ == "__main__" ブロック: 

メイン処理を実行します。環境変数からロググループ名と検索文字列を取得し、クエリを実行して結果を表示します。

## 依存関係
このスクリプトは以下のライブラリに依存しています。

### boto3: 

AWS SDK for Python

### pytz: 

タイムゾーンを扱うためのPythonライブラリ

## 注意事項
AWSアクセスキーとシークレットキーが設定されていることを確認してください。また、適切な権限があることを確認してください。

ログデータが大量にある場合、クエリの実行時間が長くなることがあります。
