import boto3
import time
import csv
import os
import argparse

# コマンドライン引数の解析
parser = argparse.ArgumentParser(description="Fetch logs from CloudWatch Logs Insights")
parser.add_argument('--profile', required=True, help='AWS profile name in .aws/config')
args = parser.parse_args()

# コマンドライン引数から設定を読み込む
aws_profile = args.profile
region_name = os.environ.get('AWS_REGION_NAME')  # 環境変数からリージョン名を取得
log_group = os.environ.get('AWS_LOG_GROUP_NAME')  # 環境変数からロググループ名を取得

# CloudWatch Logs Insights クエリの設定
start_query = int((time.time() - 3600) * 1000)  # 開始時間 (1時間前)
end_query = int(time.time() * 1000)  # 終了時間 (現在)
query = """
fields @timestamp, @message
| parse @message /(?<ip>[\\d\\.]+) - - \\[(?<timestamp>[^\\]]+)\\] "(?<http_method>[^"]+)" (?<status_code>[^ ]+) (?<size>[^ ]+) "(?<referrer>[^"]*)" "(?<user_agent>[^"]+)"/
| stats count(*) by user_agent
"""

# Boto3 セッションとクライアントの作成
session = boto3.Session(profile_name=aws_profile)
client = session.client('logs', region_name=region_name)

# クエリの実行
response = client.start_query(
    logGroupName=log_group,
    startTime=start_query,
    endTime=end_query,
    queryString=query
)

query_id = response['queryId']


# クエリ結果を取得するまで待機
while True:
    response = client.get_query_results(
        queryId=query_id
    )

    if response['status'] == 'Complete':
        results = response['results']
        break

    time.sleep(1)

# 結果が存在する場合のみ、CSVファイルに書き込む
if results:
    with open('query_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([field['field'] for field in results[0]])  # ヘッダ行

        for row in results:
            writer.writerow([field['value'] for field in row])
else:
    print("No results found")
