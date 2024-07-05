#!/usr/bin/env bash

exit_msg() {
    echo "$2"
    exit "$1"
}

source .env || exit_msg 1 'Failed to source environment'
SMART_CONTRACT_ID="ethcc24-dagi-hack-demo.$ADMIN_ID"

echo "{\"account_id\":\"$ADMIN_ID\",\"public_key\":\"$ADMIN_PUBLIC_KEY\",\"private_key\":\"$ADMIN_PRIVATE_KEY\"}" > ~/.near-credentials/testnet/$ADMIN_ID.json || exit_msg 1 'Failed to write admin key file'
echo "{\"account_id\":\"$SMART_CONTRACT_ID\",\"public_key\":\"$ADMIN_PUBLIC_KEY\",\"private_key\":\"$ADMIN_PRIVATE_KEY\"}" > ~/.near-credentials/testnet/$SMART_CONTRACT_ID.json || exit_msg 1 'Failed to write smart contract key file'
