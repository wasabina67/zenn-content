#!/bin/bash

PUB=`grep "published: true" articles/*.md | wc -l`
UNPUB=`grep "published: false" articles/*.md | wc -l`
TOTAL=$((PUB + UNPUB))

echo "- Published: ${PUB}"
echo "- Unpublished: ${UNPUB}"
echo "- Total: ${TOTAL}"
