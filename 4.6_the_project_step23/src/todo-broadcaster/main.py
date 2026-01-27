import asyncio
import os
import requests
import nats
import logging
import sys
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

async def main():
    nats_url = os.getenv("NATS_URL", "nats://localhost:4222")
    webhook_url = os.getenv("WEBHOOK_URL")

    if not webhook_url:
        logger.warning("WEBHOOK_URL not set. Messages will only be logged.")

    try:
        nc = await nats.connect(nats_url)
        logger.info(f"Connected to NATS at {nats_url}")
    except Exception as e:
        logger.error(f"Failed to connect to NATS: {e}")
        return

    async def message_handler(msg):
        data = msg.data.decode()
        logger.info(f"Received NATS message raw: {data}")

        if not webhook_url:
            return

        try:
            # Try parsing as JSON
            try:
                event = json.loads(data)
            except json.JSONDecodeError:
                # Fallback for old plain text messages
                event = {"action": "unknown", "raw": data}

            embed = {}
            if event.get("action") == "create":
                embed = {
                    "title": "🆕 Todo Created",
                    "color": 3066993, # Green
                    "fields": [{"name": "Task", "value": event.get("todo", "N/A")}],
                    "footer": {"text": "Todo App Broadcaster"}
                }
            elif event.get("action") == "update":
                status = "Done" if event.get("done") else "Not Done"
                color = 15105570 if int(event.get("done", 0)) else 15158332 # Orange or Red-ish
                embed = {
                    "title": "✏️ Todo Updated",
                    "color": color,
                    "fields": [
                        {"name": "ID", "value": str(event.get("id", "N/A")), "inline": True},
                        {"name": "Status", "value": status, "inline": True}
                    ],
                    "footer": {"text": "Todo App Broadcaster"}
                }
            else:
                 # Generic fallback
                 embed = {
                    "title": "NATS Message",
                    "description": data,
                    "color": 9807270
                 }

            payload = {
                "username": "Todo Bot 🤖",
                "avatar_url": "https://i.imgur.com/4M34hi2.png",
                "embeds": [embed]
            }

            response = requests.post(webhook_url, json=payload)
            if response.status_code >= 400:
                logger.error(f"Failed to send to webhook: {response.status_code} {response.text}")
            else:
                logger.info(f"Forwarded to webhook: {response.status_code}")

        except Exception as e:
            logger.error(f"Error forwarding to webhook: {e}")

    # Subscribe with Queue Group for scaling
    queue_group = "broadcaster_workers"
    subject = "todo_updates"

    await nc.subscribe(subject, queue=queue_group, cb=message_handler)
    logger.info(f"Subscribed to '{subject}' with queue group '{queue_group}'")

    # Keep running
    try:
        # Create a future that never completes to keep the loop running
        await asyncio.Future()
    except asyncio.CancelledError:
        await nc.close()
        logger.info("Broadcaster shutting down")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
