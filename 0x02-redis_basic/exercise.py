""" import the necessary modules """
  from redis import Redis
  import uuid

  class Cache:
      """ a class that instantiate redis function """

      def __init__(self):
          self._redis = Redis()
          self._redis.flushdb()

      """ create a method that takes data argument """
      def store(self, data:str|bytes|int|float) -> str:
          key = str(uuid.uuid4())
          self._redis.set(key, data)
          return key
