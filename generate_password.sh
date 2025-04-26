#!/bin/bash

# Check if account name was provided
if [ -z "$1" ]; then
  echo "❌ Please provide an account name."
  echo "Usage: ./generate_password.sh <account_name>"
  exit 1
fi

ACCOUNT_NAME=$1

# Run locksmith.py with account name
python3 -m locksmith.locksmith --account $ACCOUNT_NAME
