from pydantic import BaseModel, ConfigDict, Field

class ItemBase(BaseModel):
    name: str = Field(..., examples=["Apple"])
    description: str | None = Field(default=None, examples=["A delicious red apple."])

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

class ItemResponse(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
