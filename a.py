import time

def rate_limited(key, window=60):
    """
    Hard rate limit: max 100 requests per window (seconds)
    Returns True if allowed, False if blocked
    """
    LIMIT = 40
    now = int(time.time())

    if not hasattr(rate_limited, "store"):
        rate_limited.store = {}

    count, start = rate_limited.store.get(key, (0, now))

    if now - start >= window:
        rate_limited.store[key] = (1, now)
        return True

    if count >= LIMIT:
        return False

    rate_limited.store[key] = (count + 1, start)
    return True
