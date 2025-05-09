# cleanup.sh
#!/bin/bash
# Cleanup old logs, temp files, and Docker artifacts

rm -rf /tmp/*
rm -f /var/log/*.gz

docker system prune -af

echo "System cleanup complete: $(date)"