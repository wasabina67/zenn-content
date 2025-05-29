---
title: "Bashで実行時間を計測する"
emoji: "⏰"
type: "tech"
topics: ["bash"]
published: true
published_at: 2025-05-29
---

```bash
#!/bin/bash

BEGIN=$(date +'%s.%3N')
sleep 5
END=$(date +'%s.%3N')

DURING=$(echo "scale=3; ${END} - ${BEGIN}" | bc)
echo "BEGIN: ${BEGIN}"
echo "END: ${END}"
echo "DURING: ${DURING} seconds"
```
