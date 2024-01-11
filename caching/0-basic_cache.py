#!/usr/bin/env python3
"""Module containing the BasicCache class."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    and is a basic caching system.

    This caching system does not have a limit and stores
    all items put into it
    unless explicitly removed.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        This method assigns the item value for the given key
        in the cache_data dictionary.
        If the key or item is None, the item is not added to the cache.

        Args:
            key: The key under which the item is stored in the cache.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key.

        This method returns the value stored in cache_data
        corresponding to the given key.
        If the key is None or if the key doesn’t exist
        in cache_data, None is returned.

        Args:
            key: The key whose value is to be returned from the cache.

        Returns:
            The value associated with key in the cache, or
            None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
