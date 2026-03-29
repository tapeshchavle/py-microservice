import grpc
from protos import item_pb2, item_pb2_grpc
from protos import user_pb2, user_pb2_grpc

# Java's standalone gRPC server runs on 9090 natively
JAVA_GRPC_URL = "localhost:9090"

async def fetch_items_via_grpc():
    # Use standard python async gRPC client directly
    async with grpc.aio.insecure_channel(JAVA_GRPC_URL) as channel:
        stub = item_pb2_grpc.ItemGrpcServiceStub(channel)
        request = item_pb2.EmptyRequest()
        response = await stub.GetAllItems(request)
        
        # Convert Protobuf Objects back into Standard Python Dicts
        return [{"id": item.id, "name": item.name, "description": item.description} for item in response.items]

async def fetch_users_via_grpc():
    async with grpc.aio.insecure_channel(JAVA_GRPC_URL) as channel:
        stub = user_pb2_grpc.UserGrpcServiceStub(channel)
        request = user_pb2.EmptyUserRequest()
        response = await stub.GetAllUsers(request)
        return [{"id": u.id, "username": u.username, "email": u.email} for u in response.users]
