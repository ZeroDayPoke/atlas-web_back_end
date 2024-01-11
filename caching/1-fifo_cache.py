#!/usr/bin/env python3
"""Task 1"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    and implements a FIFO caching system.

    This caching system evicts the least recently
    added item once it exceeds its
    maximum capacity.
    """

    def __init__(self):
        """
        Initialize the FIFOCache.

        Overrides the parent class __init__ method.
        Initializes the cache order list
        which tracks the order in which items were added to the cache.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache exceeds its maximum capacity as
        defined by BaseCaching.MAX_ITEMS,
        the least recently added item is removed first.
        If the key or item is None,
        nothing is added to the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.cache_order:
                self.cache_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_order.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """
        Retrieve an item by key.

        Returns the value stored in the cache.
        If the key is None or the key does not
        exist in the cache, None is returned.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The value stored in the cache or None if not found.
        """
        return self.cache_data.get(key, None)
