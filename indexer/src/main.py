import asyncio
import logging
import os

from near_lake_framework import LakeConfig, streamer, Network, near_primitives
from near_lake_framework.utils import fetch_latest_block

# Some setup
logging.getLogger("near_lake_framework").setLevel(logging.INFO)
SMART_CONTRACT_ID = os.getenv("SMART_CONTRACT_ID")

async def main():
    start_block_height = int(os.getenv("BLOCKHEIGHT", fetch_latest_block(network=Network.TESTNET)))
    processed = 0
    config = LakeConfig(
        Network.TESTNET,
        start_block_height=start_block_height,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    _, streamer_messages_queue = streamer(config)
    while True:
        process_streamer_message(await streamer_messages_queue.get())
        processed += 1
              


def process_streamer_message(streamer_message: near_primitives.StreamerMessage):
    for shard in streamer_message.shards:
        for receipt_execution_outcome in shard.receipt_execution_outcomes:
            if receipt_execution_outcome.receipt.receiver_id == SMART_CONTRACT_ID:
                print(receipt_execution_outcome.execution_outcome.outcome.logs[0])


if __name__ == "__main__":
    asyncio.new_event_loop().run_until_complete(main())
