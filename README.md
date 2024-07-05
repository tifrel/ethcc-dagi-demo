To use the scripts, the following needs to be installed/set up:

- [NEAR CLI](https://docs.near.org/tools/near-cli)
- An admin NEAR account with key file under `~/.near-credentials/testnet/{admin_id}.json`
- AWS creds

You need a `.env` file with the following setup:

- `ADMIN_ID`: The NEAR account you will use to administrate this system
- `ADMIN_PUBLIC_KEY`: Public key for the admin account
- `ADMIN_PRIVATE_KEY`: Private key for the admin account
