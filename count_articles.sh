#!/bin/bash

PUB=`grep "published: true" articles/*.md | wc -l`
UNPUB=`grep "published: false" articles/*.md | wc -l`
TOTAL=$((PUB + UNPUB))

sed -i "s/^- Total:.*/- Total: ${TOTAL}/" README.md
sed -i "s/^  - Published:.*/  - Published: ${PUB}/" README.md
sed -i "s/^  - Unpublished:.*/  - Unpublished: ${UNPUB}/" README.md

if ! git diff --quiet README.md; then
    git add README.md
fi
