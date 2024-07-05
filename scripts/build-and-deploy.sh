#!/usr/bin/env bash

exit_msg() {
    echo "$2"
    exit "$1"
}

source .env || exit_msg 1 'Failed to source environment'
SMART_CONTRACT_ID="ethcc24-dagi-hack-demo.$ADMIN_ID"

# Build smart contract
(cd data-contributor-payout && cargo make build) || exit_msg 1 'Failed to build smart contract'

# Use with caution, as this wipes the state!
# near delete "$SMART_CONTRACT_ID" "$ADMIN_ID"

# (Re)create account
near create-account "$SMART_CONTRACT_ID" \
    --masterAccount "$ADMIN_ID" \
    --initialBalance 2 \
    --publicKey "$ADMIN_PUBLIC_KEY" ||
    exit_msg 1 'Failed to create smart contract account'

# Deploy smart contract
near deploy "$SMART_CONTRACT_ID" \
    data-contributor-payout/contract.wasm \
    init '{}'
