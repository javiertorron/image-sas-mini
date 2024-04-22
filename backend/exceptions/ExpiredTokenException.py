from fastapi import HTTPException, status


class ExpiredTokenException(HTTPException):
    def __init__(self, detail: str = "Token has expired"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
