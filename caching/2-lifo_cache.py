#!/usr/bin/env python3
"""Task 2"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key_added = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key_added))
                del self.cache_data[self.last_key_added]

            self.cache_data[key] = item
            self.last_key_added = key

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
