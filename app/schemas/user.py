from pydantic import BaseModel, ConfigDict, Field

class UserBase(BaseModel):
    username: str = Field(..., examples=["johndoe"])
    # NOTE: In production, you might install `pydantic[email]` and use `EmailStr` instead of `str`
    email: str = Field(..., examples=["john@example.com"])
    is_active: bool = Field(default=True)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = Field(default=None, min_length=8)

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
