---
title: "title"
emoji: "🗂"
type: "tech"
topics: ["ftp"]
published: true
published_at: 2025-05-29
---

## スニペット

```bash
#!/bin/bash

# FTP server configuration
SERVER="127.0.0.1"
PORT="21"
USERNAME="username"
PASSWORD="password"
REMOTE_DIR="/public"

# Local file to upload
LOCAL_FILE="tmp"
touch $LOCAL_FILE

# Create FTP command sequence
FTP_COMMANDS=$(cat << EOF
open $SERVER $PORT
user $USERNAME $PASSWORD
passive
prompt
cd $REMOTE_DIR
mput $LOCAL_FILE
ls
bye
EOF
)

# Execute FTP commands
echo "$FTP_COMMANDS" | ftp -n

# Clean up temporary file
rm -f $LOCAL_FILE
```
