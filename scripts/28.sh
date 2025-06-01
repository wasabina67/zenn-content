#!/bin/bash

function handle_sigint() {
    echo 'Received SIGINT!'
}

function handle_sigterm() {
    echo 'Received SIGTERM!'
    exit 0
}

trap handle_sigint SIGINT
trap handle_sigterm SIGTERM

while true; do
    echo 'sleeping...'
    sleep 5
done
