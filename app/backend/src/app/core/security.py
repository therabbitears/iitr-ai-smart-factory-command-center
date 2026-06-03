from fastapi import HTTPException, status
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)


async def get_api_key(api_key_header: str | None = None) -> str:
    if api_key_header != "changeme":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return api_key_header
