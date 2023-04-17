import unittest
from unittest.mock import MagicMock, patch
import boto3
from datetime import datetime, timedelta, timezone
from main import get_logs


class TestScript(unittest.TestCase):

    @patch("boto3.client")
    @patch("time.sleep")
    @patch("main.now")
    def test_get_logs(self, mock_now, mock_sleep, mock_boto3_client):
        mock_start_query_response = {
            "queryId": "test_query_id"
        }
        mock_get_query_results_response = {
            "status": "Complete",
            "results": [
                [
                    {
                        "field": "@timestamp",
                        "value": "2023-04-17T10:00:00Z"
                    },
                    {
                        "field": "@message",
                        "value": "Sample log message"
                    }
                ]
            ],
            "statistics": {
                "recordsMatched": 1,
                "recordsScanned": 1,
                "bytesScanned": 100
            }
        }

        mock_logs_client = MagicMock()
        mock_logs_client.start_query.return_value = mock_start_query_response
        mock_logs_client.get_query_results.return_value = mock_get_query_results_response

        mock_boto3_client.return_value = mock_logs_client

        # Set a fixed datetime object for the test
        fixed_datetime = datetime(2023, 4, 17, 10, 0, 0, tzinfo=timezone.utc)
        mock_now.return_value = fixed_datetime + timedelta(minutes=1)

        # Calculate the expected start_time and end_time
        start_time_expected = int((fixed_datetime - timedelta(minutes=1)).timestamp() * 1000)
        end_time_expected = int((fixed_datetime + timedelta(minutes=1)).timestamp() * 1000)

        get_logs("UTC", "2023-04-17 10:00:00.000000", "test_log_group")

        mock_logs_client.start_query.assert_called_once_with(
            logGroupName="test_log_group",
            startTime=start_time_expected,
            endTime=end_time_expected,
            queryString="fields @timestamp, @message | sort @timestamp desc",
        )
        mock_logs_client.get_query_results.assert_called_with(queryId="test_query_id")


if __name__ == "__main__":
    unittest.main()
