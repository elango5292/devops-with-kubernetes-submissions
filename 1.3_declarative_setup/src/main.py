import hashlib
import uuid
import time
from datetime import datetime,timezone

random_string = str(uuid.uuid4())
hash_value = hashlib.sha256(random_string.encode()).hexdigest()

while True:
    # ISO 8601 format
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{datetime.now(timezone.utc).microsecond // 1000:03d}Z"

    print(f"{timestamp}: {hash_value}")
    time.sleep(5)