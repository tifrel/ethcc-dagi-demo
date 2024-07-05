#!/usr/bin/env bash

exit_msg() {
    echo "$2"
    exit "$1"
}

source .env || exit_msg 1 'Failed to source environment'
export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
export BLOCKHEIGHT
export ADMIN_ID
export SMART_CONTRACT_ID="ethcc24-dagi-hack-demo.$ADMIN_ID"

(
    cd indexer || exit_msg 1 'Failed to enter indexer directory'
    source venv/bin/activate || exit_msg 'Failed to activate virtual environment'
    python src/main.py || exit_msg 1 'Failed to run indexer'
) || exit 1
