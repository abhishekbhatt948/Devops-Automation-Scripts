# service_monitor.sh
#!/bin/bash
# Check if services are running and restart if stopped

SERVICES=(nginx docker)

for service in "${SERVICES[@]}"
do
  systemctl is-active --quiet $service
  if [ $? -ne 0 ]; then
    echo "$service is not running. Restarting..."
    systemctl restart $service
  else
    echo "$service is running."
  fi
done