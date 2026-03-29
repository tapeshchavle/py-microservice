from fastapi import APIRouter
from app.clients.java_rest_client import fetch_items_from_java, fetch_users_from_java
from app.clients.java_grpc_client import fetch_items_via_grpc, fetch_users_via_grpc

router = APIRouter(prefix="/java-integration", tags=["Java Testing (As Server)"])

@router.get("/rest/items")
async def get_items_rest():
    """Fetches Items from the Java Server using HTTP/REST"""
    return await fetch_items_from_java()

@router.get("/rest/users")
async def get_users_rest():
    """Fetches Users from the Java Server using HTTP/REST"""
    return await fetch_users_from_java()

@router.get("/grpc/items")
async def get_items_grpc():
    """Fetches Items from the Java Server using pure high-speed gRPC"""
    return await fetch_items_via_grpc()

@router.get("/grpc/users")
async def get_users_grpc():
    """Fetches Users from the Java Server using pure high-speed gRPC"""
    return await fetch_users_via_grpc()
