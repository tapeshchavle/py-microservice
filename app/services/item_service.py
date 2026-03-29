from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse

# This is our temporary hardcoded database. 
# We will replace this with a real SQLAlchemy database in Phase 3.
FAKE_DB = [
    {"id": 1, "name": "MacBook Pro", "description": "M3 Max Chip, 36GB RAM"},
    {"id": 2, "name": "Logitech MX Master 3S", "description": "Wireless Productivity Mouse"},
]

class ItemService:
    @staticmethod
    def get_all_items() -> list[ItemResponse]:
        """Returns all items from the database."""
        return [ItemResponse(**item) for item in FAKE_DB]

    @staticmethod
    def get_item(item_id: int) -> ItemResponse | None:
        """Returns a single item by its ID."""
        for item in FAKE_DB:
            if item["id"] == item_id:
                return ItemResponse(**item)
        return None

    @staticmethod
    def create_item(item_in: ItemCreate) -> ItemResponse:
        """Creates a new item and saves it."""
        # Generate a new ID based on the current length (not safe for real DBs, but fine for hardcoded!)
        new_id = len(FAKE_DB) + 1 if FAKE_DB else 1
        
        # Convert Pydantic object to dictionary and merge with new ID
        new_item = {"id": new_id, **item_in.model_dump()}
        FAKE_DB.append(new_item)
        
        return ItemResponse(**new_item)

    @staticmethod
    def update_item(item_id: int, item_in: ItemUpdate) -> ItemResponse | None:
        """Updates an existing item."""
        for idx, item in enumerate(FAKE_DB):
            if item["id"] == item_id:
                # exclude_unset=True ensures we only update fields the user actually passed
                update_data = item_in.model_dump(exclude_unset=True)
                
                # Merge old data with new data
                updated_item = {**item, **update_data}
                FAKE_DB[idx] = updated_item
                return ItemResponse(**updated_item)
        return None

    @staticmethod
    def delete_item(item_id: int) -> bool:
        """Deletes an item by ID."""
        for idx, item in enumerate(FAKE_DB):
            if item["id"] == item_id:
                FAKE_DB.pop(idx)
                return True
        return False
