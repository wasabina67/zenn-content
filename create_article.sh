#!/bin/bash

# Get the latest article number
latest_article_num=$(ls -1 ./articles/ | grep -Eo '^[0-9]+' | sort -n | tail -1)

# Calculate new article number (increment)
new_article_num=$((latest_article_num + 1))

# Generate random string
random_str=$(bash ./urandom_str.sh)

# Create new filename
new_filename="${new_article_num}-${random_str}.md"

# Create new article file from template
cp -p ./articles_template/9999-template.md "./articles/${new_filename}"

# Display created article information
echo "New article created: ${new_filename}"
echo "File path: ./articles/${new_filename}"
