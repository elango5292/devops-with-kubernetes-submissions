import os

import hashlib
import uuid
import time
from datetime import datetime,timezone

WRITE_PATH = os.getenv("SHARED_HASH_PATH", "./hash.txt")

random_string = str(uuid.uuid4())
cache_string = hashlib.sha256(random_string.encode()).hexdigest()

while True:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{datetime.now(timezone.utc).microsecond // 1000:03d}Z"
    final_string = f"{timestamp}: {cache_string}"
    with open(WRITE_PATH, 'w') as f:
        f.write(final_string)
    time.sleep(5)

