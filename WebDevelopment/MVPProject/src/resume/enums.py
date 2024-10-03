from enum import Enum


class PaginationOrder(str, Enum):
    CREATED_AT: str = "created_at"
    VOTE_COUNT: str = "vote_count"
