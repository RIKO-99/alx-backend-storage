"""import necessary modules """
import uuid
import redis

class Cache:
    def __init__(self, redis_host="localhost", redis_port=6379, db=0):
        # Initialize a Redis client and flush the database
        self._redis = redis.Redis(host=redis_host, port=redis_port, db=db)
        self._redis.flushdb()

    def store(self, data: str or bytes or int or float) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())

        # Convert the data to a string (if not already)
        if not isinstance(data, str):
            data = str(data)

        # Store the data in Redis with the random key
        self._redis.set(key, data)

        return key
