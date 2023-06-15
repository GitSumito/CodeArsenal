# README.md

## Project Title: CloudWatch Logs Insights Fetcher

This script fetches logs from AWS CloudWatch Logs Insights, executes a specific query to extract and aggregate data based on user agents, and writes the results to a CSV file.

## Requirements

- Python 3.6+
- Boto3 library
- AWS Account
- AWS CLI configured with an appropriate profile and access keys

## Setup and Installation

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required dependencies:

    ```sh
    pip install boto3
    ```

3. Set up AWS CLI with the appropriate credentials and profile. You can follow the [official AWS CLI Configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

4. Set environment variables for the AWS region and log group you want to query:

    ```sh
    export AWS_REGION_NAME='us-west-2'
    export AWS_LOG_GROUP_NAME='/aws/lambda/my-lambda-function'
    ```

## Usage

Run the script by specifying the AWS profile as a command line argument:

```sh
python your_script.py --profile YOUR_AWS_PROFILE_NAME
```

The script will execute a query on AWS CloudWatch Logs Insights, and write the results into a CSV file named `query_results.csv` in the current directory.

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
