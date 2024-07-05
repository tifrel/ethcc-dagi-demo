#!/usr/bin/env bash

exit_msg() {
    echo "$2"
    exit "$1"
}

source .env || exit_msg 1 'Failed to source environment'
SMART_CONTRACT_ID="ethcc24-dagi-hack-demo.$ADMIN_ID"

tail -n +2 "indexer/contributions.csv" | while IFS=',' read -r x y; do
    # TODO: If called by admin, this is just a circlejerk
    near call "$SMART_CONTRACT_ID" contribute \
        "{\"x\":$x,\"y\":$y}" \
        --accountId "$ADMIN_ID"
    sleep 1
done
