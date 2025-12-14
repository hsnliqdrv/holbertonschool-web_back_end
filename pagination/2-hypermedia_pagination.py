#!/usr/bin/env python3
"""2-hypermedia_pagination

Hypermedia Pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """Gives a tuple containing start and end index"""
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets pages from dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Gets hypermedia metadata from dataset"""
        length = len(self.dataset())
        pages = self.get_page(page, page_size)
        metadata = {}
        metadata['page_size'] = len(pages)
        metadata['page'] = page
        metadata['data'] = pages
        next_page_exists = index_range(page + 1, page_size)[0] < length
        metadata['next_page'] = None if not next_page_exists else page + 1
        metadata['prev_page'] = None if page <= 1 else page - 1
        metadata['total_pages'] = math.ceil(l / page_size)
        return metadata
