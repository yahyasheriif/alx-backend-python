#!/usr/bin/env python3
"""Generic utilities for GitHub organization client."""

import requests
from functools import wraps
from typing import Mapping, Sequence, Any, Dict, Callable


__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map using a sequence of keys.

    Args:
        nested_map: A dictionary with nested dictionaries.
        path: A sequence of keys representing the access path.

    Returns:
        The value found at the end of the path.

    Raises:
        KeyError: If any key along the path is missing.
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Dict:
    """
    Make a GET request to a given URL and return the JSON response.

    Args:
        url: The URL to request.

    Returns:
        A dictionary representing the JSON response.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """
    Decorator to cache the result of a method.

    The cached result is stored in an attribute named after the method.

    Args:
        fn: The method to cache.

    Returns:
        The memoized property.
    """
    attr_name = f"_{fn.__name__}"

    @wraps(fn)
    def memoized(self):
        """Return cached result if available, otherwise call and store result."""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
