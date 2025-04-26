#!/bin/bash

# Check if account name was provided
if [ -z "$1" ]; then
  echo "❌ Please provide an account name."
  echo "Usage: ./recover_password.sh <account_name>"
  exit 1
fi

ACCOUNT_NAME=$1

# Run recover_password.py with account name
python3 recover_password.py --account $ACCOUNT_NAME
