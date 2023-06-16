# README.md

## Project Title: CloudWatch Logs Insights Fetcher

This script fetches logs from AWS CloudWatch Logs Insights, executes a specific query to extract and aggregate data based on user agents, and writes the results to a CSV file.

## Requirements

- Python 3.6+
- Boto3 library
- AWS Account
- AWS CLI configured with an appropriate profile and access keys

## Setup and Installation

1. Install the required dependencies:

   ```sh
   pip install boto3 user_agents
   ```

2. Set environment variables for the AWS region and log group you want to query:

   ```sh
   export AWS_REGION_NAME='ap-northeast-1'
   export AWS_LOG_GROUP_NAME='/aws/lambda/my-lambda-function'
   ```

## Usage

Run the script by specifying the AWS profile as a command line argument:

```sh
# download
python3 UserAgentDownloader.py --profile your-aws-profile
# parse
python3 UserAgentParser.py

```

The script will execute a query on AWS CloudWatch Logs Insights, and write the results into a CSV file named `query_results.csv` in the current directory.

## results

```
head parsed_logs.csv
Device,OS Version,Browser,Browser Version,Count
PC,Windows 10,Edge,114.0.1823,92
PC,Windows 10,Chrome,114.0.0,112
Mobile,iOS 15.6,Mobile Safari,15.6,8
Mobile,iOS 16.5,Mobile Safari,16.5,9
PC,Windows 10,Chrome,109.0.0,1
PC,Other ,PostmanRuntime,7.26.5,2
Mobile,iOS 16.5,Chrome Mobile iOS,114.0.5735,1
Mobile,iOS 16.2,Google,267.0.537056344,8
PC,Windows 8,Chrome,89.0.4389,1
```

## Script Details

The script uses Boto3 to interact with AWS. It sends a query to CloudWatch Logs Insights to parse and analyze the logs based on user agents.

The specific query executed by the script is:

```plaintext
fields @timestamp, @message
| parse @message /(?<ip>[\d\.]+) - - \[(?<timestamp>[^\]]+)\] "(?<http_method>[^"]+)" (?<status_code>[^ ]+) (?<size>[^ ]+) "(?<referrer>[^"]*)" "(?<user_agent>[^"]+)"/
| stats count(*) by user_agent
```

This query parses the logs and counts the number of occurrences for each user agent.

## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

MIT License. See the [LICENSE](LICENSE) file for details.
