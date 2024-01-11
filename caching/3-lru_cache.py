#!/usr/bin/env python3
"""Module containing the LRUCache class."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    and implements an LRU caching system.

    This caching system evicts the least recently
    used item once it exceeds its
    maximum capacity. The access order of items is
    tracked to determine which item
    should be evicted.
    """

    def __init__(self):
        """
        Initialize the LRUCache.

        Overrides the parent class __init__ method.
        Initializes the access_order list
        which tracks the order in which items are accessed.
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache exceeds its maximum capacity as
        defined by BaseCaching.MAX_ITEMS,
        the least recently used item is removed first.
        If the key or item is None,
        nothing is added to the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
        """
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
        """
        Retrieve an item by key.

        Returns the value stored in the cache.
        If the key is None or the key does not
        exist in the cache, None is returned.
        If the key exists, it becomes the most
        recently used item.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The value stored in the cache or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
