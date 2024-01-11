#!/usr/bin/env python3
"""Task 3"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru = self.access_order.pop(0)
                del self.cache_data[lru]
                print("DISCARD: {}".format(lru))

            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
