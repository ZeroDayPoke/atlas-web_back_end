#!/usr/bin/env python3
"""Task 1"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.cache_order:
                self.cache_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_order.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
