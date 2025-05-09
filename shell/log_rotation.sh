# log_rotation.sh
#!/bin/bash
# Script to rotate and compress logs older than 7 days

LOG_DIR="/var/log/myapp"
ARCHIVE_DIR="/var/log/myapp/archive"

mkdir -p "$ARCHIVE_DIR"
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -exec gzip {} \; -exec mv {}.gz "$ARCHIVE_DIR" \;
echo "Log rotation completed: $(date)"
# End of script
# This script rotates and compresses log files older than 7 days in the specified log directory.
# It creates an archive directory if it doesn't exist and moves the compressed logs there.
# The script uses the find command to locate log files older than 7 days and compresses them using gzip.
# The script is designed to be run periodically, such as through a cron job, to manage log file sizes and keep the log directory organized.
# Ensure the script has execute permissions
# and is run with appropriate user privileges to access the log files.
# To set up a cron job for this script, you can add the following line to your crontab:
# 0 0 * * * /path/to/log_rotation.sh
# This will run the script every day at midnight.
# Make sure to replace "/path/to/log_rotation.sh" with the actual path to your script.
# You can check the cron job logs to verify that the script is running as expected