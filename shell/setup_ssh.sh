# setup_ssh.sh
#!/bin/bash
# Automatically copy SSH key to remote host

if [ -z "$1" ]; then
  echo "Usage: $0 user@host"
  exit 1
fi

ssh-copy-id $1
echo "SSH key added to $1"