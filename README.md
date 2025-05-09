# DevOps Automation Scripts - README

## Shell Scripts (`shell/`)

### `log_rotation.sh`
- Rotates and compresses old log files daily to save disk space.

### `log_deleation.sh`
- run cron job to Rotates and compresses and delete old log files daily to save disk space.

### `disk_alert.sh`
- Checks disk usage and alerts if it exceeds the threshold.

### `docker_push.sh`
- Automates Docker image build, tag, and push to Docker Hub.

### `service_monitor.sh`
- Monitors system services and restarts them if they go down.

### `cleanup.sh`
- Removes unnecessary temp/log files and prunes Docker containers/images.

### `setup_ssh.sh`
- Copies SSH key to a remote server to enable passwordless login.

## Python Scripts (`python/`)

### `ec2_scheduler.py`
- Starts or stops an EC2 instance based on time of day.

### `s3_cleanup.py`
- Deletes old S3 files older than a defined retention period.

### `iam_user_report.py`
- Generates a CSV report of all IAM users with creation and password usage data.

### `cloudwatch_parser.py`
- Parses latest logs from a given CloudWatch log group and prints error messages.

### `api_smoke_test.py`
- Sends test requests to endpoint URLs and checks if responses are successful.

### `jenkins_trigger.py`
- Triggers a Jenkins build job using REST API and prints the status code.

### `slack_notifier.py`
- Sends a notification to a Slack channel via a webhook.

### `route53_failover_tester.py`
- Checks health status of Route 53 failover DNS records.

---

Each script can be adapted to different environments and pipelines. Credentials, tokens, or IDs should be stored securely using secrets management tools or environment variables.