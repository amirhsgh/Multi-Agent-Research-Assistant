import redis
import json
import hashlib
from typing import Optional, Any



class RedisCache:

    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )

    def _generate_key(self, text: str) -> str:

        return hashlib.md5(
            text.encode()
        ).hexdigest()


    def get(self, key: str) -> Optional[Any]:
        """خواندن cache"""

        cached = self.redis_client.get(key)

        if cached:
            return json.loads(cached)

        return None

    def set(
        self,
        key: str,
        value: Any,
        expire: int = 3600
    ):
        """ذخیره cache"""

        self.redis_client.setex(
            key,
            expire,
            json.dumps(value)
        )

    def cached_search(
        self,
        query: str,
        search_func
    ):
        """جستجو با cache"""

        cache_key = self._generate_key(query)

        cached_result = self.get(cache_key)

        if cached_result:
            return {
                "source": "cache",
                "data": cached_result
            }

        result = search_func(query)

        self.set(cache_key, result)

        return {
            "source": "api",
            "data": result
        }