#!/usr/bin/env python3
"""Task 4"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru = self.access_order[-1]
                del self.cache_data[mru]
                self.access_order.pop()
                print("DISCARD: {}".format(mru))

            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
