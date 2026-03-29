import httpx

JAVA_REST_URL = "http://localhost:8081/api"

async def fetch_items_from_java():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JAVA_REST_URL}/items")
        response.raise_for_status()
        return response.json()

async def fetch_users_from_java():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JAVA_REST_URL}/users")
        response.raise_for_status()
        return response.json()
