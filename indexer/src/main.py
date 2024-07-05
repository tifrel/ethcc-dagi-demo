import asyncio
import logging
import os
import sys

from near_lake_framework import LakeConfig, streamer, Network, near_primitives
from near_lake_framework.utils import fetch_latest_block

# Suppress warning logs from specific dependencies
logging.getLogger("near_lake_framework").setLevel(logging.INFO)

LIMIT=120

# Read environment. TODO: fail if unset!
NETWORK = Network.TESTNET
SMART_CONTRACT_ID = os.getenv("SMART_CONTRACT_ID")
BLOCKHEIGHT = int(os.getenv("BLOCKHEIGHT", fetch_latest_block(network=NETWORK)))
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

EVENT_LOOP = asyncio.new_event_loop()

async def main():
    print(f'block height: {BLOCKHEIGHT}')
    latest_final_block = BLOCKHEIGHT
    config = LakeConfig(
        NETWORK,
        start_block_height=latest_final_block,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_key=AWS_SECRET_ACCESS_KEY,
        preload_pool_size=5,
    )

    stream_handle, streamer_messages_queue = streamer(config)
    processed = 0
    # print("FUGGIT")
    # sys.exit(1)
    try:
        while True:
            print(f'Processing block {BLOCKHEIGHT + processed} ({processed})')
            streamer_message = await streamer_messages_queue.get()
            process_streamer_message(streamer_message)

            # FIXME: do not go past limit
            processed += 1
            if processed >= LIMIT:
                while not streamer_messages_queue.empty():
                    await streamer_messages_queue.get_nowait()
                stream_handle.cancel()
                await stream_handle
                break
    except asyncio.CancelledError:
        pass
    finally:
        stream_handle.cancel()
        await stream_handle
              


def process_streamer_message(streamer_message: near_primitives.StreamerMessage):
    print("  Processing message")
    for shard in streamer_message.shards:
        print(f"  Processing shard {shard.shard_id}")
        for receipt_execution_outcome in shard.receipt_execution_outcomes:
            if receipt_execution_outcome.executor_id:
                print(f"Got execution: {receipt_execution_outcome}")
                # for log in receipt_execution_outcome.execution_outcome.outcome.logs:
                #     print(f"Got lot: {log}")


if __name__ == "__main__":
    try:
        EVENT_LOOP.run_until_complete(main())
    finally:
        EVENT_LOOP.run_until_complete(EVENT_LOOP.shutdown_asyncgens())
        EVENT_LOOP.close()
