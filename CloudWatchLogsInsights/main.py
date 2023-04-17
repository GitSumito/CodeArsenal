import boto3
import time
import os
from pytz import timezone as pytz
from datetime import datetime, timedelta, timezone


def get_logs(timezone_str, target_time_str, log_group):
    print(f"timezone: {timezone_str}")
    print(f"target_time_str: {target_time_str}")

    target_timezone = pytz(timezone_str)
    target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S.%f").replace(microsecond=0)
    target_time = target_timezone.localize(target_time)

    start_time = int((target_time - timedelta(minutes=1)).timestamp() * 1000)
    end_time = int((target_time + timedelta(minutes=1)).timestamp() * 1000)

    query = "fields @timestamp, @message | sort @timestamp desc"
    insights = boto3.client("logs")
    results = insights.start_query(
        logGroupName=log_group,
        startTime=start_time,
        endTime=end_time,
        queryString=query,
    )

    while True:
        query_results = insights.get_query_results(queryId=results["queryId"])
        if query_results["status"] == "Complete":
            for result in query_results["results"]:
                print(result)
            break
        time.sleep(1)

    print("Query:", query)
    print("Query status:", query_results["status"])
    print("Statistics:", query_results["statistics"])

def now(timezone):
    return datetime.now(timezone)

def main():
    log_group = os.environ["LOG_GROUP_NAME"]
    search_string = os.environ["SEARCH_STRING"]

    query = f'''
    fields @timestamp, @message
    | filter @message like /{search_string}/
    | sort @timestamp asc
    '''

    JST = timezone(timedelta(hours=9))
    now_jst = now(JST)
    now_jst_epoch_ms = int(now_jst.timestamp() * 1000)

    start_time = now_jst_epoch_ms - (24 * 60 * 60 * 1000)
    end_time = now_jst_epoch_ms

    insights = boto3.client("logs")
    results = insights.start_query(
        logGroupName=log_group,
        startTime=start_time,
        endTime=end_time,
        queryString=query,
    )

    query_results = None
    while query_results is None or query_results["status"] != "Complete":
        time.sleep(1)
        query_results = insights.get_query_results(queryId=results["queryId"])

    oneline = query_results["results"]
    if oneline:
        timestamp_value = oneline[0][0]['value']

    get_logs("UTC", timestamp_value, log_group)


if __name__ == "__main__":
    main()
