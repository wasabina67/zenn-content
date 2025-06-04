#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo 'Error: The script expects exactly 3 arguments.'
    exit 1
fi

echo 'The number of arguments is 3.'
echo $1
echo $2
echo $3
echo 'Hello, World!'
false

if [ "$?" -eq 0 ]; then
    echo 'Command succeeded 🤗'
else
    echo 'Command failed 😱'
fi
