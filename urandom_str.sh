#!/bin/bash

tr -dc 'a-z0-9' < /dev/urandom | head -c 16; echo
