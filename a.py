import time

def rate_limited(key, limit=5, window=60):
    """
    Returns True if allowed, False if rate-limited.
    key    -> user/ip/api-key identifier
    limit  -> max requests per window
    window -> time window in seconds
    """
    now = int(time.time())
    if not hasattr(rate_limited, "store"):
        rate_limited.store = {}

    count, start = rate_limited.store.get(key, (0, now))

    if now - start >= window:
        rate_limited.store[key] = (1, now)
        return True

    if count < limit:
        rate_limited.store[key] = (count + 1, start)
        return True

    return False
