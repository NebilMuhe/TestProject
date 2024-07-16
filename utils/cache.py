from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=300)

def get_cached_posts(user_id: int):
    return cache.get(user_id)

def set_cached_posts(user_id: int, posts):
    cache[user_id] = posts
