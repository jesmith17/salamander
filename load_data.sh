#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
  # Source the .env file
  set -a
  source .env
  set +a
else
  echo ".env file not found!"
  exit 1
fi

if [ -z "$MONGODB_URI" ]; then
  echo "MONGODB_URI is not set in .env. Please add it and save the file."
  exit 1
fi

echo "Importing dataset.json into MongoDB..."
mongoimport --uri="$MONGODB_URI" --db=gerrymander --collection=census_data --file=dataset.json --jsonArray

if [ $? -eq 0 ]; then
  echo "Successfully imported dataset into MongoDB."
else
  echo "Failed to import dataset."
  exit 1
fi
