### `log_deletation.sh`
- Rotates, compresses, and deletes old log files daily using cron.
- Add to cron with: `0 0 * * * /bin/bash /path/to/log_rotation.sh`

#!/bin/bash

LOG_DIR="/var/log/myapp"
BACKUP_DIR="/var/log/myapp/archive"
RETENTION_DAYS=7
DATE=$(date +"%Y-%m-%d")

mkdir -p "$BACKUP_DIR"

# Rotate and compress logs
find "$LOG_DIR" -maxdepth 1 -name "*.log" -type f | while read -r logfile; do
  filename=$(basename "$logfile")
  gzip -c "$logfile" > "$BACKUP_DIR/${filename}_$DATE.gz"
  : > "$logfile"
  echo "Archived and cleared $logfile"
done

# Delete old backups
find "$BACKUP_DIR" -type f -name "*.gz" -mtime +$RETENTION_DAYS -exec rm -f {} \;
echo "Old archives older than $RETENTION_DAYS days deleted."