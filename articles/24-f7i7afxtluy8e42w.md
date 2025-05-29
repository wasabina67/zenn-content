---
title: "BashでFTP操作を自動化する"
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
echo "This is test content" > $LOCAL_FILE

# Execute FTP commands using heredoc
ftp -n << EOF
open $SERVER $PORT
user $USERNAME $PASSWORD
passive
prompt
cd $REMOTE_DIR
mput $LOCAL_FILE
ls
bye
EOF

# Clean up temporary file
rm -f $LOCAL_FILE
```
