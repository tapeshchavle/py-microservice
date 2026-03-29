from fastapi import APIRouter, HTTPException, status
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=list[ItemResponse])
def get_items():
    return ItemService.get_all_items()

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    item = ItemService.get_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item_in: ItemCreate):
    return ItemService.create_item(item_in)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_in: ItemUpdate):
    item = ItemService.update_item(item_id, item_in)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    success = ItemService.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
