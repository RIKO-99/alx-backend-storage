""" web module """

import requests
from cachetools import Cache, TTLCache

# Initialize a cache with a 10-second expiration time
cache = TTLCache(maxsize=128, ttl=10)

def get_page(url: str) -> str:
    # Check if the URL is already in the cache
    if url in cache:
        return cache[url]

    # Make an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        content = response.text

        # Increment the access count and store it in the cache
        cache["count:" + url] = cache.get("count:" + url, 0) + 1

        # Cache the content with a 10-second expiration
        cache[url] = content

        return content
    else:
        raise Exception(f"Failed to fetch content from {url}")

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://example.com"
    
    try:
        content = get_page(url)
        print(content)
    except Exception as e:
        print(f"An error occurred: {e}")

