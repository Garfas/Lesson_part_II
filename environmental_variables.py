#2023.03.22
from typing import Optional


from pydantic import BaseSettings,  IPvAnyAddress

class Settings(BaseSettings):
    MONGODB_URL: IPvAnyAddress
    API_V1_STR: str = "/api/v1"
    GF_API_URL: Optional[str] = None
    TOKEN_SECRET_KEY: str ="fj0823t8y3t9shoidn9184h13iudhaslidfuh3190841-00=52394hfu"
    
settings = Settings()

print(settings.MONGODB_URL)