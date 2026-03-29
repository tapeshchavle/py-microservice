from app.schemas.user import UserCreate, UserUpdate, UserResponse

# Hardcoded static database for Users
STATIC_USERS_DB = [
    {"id": 1, "username": "admin", "email": "admin@example.com", "is_active": True},
    {"id": 2, "username": "tapesh", "email": "tapesh@example.com", "is_active": True},
]

class UserService:
    @staticmethod
    def get_all_users() -> list[UserResponse]:
        """Returns all users."""
        return [UserResponse(**user) for user in STATIC_USERS_DB]

    @staticmethod
    def get_user(user_id: int) -> UserResponse | None:
        """Returns a single user by ID."""
        for user in STATIC_USERS_DB:
            if user["id"] == user_id:
                return UserResponse(**user)
        return None

    @staticmethod
    def create_user(user_in: UserCreate) -> UserResponse:
        """Creates a new user."""
        new_id = len(STATIC_USERS_DB) + 1 if STATIC_USERS_DB else 1
        
        user_dict = user_in.model_dump()
        # Keep passwords private/unreturned. Normally we would hash it here.
        user_dict.pop("password", None)
        
        new_user = {"id": new_id, **user_dict}
        STATIC_USERS_DB.append(new_user)
        
        return UserResponse(**new_user)

    @staticmethod
    def update_user(user_id: int, user_in: UserUpdate) -> UserResponse | None:
        """Updates an existing user."""
        for idx, user in enumerate(STATIC_USERS_DB):
            if user["id"] == user_id:
                update_data = user_in.model_dump(exclude_unset=True)
                update_data.pop("password", None) # Avoid leaking password on update
                 
                updated_user = {**user, **update_data}
                STATIC_USERS_DB[idx] = updated_user
                return UserResponse(**updated_user)
        return None

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Deletes a user by ID."""
        for idx, user in enumerate(STATIC_USERS_DB):
            if user["id"] == user_id:
                STATIC_USERS_DB.pop(idx)
                return True
        return False
