#!/bin/bash

BEGIN=$(date +'%s.%3N')
sleep 5
END=$(date +'%s.%3N')

DURING=$(echo "scale=3; ${END} - ${BEGIN}" | bc)
echo "BEGIN: ${BEGIN}"
echo "END: ${END}"
echo "DURING: ${DURING} seconds"
