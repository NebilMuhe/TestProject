from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=300)

def get_cached_posts(user_id: str):
    return cache.get(user_id)

def set_cached_posts(user_id: str, posts):
    cache[user_id] = posts
