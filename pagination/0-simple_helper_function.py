#!/usr/bin/env python3
"""0-simple_helper_function

Provides a simple helper function
"""


def index_range(page: int, page_size: int):
    """Gives a tuple containing start and end index"""
    return (page - 1) * page_size, page * page_size
