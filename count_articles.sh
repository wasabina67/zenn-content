#!/bin/bash

PUB=`grep "published: true" articles/*.md | wc -l`
UNPUB=`grep "published: false" articles/*.md | wc -l`
TOTAL=$((PUB + UNPUB))

sed -i "s/^- Published:.*/- Published: ${PUB}/" README.md
sed -i "s/^- Unpublished:.*/- Unpublished: ${UNPUB}/" README.md
sed -i "s/^- Total:.*/- Total: ${TOTAL}/" README.md
