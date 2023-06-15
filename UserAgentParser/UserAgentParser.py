import csv
from user_agents import parse

# ログファイルの読み込み
with open('query_results.csv', 'r') as file:
    logs = csv.DictReader(file)
    
    # 結果を保存するためのリスト
    results = []

    # 各ログエントリを処理
    for log in logs:
        user_agent = log['user_agent']
        count = log['count']

        # user_agents ライブラリでユーザーエージェント文字列を解析
        ua = parse(user_agent)
        device_type = 'Mobile' if ua.is_mobile else 'Tablet' if ua.is_tablet else 'PC'
        os = f"{ua.os.family} {ua.os.version_string}"
        browser = f"{ua.browser.family}"
        browser_version = f"{ua.browser.version_string}"

        # 結果をリストに追加
        results.append([device_type, os, browser, browser_version, count])

# 結果を新しいCSVファイルに出力
with open('parsed_logs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Device', 'OS Version', 'Browser', 'Browser Version', 'Count'])
    writer.writerows(results)

