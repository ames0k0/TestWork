from fastapi import HTTPException, status


class RecordIDAndUserIDAreRequired(HTTPException):
    """Record id and User id are required"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Queries `id=` and `user=` are required",
        )
