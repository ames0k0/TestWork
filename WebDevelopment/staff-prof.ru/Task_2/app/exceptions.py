from fastapi import HTTPException, status


class RecordIDAndUserIDAreRequired(HTTPException):
    """Record id and User id are required"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Queries `id=` and `user=` are required",
        )


class UserIDOrTokenIsInvalid(HTTPException):
    """User id and/or token are invalid"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="User `id=` and/or `token=` are invalid",
        )


class RecordIDOrUserIDIsInvalid(HTTPException):
    """Record id and/or User id are invalid"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="RecordID `id=` and/or UserID `user=` are invalid",
        )
