#!/usr/bin/env python3
"""Module containing the LIFOCache class."""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and
    implements a LIFO caching system.

    This caching system evicts the most recently added
    item once it exceeds its
    maximum capacity. The exception is if the most recently
    added item is put again,
    in which case the item added before it is removed.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.

        Overrides the parent class __init__ method.
        Initializes last_key_added variable
        to keep track of the last key added to the cache.
        """
        super().__init__()
        self.last_key_added = None

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache exceeds its maximum capacity
        as defined by BaseCaching.MAX_ITEMS,
        the most recently added item is removed.
        If the key or item is None, nothing
        is added to the cache.

        Args:
            key: The key under which the item will be stored.
            item: The item to be stored in the cache.
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
